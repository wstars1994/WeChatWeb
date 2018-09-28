from HttpClient import HttpClient
from WeChatUrl import WeChatUrl
from datetime import datetime
class Message() :

    def recv(self,model):
        i=1;
        while(i>0):
            url = WeChatUrl.MSG_REC_RUL % (model.skey,model.lang,model.ticket,model.sid);
            data = model.get_base_request();
            # timestamp = int(datetime.now().timestamp());
            data = bytearray(data, 'utf8');
            print(HttpClient.res_cookie);
            result = HttpClient().rq(url,data,{});
            print(result);
            i=i-1;