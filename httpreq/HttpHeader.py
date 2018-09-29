class HttpHeader() :

    __cookies = {
        "mm_lang": "zh_CN",
        "MM_WX_NOTIFY_STATE": 1,
        "MM_WX_SOUND_STATE": 1,
        "login_frequency": 1
    };

    __res_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Referer": "https://wx.qq.com/?&lang=zh_CN",
        "Connection": "keep-alive",
        "Accept": "application/json,text/plain,*/*",
        "Cookie" :""
    };

    def add_header(self,new_header):
        self.__res_headers.update(new_header);

    def get_headers(self):
        #转化cookies
        cookies = [];
        for key in self.__cookies :
            cookies.append(key+"="+str(self.__cookies[key]));
        cookiesStr = ";".join(cookies);
        self.__res_headers["Cookie"] = cookiesStr+";";
        return self.__res_headers;

    def add_cookie(self,new_cookie={}):
        self.__cookies.update(new_cookie);