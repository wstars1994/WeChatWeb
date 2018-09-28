class LoginParamModel :

    def __init__(self,ticket,lang,uuid,skey,sid,uin):
        self.ticket = ticket;
        self.lang = lang;
        self.uuid = uuid;
        self.skey = skey;
        self.sid = sid;
        self.uin = uin;

    def get_base_request(self):
        return '{"BaseRequest":{"DeviceID":"e063244812538015","Sid":"'+self.sid+'","Skey":"'+self.skey+'","Uin":'+self.uin+'}}';

