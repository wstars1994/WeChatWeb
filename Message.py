from httpreq.HttpClient import HttpClient
from httpreq.HttpWXUrl import WeChatUrl
from httpreq.ResultCheck import ResultCheck
from datetime import datetime
from httpreq.HttpHeader import HttpHeader

class Message(object) :

    def recv(self,model):
        list = model.sync_key["List"];
        sync_key_list = [];
        for key in list:
            sync_key_list.append(str(key["Key"]) + "_" + str(key["Val"]));
        sync_key = "|".join(sync_key_list);

        while(1):
            timestamp = int(datetime.now().timestamp());
            url = WeChatUrl.MSG_SYNC_CHECK_URL % (timestamp * 1000, model.skey, model.uin, sync_key, model.sid);
            HttpHeader().add_cookie({"wxpluginkey": timestamp});
            result = HttpClient().rq(url, None, {"Host":"webpush.wx.qq.com"});
            result = ResultCheck().sync_check(result);
            if result[0]==0:
                if result[1]>0:#有新消息,发起请求
                    self.__message(model);
                    pass


    def __message(self,model):
        url = WeChatUrl.MSG_REC_RUL % (model.skey, model.lang, model.ticket, model.sid);
        data = bytearray(model.get_base_request(), 'utf8');
        result = HttpClient().rq(url, data, {});
        print(result);



        # while(1):
        #     url = WeChatUrl.MSG_REC_RUL % (model.skey,model.lang,model.ticket,model.sid);
        #     # timestamp = int(datetime.now().timestamp());
        #     data = bytearray(model.get_base_request(), 'utf8');
        #     result = HttpClient().rq(url,data,{});
        #     print(result);