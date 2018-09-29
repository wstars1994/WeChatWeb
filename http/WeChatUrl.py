class WeChatUrl():

    QRCODE_UUID_URL = "https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage&fun=new&lang=zh_CN&_=%d";

    QRCODE_IMG_URL="https://login.weixin.qq.com/qrcode/%s";

    LOGIN_FIRST_URL="https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid=%s&tip=1&r=%s&_=%s";

    LOGIN_KEY_URL="https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?ticket=%s&uuid=%s&lang=%s&scan=%d&fun=new&version=v2";

    LOGIN_FINAL_URL = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=%d&lang=%s&pass_ticket=%s";

    MSG_REC_RUL = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsync?skey=%s&lang=%s&pass_ticket=%s&sid=%s";

    MSG_CONTACT_LIST = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=%s&r=%d&seq=0&skey=%s";

    MSG_SYNC_CHECK_URL = "https://webpush.wx.qq.com/cgi-bin/mmwebwx-bin/synccheck?r=%d&skey=%s&uin=%s&deviceid=e153426668358344&synckey=%s&sid=%s";