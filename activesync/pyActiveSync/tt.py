import sys, time

from utils.as_code_pages import as_code_pages
from utils.wbxml import wbxml_parser
from utils.wapxml import wapxmltree, wapxmlnode
from client.storage import storage

from client.FolderSync import FolderSync
from client.Sync import Sync
from client.GetItemEstimate import GetItemEstimate
from client.ResolveRecipients import ResolveRecipients
from client.FolderCreate import FolderCreate
from client.FolderUpdate import FolderUpdate
from client.FolderDelete import FolderDelete
from client.Ping import Ping
from client.MoveItems import MoveItems
from client.Provision import Provision
from client.ItemOperations import ItemOperations
from client.ValidateCert import ValidateCert
from client.SendMail import SendMail
from client.SmartForward import SmartForward
from client.SmartReply import SmartReply
from objects.MSASHTTP import ASHTTPConnector
from objects.MSASCMD import FolderHierarchy, as_status
from objects.MSASAIRS import airsync_FilterType, airsync_Conflict, airsync_MIMETruncation, airsync_MIMESupport, airsync_Class, airsyncbase_Type
#from proto_creds import * #create a file proto_creds.py with vars: as_server, as_user, as_pass

pyver = sys.version_info

as_user = 'huyahui@atyun.net'
as_pass = '&WViTJFIpD8$mY3a'
as_server = 'ex.exmail.qq.com'
as_reciever = 'tirsottttt@outlook.com'

storage.create_db_if_none()
conn, curs = storage.get_conn_curs()
device_info = {"Model":"%d.%d.%d" % (pyver[0], pyver[1], pyver[2]), "IMEI":"123456", "FriendlyName":"My pyAS Client", "OS":"Python", "OSLanguage":"en-us", "PhoneNumber": "NA", "MobileOperator":"NA", "UserAgent": "pyAS"}

cp, cp_sh = as_code_pages.build_as_code_pages()
parser = wbxml_parser(cp, cp_sh)


as_conn = ASHTTPConnector(as_server)
as_conn.set_credential(as_user, as_pass)
print(as_conn.credential)

import email.mime.text
email_mid = storage.get_new_mid()
my_email = email.mime.text.MIMEText("Test email #%s from pyAS." % email_mid)
my_email["Subject"] = "Test #%s from pyAS!" % email_mid
my_email["From"] = as_user
my_email["To"] = as_reciever
print type(my_email)
# sendmail_xmldoc_req = SendMail.build(email_mid, my_email)
# print "\r\nRequest:"
# print sendmail_xmldoc_req
# res = as_conn.post("SendMail", parser.encode(sendmail_xmldoc_req))
# print "\r\nResponse:"
#
# if res == '':
#    print "\r\nTest message sent successfully!"
# else:
#    sendmail_xmldoc_res = parser.decode(res)
#    print sendmail_xmldoc_res
#    sendmail_res = SendMail.parse(sendmail_xmldoc_res)

# update folder
# def as_request(cmd, wapxml_req):
#     print "\r\n%s Request:" % cmd
#     print wapxml_req
#     res = as_conn.post(cmd, parser.encode(wapxml_req))
#     wapxml_res = parser.decode(res)
#     print "\r\n%s Response:" % cmd
#     print wapxml_res
#     return wapxml_res
#
#
# parent_folder = storage.get_folderhierarchy_folder_by_name("Inbox", curs)
# new_folder = FolderHierarchy.Folder(parent_folder[0], "TestFolder1", str(FolderHierarchy.FolderCreate.Type.Mail))
# foldercreate_xmldoc_req = FolderCreate.build(storage.get_synckey("0"), new_folder.ParentId, new_folder.DisplayName, new_folder.Type)
# foldercreate_xmldoc_res = as_request("FolderCreate", foldercreate_xmldoc_req)
# foldercreate_res_parsed = FolderCreate.parse(foldercreate_xmldoc_res)
# if foldercreate_res_parsed[0] == "1":
#     new_folder.ServerId = foldercreate_res_parsed[2]
#     storage.insert_folderhierarchy_change(new_folder, curs)
#     storage.update_synckey(foldercreate_res_parsed[1], "0", curs)
#     conn.commit()
# else:
#     print as_status("FolderCreate", foldercreate_res_parsed[0])
