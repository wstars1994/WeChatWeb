class WeChatResultCheck():
    def uuid_check(self,result):
        resultArr = result.split(";");
        if len(resultArr)==3:
            return [0,resultArr[1].split("\"")[1]];
        else:
            return [1,"返回错误"]

    def first_login_check(self,result):
        resultArr = result.split(";");
        code = resultArr[0].split("=")[1];
        if int(code)==200:
            return [code,resultArr[1].split("\"")[1]];
        return [code];