import urllib.request as requestLib
from httpreq.HttpHeader import HttpHeader

class HttpClient():

    def rq(self,url, data=None, headers={}):
        HttpHeader().add_header(headers);
        req = requestLib.Request(url, data, HttpHeader().get_headers());
        res = requestLib.urlopen(req,timeout=60);
        self.__set_res_cookies(res.headers);
        return res.read().decode("utf-8");

    def download(url,filePath):
        requestLib.urlretrieve(url, filePath);

    def __set_res_cookies(self,headers):
        keys = list(headers);
        header_values_list = list(headers.values());
        for i in range(len(keys)):
            if keys[i]=="Set-Cookie":
                value = header_values_list[i];
                cs = value.split(";");
                for cookie in cs:
                    nv = cookie.split("=",1);
                    if nv[0]==" Domain" or nv[0]==" Path" or nv[0]==" Expires" or nv[0]==" Secure":
                        continue;
                    HttpHeader().add_cookie({nv[0]:nv[1]});