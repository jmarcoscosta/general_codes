from urllib.request import urlopen 
html = urlopen("https://pt.wikipedia.org/wiki/J%C3%BAlio_C%C3%A9sar")
print(html.read())