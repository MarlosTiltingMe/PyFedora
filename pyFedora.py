import json, requests, os, sys

headers = {
    'User-Agent': '/u/YourUsername'
}

try:
    os.remove("pyFedora.html")
except OSError:
    print('No cleanup.')

file = open("pyFedora.html", "a")

#I refuse to believe Python can be aesthetically pleasing.
#So I didn't try. This is a project of necessity and boredom.

def setup():

    global FOOTER
    global user_name
    global sub_reddit
    global url

    user_name  = raw_input("What's your name? \n")
    sub_reddit = raw_input("What Reddit would you like to view?\n")
    url = 'https://reddit.com/r/' + sub_reddit + '/hot.json'

    HEADER = """
        <html>
            <head>
                <title>pyFedora</title>
                <link rel="stylesheet" type="text/css" href="http://marlo.club/static/lib/bootstrap/bootstrap.min.css" />
                <link rel="stylesheet" type="text/css" href="http://marlo.club/static/lib/bootstrap/bootstrap-theme.min.css" />
                <style>
                .grow {
                  transition: all .2s ease-in-out;
                  border: 1px solid #f0f0f0;
                  border-bottom: 2px solid #ccc;
                  -webkit-border-radius:5px;
                  -moz-border-radius:5px;
                  border-radius:5px;
                  outline: 1px solid #ddd;
                  border-top: 1px solid #fff;
                  padding: 10px;
                  background: #f0f0f0;
                }
                .grow:hover { transform: scale(1.3); }
                .container {
                    width:70%;
                }
                img {
                    width:30%;
                    height:30%;
                }
                body {
                    background-color:#ccc;
                }
                .heading {
                    background-color:#232323;
                    border:1px solid white;
                    width:30%;
                }
            </style>
            </head>
            <body>
            <div id="nav" class="nav navbar-inverse">
                <a class="navbar-brand" href="/">""" + user_name + """</a>
                <ul class="nav navbar-nav navbar-left">
                    <li><a href="http://reddit.com/r/"""+ sub_reddit +"""">
                    """+ sub_reddit + """</a></li>
                </ul>
            </div>
            <center><div class='container'>"""

    file.write(HEADER)
    FOOTER = """</div></center></body></html>"""


#Inside joke. This function right here? THIS FUNCTION'S A GO!
def go():
    global FOOTER
    r = requests.get(url, headers=headers)
    parsed = json.loads(r.text)

    for thread in parsed["data"]["children"]:
        if thread["data"].get('preview'):

            author = thread["data"]["author"]
            permalink = thread["data"]["permalink"]

            file.write("<h3 class='heading'><a href='http://reddit.com/u/" +
            author + "'>" +
            author + "</a></h3>")

            for image in thread["data"]["preview"]["images"]:
                file.write("<br /><a href='http://reddit.com" + permalink +
                 "'><img class='grow' src=\'" +
                image["source"]["url"] + "\'/></a><br>")


    file.write(FOOTER)
    file.close()

setup()
go()
