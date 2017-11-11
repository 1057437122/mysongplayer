#!/usr/bin/python
# -*- coding: utf8 -*-
import os
from myconfig import cnf
#get if mpv player is started or start it if not
socket_file_ifexists = os.path.isfile(cnf['mpvsocket'])
if socket_file_ifexists:
	process_exists_cmd = 'ps -ef |grep mpv |grep -v grep '
	process_exit_code = os.system(process_exists_cmd)
	if process_exit_code == 0:
	else:
		player_play_cmd = 'mpv --loop --no-video --input-ipc-server=/tmp/mpvsocket '+cnf['songs_path']+' >/dev/null 2>&1 &'
		os.system(player_play_cmd)
