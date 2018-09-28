from Login import Login
from Message import Message
login = Login();

loginParamModel = login.login(login.get_qrcode());

if loginParamModel != None:
    Message().recv(loginParamModel);


