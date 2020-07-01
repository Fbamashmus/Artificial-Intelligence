from urllib.request import urlopen


f = urlopen("https://www.ros.org/")
print(f.read())
