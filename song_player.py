import os
from myconfig import config,syscmd
from mytools import *
class song_player:
    def __init__(self,path='',socket_file=''):
        self.path = path
        self.socket_file = socket_file
        self.set_default_param()
        self.start_cmd = 'mpv --no-video '+self.path+' --loop --input-ipc-server='+self.socket_file+' &'
        self.play_cmd = create_cmd('["set_property","pause","no"]',self.socket_file)
        self.pause_cmd = create_cmd('["set_property","pause","yes"]',self.socket_file)
        self.stop()
        self.start()
    def set_default_param(self):
        if self.path == '':
            self.path = config['default_music_path']
        if self.socket_file == '':
            self.socket_file = config['default_socket_file']
    def start(self):
        os.system(self.start_cmd)
        os.system('sleep 3')
        os.system(self.pause_cmd)
    def music_play(self):
        os.system(self.play_cmd)
    def music_pause(self):
        os.system(self.pause_cmd)
    def stop(self):
        os.system(syscmd['kill_mpv'])
