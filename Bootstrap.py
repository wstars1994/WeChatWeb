from Login import Login

qr_uuid=Login().get_qrcode();
Login().login(qr_uuid);

