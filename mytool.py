#!/usr/bin/python
# -*- coding: utf8 -*-
import base64
import paramiko
import time
import sys
import commands
import json
from myconfig import cnf

def mylog(log_str,log_file='my_log_file.log',print_out=False):
	with open(log_file,'a+') as fp:
		fp.write(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
		fp.write(':'+str(log_str))
		#fp.write(':'+str(log_str).decode('utf-8'))
		if(print_out):
			print(str(log_str))
		fp.write('\n')

def get_cpu_usage():
	return 20
def get_mem_usage():
	return 20
def get_hd_usage():
	return 20
def get_current_percent():
	return 20

def get_current_song():
	command='''"get_property","filename"'''
	return send_command(command)
def send_command(command,command_serial_num = 0,with_ret = False):
#send command to mpv ipc server and get return 
#@param with_ret need send to callback function on remote server , default false.
#echo '{ "command":["$command","$param1",...] }' |socat - $mpvsocket
	command_string_format='echo \'{ "command":['+command+'] }\' |socat - '+cnf['mpvsocket']
	try:
		res = json.loads(commands.getoutput(command_string_format))
		if res['error'] == u'success':
			#
			mylog('execmd success')
			if 'data' in res.keys():
				return res['data']
		else:
			mylog('exe cmd error:'+res['error'])
	except OSError:
		mylog('exe command failed')
