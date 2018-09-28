import urllib.request as requestLib

class HttpClient():
    def rq(url, data=None, headers={}):
       return requestLib.urlopen(requestLib.Request(url,data,headers)).read().decode("utf-8");

    def download(url,filePath):
        requestLib.urlretrieve(url, filePath)
