#!/usr/bin/python
# -*- coding: utf8 -*-
import os
from song_player import song_player
from myconfig import syscmd
from mytools import *
def restart_app():
#kill player controller process
  os.system(syscmd['kill_player_controller'])
#restart player controller process
  os.system(syscmd['start_player_controller'])

if not check_process_running():
  my_log('not running')
  restart_app()

if not in_allow_time():
  my_log('not allow time')
  os.system(create_cmd('["set_property","pause","yes"]'))

if not is_pause():
#check if the play back time changed
  playback_time = now_playback_time()
  my_log(playback_time)
  os.system('sleep 3')
  playback_time_2 = now_playback_time()
  my_log(playback_time_2)
  if playback_time_2 == playback_time :
    restart_app()
    set_play()
