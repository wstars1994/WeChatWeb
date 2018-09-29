import json

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

    def final_login_check(self,result):
        json_res = json.loads(result);
        base_response = json_res['BaseResponse'];
        ret = base_response['Ret'];
        msg = base_response['ErrMsg'];
        sync_key = {};
        if ret==0 :
            sync_key = json_res['SyncKey'];
        return [ret,msg,sync_key];