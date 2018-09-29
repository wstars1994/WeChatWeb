from httpreq.HttpClient import HttpClient
from httpreq.HttpWXUrl import WeChatUrl
from datetime import datetime
from ContactModel import ContactModel

import json

class Contact() :

    __members = [];

    def req_members(self,model):
        timestamp = int(datetime.now().timestamp());
        result = HttpClient().rq(WeChatUrl.MEMBERS_URL % (model.ticket,timestamp,model.skey),None,{});
        result = json.loads(result);
        member_list = result["MemberList"];
        for member in member_list:
            id = member["UserName"];
            nick_name = member["NickName"];
            signature = member["Signature"];
            icon = member["HeadImgUrl"];
            sex = member["Sex"];
            self.__add_member(ContactModel(id,nick_name,signature,icon,sex));
        print(self.__members);

    def __get_members(self):
        return self.__members;

    def __add_member(self,contact_model):
        self.__members.append(contact_model);

    def get_member(self,id):
        for model in self.__members :
            if model.id == id:
                return model;