import os
from datetime import date

today = date.today()

f = open("index.html", "w")

html_str = ("""
<!DOCTYPE html>
<html>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<head>
<link rel="stylesheet" href="https://paologhin.github.io/turnivet/style.css">
</head>
<body>

<div class="header-color">
  <div class="header">
  <img id="header-image" src="https://raw.githubusercontent.com/paologhin/turnivet/main/bovini.jpg">
  <h1 id="title">TurniVet</h1>
<p id="subtitle">Ultimo aggiornamento <b>""" + 
today.strftime("%d/%m/%y") + "</b></p>\n" +
"""
  </div> 
</div>

<table>
""")

for file in os.listdir("./"):
    if file.endswith(".html"):
        if file != "index.html":
            html_str += "\n<tr><td><A HREF=https://paologhin.github.io/turnivet/" + file + ">" + file.removesuffix('.html')
            html_str += "</A></td></tr>"

html_str += """
</table>

</body>
</html>
"""

f.write(html_str)
f.close()


