class LoginParamModel :

    def __init__(self,ticket,lang,uuid,skey,sid,uin):
        self.ticket = ticket;
        self.lang = lang;
        self.uuid = uuid;
        self.skey = skey;
        self.sid = sid;
        self.uin = uin;

    def get_base_request(self):
        return '{"BaseRequest":{"DeviceID":"e151448812791695","Sid":"'+self.sid+'","Skey":"'+self.skey+'","Uin":'+self.uin+'},"rr":-527743829,"SyncKey":{"Count":4,"List":[{"Key":1,"Val":725111440},{"Key":2,"Val":725111934},{"Key":3,"Val":725111832},{"Key":1000,"Val":1538120642}]}}';

