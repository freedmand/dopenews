import re, codecs

ARTICLE = """
<!DOCTYPE html>
<html>

<head>
    <title>%s</title>
    <link href="../style.css" rel="stylesheet" type="text/css">
</head>

<body>
    <div class="sidebar-container">
        <a href="../index.html">
            <img src="../dopemini.png" id="dopemini">
        </a>
        <ul class="sidebar-container">
            <a href="../baseball.html">
                <li class="sidebar">BASEBALL</li>
            </a>
            <a href="../weightlifting.html">
                <li class="sidebar" style="letter-spacing: 0.1em;">WEIGHTLIFTING</li>
            </a>
            <a href="../track.html">
                <li class="sidebar" style="letter-spacing: 0.1em;">TRACK &amp; FIELD</li>
            </a>
            <a href="../cycling.html">
                <li class="sidebar">CYCLING</li>
            </a>
            <a href="../chess.html">
                <li class="sidebar">CHESS</li>
            </a>
            <a href="../retailers.html">
                <li class="sidebar" style="letter-spacing: 0.1em;">RETAILERS</li>
            </a>
            <a href="../about.html">
                <li class="sidebar" style="letter-spacing: 0.02em;">ABOUT</li>
            </a>
        </ul>
    </div>

    <div class="main-content-article">
        <div class="article-container">
            <div class="article-container-head"></div>
            <div class="article-container-tail"></div>
            <h2>%s</h2>
            <h1>%s</h1>
            <div class="byline">by %s</div>

            %s
        </div>

    </div>

</body>

</html>
"""

LIST = """
<!DOCTYPE html>
<html>

<head>
    <title>%s News</title>
    <link href="style.css" rel="stylesheet" type="text/css">
</head>

<body>
    <div class="sidebar-container">
        <a href="index.html">
            <img src="dopemini.png" id="dopemini">
        </a>
        <ul class="sidebar-container">
            <a href="baseball.html">
                <li class="sidebar">BASEBALL</li>
            </a>
            <a href="weightlifting.html">
                <li class="sidebar" style="letter-spacing: 0.1em;">WEIGHTLIFTING</li>
            </a>
            <a href="track.html">
                <li class="sidebar" style="letter-spacing: 0.1em;">TRACK &amp; FIELD</li>
            </a>
            <a href="cycling.html">
                <li class="sidebar">CYCLING</li>
            </a>
            <a href="chess.html">
                <li class="sidebar">CHESS</li>
            </a>
            <a href="retailers.html">
                <li class="sidebar" style="letter-spacing: 0.1em;">RETAILERS</li>
            </a>
            <a href="about.html">
                <li class="sidebar" style="letter-spacing: 0.02em;">ABOUT</li>
            </a>
        </ul>
    </div>

    <div class="main-content">
        <h1>%s News</h1>

        <ul class="article-list">
%s
        </ul>
    </div>
</body>

</html>
"""

LIST_ENTRY = """
            <li class="article-list">
                <h4>%s</h4>
                <a class="article-link" href="%s">
                    <h3>%s</h3>
                </a>
            </li>
"""

files = ['baseball.txt', 'weightlifting.txt', 'track.txt', 'cycling.txt', 'chess.txt']
html_files = ['baseball.html', 'weightlifting.html', 'track.html', 'cycling.html', 'chess.html']
folders = ['bsbl', 'wght', 'trck', 'cycl', 'chss']
english = ['Baseball', 'Weightlifting', 'Track & Field', 'Cycling', 'Chess']

url_chars = 'abcdefghijklmnopqrstuvwxyz0123456789_'

def urlize(fn):
  name = fn.lower().replace(' ','_')
  return filter(lambda x: x in url_chars, name)[:40] + '.html'

for i in xrange(len(files)):
  t = codecs.open(files[i], "r", "utf-8").read()
  articles = t.split('\nXXXXX\nXXXXX')
  list_entries = []
  for article in articles:
    split = article.split('\nXXXXX')
    if len(split) != 4:
      continue
    title = split[0].strip().encode('ascii', 'xmlcharrefreplace')
    author = split[1].strip().upper().encode('ascii', 'xmlcharrefreplace')
    date = split[2].strip().encode('ascii', 'xmlcharrefreplace')
    content = split[3].strip().encode('ascii', 'xmlcharrefreplace')
    content = "<p>" + re.sub("[\n]+", "</p><p>", content) + "</p>"
    
    html = ARTICLE % (title, date, title, author, content)

    fn = folders[i] + '/' + urlize(title)
    f = open(fn, 'w')
    f.write(html)
    f.close()
    list_entries += [(date, fn, title)]
  listings = '\n'.join([LIST_ENTRY % (entry[0], entry[1], entry[2]) for entry in list_entries])
  list_page = LIST % (english[i], english[i], listings)
  f = open(html_files[i], 'w')
  f.write(list_page)
  f.close()
