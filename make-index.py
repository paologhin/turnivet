import os

f = open("index.html", "w")

html_str = """
<!DOCTYPE html>
<html>
<body>

<h2>TurniVet</h2>

"""

for file in os.listdir("./"):
    if file.endswith(".html"):
        if file != "index.html":
            html_str += "\n<A HREF=https://paologhin.github.io/turnivet/" + file + ">" + file.removesuffix('.html') + "</A>"
            html_str += "\n<br><br>"

html_str += """

</body>
</html>
"""

f.write(html_str)
f.close()
