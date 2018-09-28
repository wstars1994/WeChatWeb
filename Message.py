from HttpClient import HttpClient
from WeChatUrl import WeChatUrl
class Message() :

    def recv(self,model):
        while(1):
            url = WeChatUrl.MSG_REC_RUL % (model.skey,model.lang,model.ticket,model.sid);
            result = HttpClient().rq(url,bytearray(model.get_base_request(), 'utf8'),{"Content-Type":"application/json;charset=utf-8","Connection": "keep-alive", "Keep-Alive": "timeout=60, max=2"});
            print(result);