from HttpClient import HttpClient
from datetime import datetime
from WeChatUrl import WeChatUrl
from WeChatResultCheck import WeChatResultCheck
from urllib import parse
import xml.etree.ElementTree

class Login():

    def get_qrcode(self,path="D:/1.jpg"):
        timestamp = int(datetime.now().timestamp());
        uuid_url = WeChatUrl.QRCODE_UUID_URL % (timestamp);
        result = HttpClient.rq(uuid_url, None, {});
        uuid_msg=WeChatResultCheck().uuid_check(result);
        if uuid_msg[0]==0:
            qr_url = WeChatUrl.QRCODE_IMG_URL % uuid_msg[1];
            HttpClient.download(qr_url,path);
            print("[SUCCESS] 二维码获取成功,路径:" + path);
            print("[SUCCESS] 请打开微信扫描二维码");
            return uuid_msg[1]
        else:
            print(uuid_msg[1])

    def login(self,qr_uuid):
        while(1):
            timestamp = int(datetime.now().timestamp());
            first_login_url = WeChatUrl.LOGIN_FIRST_URL % (qr_uuid,~timestamp,timestamp);
            result = HttpClient.rq(first_login_url, None, {"Connection": "keep-alive", "Keep-Alive": "timeout=10, max=2"});
            codeList = WeChatResultCheck().first_login_check(result);
            code=int(codeList[0]);
            if code==201 :
                print("[SUCCESS] 扫码成功,确认后登陆");
            if code==200 :
                final_login_url = codeList[1];
                Login().__final_login(final_login_url);
                break;
            if code == 408:
                print("[SUCCESS] 请打开微信扫描二维码");

    def __final_login(self,final_login_url):
        login_key_params = Login().__get_login_key(final_login_url);
        ticket = login_key_params[0];
        lang = login_key_params[1];
        scan = login_key_params[2];
        uuid = login_key_params[3];
        login_key_url = WeChatUrl.LOGIN_KEY_URL % (ticket,uuid,lang,int(scan));
        login_key_result_xml = HttpClient.rq(login_key_url, None, {});
        content = xml.etree.ElementTree.fromstring(login_key_result_xml)
        name = content.findall('error');
        skey = content.findtext('skey');
        wxsid = content.findtext('wxsid');
        wxuin = content.findtext('wxuin');
        pass_ticket = content.findtext('pass_ticket')  # 找到下一层的Name节点
        #获取最终登录URL
        timestamp = int(datetime.now().timestamp());
        final_login_url = WeChatUrl.LOGIN_FINAL_URL % (int(~timestamp),lang,pass_ticket);
        data='{"BaseRequest":{"DeviceID":"e063244812538015","Sid":"'+wxsid+'","Skey":"'+skey+'","Uin":'+wxuin+'}}';
        result = HttpClient.rq(final_login_url,bytearray(data, 'utf8'),{"Content-Type":"application/json;charset=utf-8"});
        print(result);

    def __get_login_key(self,final_login_url):
        query = parse.urlparse(final_login_url).query;
        query_dict = parse.parse_qs(query);
        ticket = query_dict['ticket'][0];
        lang = query_dict['lang'][0];
        scan = query_dict['scan'][0];
        uuid = query_dict['uuid'][0];
        return [ticket,lang,scan,uuid];