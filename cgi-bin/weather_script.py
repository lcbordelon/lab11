#!/usr/bin/python3
print("Content-type: text/html")
print() # This extra newline is important!


print("""
<html>
  <head>
    <title>Weather Map Lab by Bordelon</title>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link href="/lab11/css/styles.css" rel="stylesheet" />
  </head>
  <body>
    <img src="../Blank_US_Map_(states_only).svg" alt="Weather Map" />
  </body>
</html>
""")

