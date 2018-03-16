#run each minute
#check whether mpv&python process running :if any not run then restart python process 
#check time: if now is later than 10 pm it will auto pause
#check running: if get pause status is FALSE but get playback_time not increase then reboot 
#
import os
from datetime import datetime
#from song_player import song_player
from myconfig import config,syscmd
import json
import time

def check_process_running():
  player_controller = os.popen(syscmd['get_player_controller_process_count']).read().strip()
  mpv_process = os.popen(syscmd['get_mpv_process_count']).read().strip()
  if ( player_controller == '0' or mpv_process == '0' ):#either of them is not running
    return False
  return True

def in_allow_time():
  now_sign = int(datetime.now().strftime('%H'))
  if now_sign <= 20 and now_sign >= 6:
    return True
  else:
    return False

def get_socket_data(cmd):
  ret = json.loads(os.popen(cmd).read().strip())
  if ret['error'] == 'success':
    return ret['data']
  else:
    return False

def create_cmd(args,socket_file=config['default_socket_file']):
#args: string of command like  ["get_property","filename"]
  return 'echo \'{ "command":' + args + ' }\' |socat - ' + socket_file

def is_pause():
  return get_socket_data(create_cmd('["get_property","pause"]'))

def now_playback_time():
  return get_socket_data(create_cmd('["get_property","playback-time"]'))

def set_play():
  os.system(create_cmd('["set_property","pause","no"]'))
def set_pause():
  os.system(create_cmd('["set_property","pause","yes"]'))

def my_log(log_str,log_file='my_log_file.log',print_out=False):
  with open(log_file,'a+') as fp:
    fp.write(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
    fp.write(':'+str(log_str))
    if(print_out):
      print(str(log_str))
    fp.write('\n')
