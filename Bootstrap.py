from Login import Login
from Message import Message
login = Login();

qr_uuid = login.get_qrcode();
loginParamModel = login.login(qr_uuid);

if loginParamModel is None:
    Message().recv(loginParamModel);
