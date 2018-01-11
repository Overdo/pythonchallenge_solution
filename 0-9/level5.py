# view source code say's <!-- peak hell sounds familiar ? -->
# so pickle
# then we got source code
"""
<html>
<head>
  <title>peak hell</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<center>
<img src="peakhell.jpg"/>
<br><font color="#c0c0ff">
pronounce it
<br>
<peakhell src="banner.p"/>
</body>
</html>

"""
# the key is in the banner.p
# yes ,looks like pickle.dumps's result ,so

import pickle
import urllib2


def main():
    a = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p").readlines()
    data = pickle.loads(''.join(a))
    for r in data:
        result = ''
        for s in r:
            result = result + s[0] * s[1]
        print(result)
    # we got channel


if __name__ == '__main__':
    main()
