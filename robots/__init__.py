
import urllib.request
import urllib.error
import urllib.parse


class RobotsURLParser():
    def __init__(self):
        self.urlconvs = ["https://", "http://"]
        self.doNots = ["mailto:", "javascript:"]

    def parse(self, url, baseurl=False):
        if baseurl:
            for i in self.doNots:
                if i in baseurl:
                    return ''
            okurl = False
            if baseurl[0:2] == "//":
                baseurl = "http://" + baseurl
            for i in self.urlconvs:
                if i in baseurl:
                    okurl = True
            if okurl == False:
                baseurl = "http://" + baseurl
            if '#' in url:
                url = baseurl+url
        for i in self.doNots:
            if i in url:
                return ''
        okurl = False
        if url[0:2] == "//":
            url = "http:" + url
        for i in self.urlconvs:
            if i in url:
                okurl = True
        if okurl == False:
            url = "http://" + url
        if baseurl:
            splitbaseurl = baseurl.split("/")
            url = splitbaseurl[0]+"//"+splitbaseurl[2]+"/robots.txt"
        else:
            spliturl = url.split("/")
            baseurl = spliturl[2]
            url = spliturl[0]+"//"+baseurl+"/robots.txt"
        return url


class Parser():

    currentUserAgent = ""

    disallows = {}
    allows = {}

    def __init__(self, url):
        headers = {}  # Initializes header
        # Sets User Agent
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        urlparser = RobotsURLParser()
        newurl = urlparser.parse(url)
        req = urllib.request.Request(
            newurl, headers=headers)  # Initializes Request
        res = urllib.request.urlopen(req)  # Gets Response

        self.robots = res.read()
        self.robots = self.robots.decode()
        self.robots = self.robots.split("\n")
        for line in self.robots:
            if line == "\n":
                pass
            elif line == "":
                pass
            elif line[0] == "#":
                pass
            elif line[0] == " ":
                for i in line:
                    if line[i] != " ":
                        line = line[i:len(line)]
                    elif line[i] == "\n":
                        pass
            else:
                param = line.split(":")
                param[1] = param[1].replace(" ", "")
                if param[0].lower() == "User-Agent".lower():
                    self.currentUserAgent = param[1]
                elif param[0].lower() == "Disallow".lower():
                    psplit = param[1].replace(
                        "?*", "").replace("?", "").replace("*", "").split("//")
                    if len(psplit) == 1:
                        newparam = psplit[0]
                    else:
                        newparam = []
                        for i in psplit:
                            newparam.append(i)

                    if self.currentUserAgent != "":
                        if self.currentUserAgent in self.disallows:
                            self.disallows[self.currentUserAgent].append(
                                newparam)
                        else:
                            self.disallows[self.currentUserAgent] = []
                            self.disallows[self.currentUserAgent].append(
                                newparam)
                elif param[0].lower() == "Allow".lower():
                    psplit = param[1].replace(
                        "?*", "").replace("?", "").replace("*", "").split("//")
                    print(psplit)
                    if len(psplit) == 1:
                        newparam = psplit[0]
                    else:
                        newparam = []
                        for i in psplit:
                            newparam.append(i)

                    if self.currentUserAgent != "":
                        if self.currentUserAgent in self.allows:
                            self.allows[self.currentUserAgent].append(newparam)
                        else:
                            self.allows[self.currentUserAgent] = []
                            self.allows[self.currentUserAgent].append(newparam)
