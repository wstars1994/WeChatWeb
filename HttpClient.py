import urllib.request as requestLib
import http.cookiejar as cookie
class HttpClient():

    #全局请求Cookie
    res_cookie = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",
            "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Referer":"https://wx.qq.com/?&lang=zh_CN",
            "Connection":"keep-alive",
            "mm_lang" : "zh_CN",
            "MM_WX_NOTIFY_STATE" : 1,
            "MM_WX_SOUND_STATE" : 1,
            "login_frequency":1,
            "Accept":"application/json,text/plain,*/*"
    };

    def rq(self,url, data=None, headers={}):
        HttpClient.res_cookie.update(headers);
        req = requestLib.Request(url, data,  HttpClient.res_cookie);
        res = requestLib.urlopen(req);
        self.__set_res_cookies(res.headers);
        return res.read().decode("utf-8");

    def download(url,filePath):
        requestLib.urlretrieve(url, filePath);

    def __set_res_cookies(self,headers):
        new_cookie = {};
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
                    if len(nv)==2:
                        new_cookie[nv[0].strip()] = nv[1];
                    else :
                        new_cookie[nv[0].strip()] = "";
        HttpClient.res_cookie.update(new_cookie);

