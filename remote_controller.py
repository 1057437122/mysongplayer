#!/usr/bin/python
# -*- coding: utf8 -*-
import os
import urllib2
from myconfig import cnf
#from mytool import mylog
import mytool
import commands
import json
import time
import urllib2
import urllib
import sys
import myencrypt
reload(sys)
sys.setdefaultencoding('utf-8')
remote_url = cnf['remote_http_protocol']+'://'+cnf['mydomain']+':'+str(cnf['command_port'])+'/api/ping?'
#cpu|||memory|||Hdisk usage|||current songs|||current percent|||timestamp|||myserial_code
while True:
	time.sleep(2)
	cpu_usage = mytool.get_cpu_usage()
	mem_usage = mytool.get_mem_usage()
	hd_usage = mytool.get_hd_usage()
	current_song = mytool.get_current_song()
	current_percent = mytool.get_current_percent()
	timestamp = int(time.time())
	key = str(cpu_usage)+cnf['key_split']+str(mem_usage)+cnf['key_split']+str(hd_usage)+cnf['key_split']+str(current_song)+cnf['key_split']+str(current_percent)+cnf['key_split']+str(timestamp)+cnf['key_split']+cnf['player_code']
	mytool.mylog('createdkey:'+key)
	url=urllib.urlencode({'key':myencrypt.myencrypt(key)})
	try:
		#request = urllib2.Request(remote_url,url)
		#response = urllib2.urlopen(request)
		response = urllib2.urlopen(remote_url+url)
		status_code = response.getcode()
		ret = response.read()
		mytool.mylog('ret we get:'+ret)
		res = json.loads(myencrypt.mydecrypt(ret))
		mytool.mylog('res after decrypt:'+str(res))
		if res['type'] == '':
			print 'null'
		elif res['type'] == 'exe_cmd':
			#exe player command 
			#need to be safe
			mytool.send_command(res['cmd'])


	except urllib2.URLError,e:
		mytool.mylog('error:'+str(e.reason))
