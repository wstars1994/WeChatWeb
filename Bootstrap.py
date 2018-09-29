from Login import Login
from Message import Message
from Contact import Contact
login = Login();

qr_uuid = login.get_qrcode();
loginParamModel = login.login(qr_uuid);

if loginParamModel is not None:
    Contact().req_members(loginParamModel);
    Message().recv(loginParamModel);
