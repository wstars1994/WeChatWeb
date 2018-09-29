from httpreq.HttpClient import HttpClient
from Contact import Contact
from httpreq.HttpWXUrl import WeChatUrl
from httpreq.ResultCheck import ResultCheck
from datetime import datetime
import time
from httpreq.HttpHeader import HttpHeader
import json

class Message(object) :

    def recv(self,model):
        while(1):
            list = model.sync_key["List"];
            sync_key_list = [];
            for key in list:
                sync_key_list.append(str(key["Key"]) + "_" + str(key["Val"]));
            sync_key = "|".join(sync_key_list);
            timestamp = int(datetime.now().timestamp());
            url = WeChatUrl.MSG_SYNC_CHECK_URL % (timestamp * 1000, model.skey, model.uin, sync_key, model.sid);
            HttpHeader().add_cookie({"wxpluginkey": timestamp});
            result = HttpClient().rq(url, None, {"Host":"webpush.wx.qq.com"});
            result = ResultCheck().sync_check(result);
            if result[0]==0:
                if result[1]>0:#有新消息,发起请求
                    self.__message(model);

    def __message(self,model):
        url = WeChatUrl.MSG_REC_RUL % (model.skey, model.lang, model.ticket, model.sid);
        base_request = json.loads(model.get_base_request());
        base_request["SyncKey"] = model.sync_key;
        base_request["rr"] = ~int(datetime.now().timestamp());
        data = bytearray(str(base_request).replace("'","\""), 'utf8');
        result = HttpClient().rq(url, data, {"Host":"wx.qq.com"});
        sync_key = ResultCheck().sync_rec_check(result);
        model.sync_key = sync_key;
        result = json.loads(result);
        result = result["AddMsgList"];
        print(result);
        for msg in result :
            from_user_name = msg["FromUserName"];
            content = msg["Content"];
            msg_type = int(msg["MsgType"]);
            localTime = time.localtime(int(msg["CreateTime"]))
            strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime);
            model = Contact().get_member(from_user_name);
            nick_name = model.nick_name;
            if msg_type==51:
                print("["+strTime+"] "+nick_name+" : 普通点击消息");
            else :
                print("[" + strTime + "] " + nick_name + " : " + content);