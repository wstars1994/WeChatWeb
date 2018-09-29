from http.HttpClient import HttpClient
from http.WeChatUrl import WeChatUrl
from datetime import datetime

class Message(object) :

    def recv(self,model):
        timestamp = int(datetime.now().timestamp());

        list = model.sync_key["List"];
        sync_key_list = [];
        for key in list :
            sync_key_list.append(str(key["Key"])+"_"+str(key["Val"]));
        sync_key = "|".join(sync_key_list);
        # window.synccheck={retcode:"0",selector:"0"}
        url = WeChatUrl.MSG_SYNC_CHECK_URL % (timestamp*1000,model.skey,model.uin,sync_key,model.sid);
        HttpClient.res_headers.update({"wxpluginkey":timestamp});
        result = HttpClient().rq(url, None, {"Host":"webpush.wx.qq.com"});
        print(url);
        print(result);

        # while(1):
        #     url = WeChatUrl.MSG_REC_RUL % (model.skey,model.lang,model.ticket,model.sid);
        #     # timestamp = int(datetime.now().timestamp());
        #     data = bytearray(model.get_base_request(), 'utf8');
        #     result = HttpClient().rq(url,data,{});
        #     print(result);

            # https://webpush.wx.qq.com/cgi-bin/mmwebwx-bin/synccheck?r = 1538184039507 & skey = % 40
            # crypt_121afffd_050fdd1189123b662937838365ca992a & sid = mNLUc9Ywv2NiZQX3 & uin = 228200615 & deviceid = e160829819295044 & synckey = 1_725111440 % 7
            # C2_725112311 % 7
            # C3_725112195 % 7
            # C11_725112236 % 7
            # C201_1538183867 % 7
            # C203_1538180624 % 7
            # C1000_1538175722 % 7
            # C1001_1538175794 & _ = 1538183174414

