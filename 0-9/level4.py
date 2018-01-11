import urllib2


def main():
    resp = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579").read()
    t = 0
    while True:
        print(t)
        t = t + 1
        print(resp)

        if t >= 400:
            break
        if resp.startswith("<font color=red>Your hands are getting tired </font>and the next nothing is "):
            resp = resp.replace("<font color=red>Your hands are getting tired </font>and the next nothing is ", "")
            resp = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + resp).read()
        elif resp.startswith("and the next nothing is "):
            resp = resp.replace("and the next nothing is ", "")
            resp = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + resp).read()
        else:
            print(resp)

            break


if __name__ == '__main__':
    main()
