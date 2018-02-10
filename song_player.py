import os
class song_player:
    def __init__(self,path,socket_file):
        self.path = path
        self.socket_file = socket_file
        self.start_cmd = 'mpv --no-video '+self.path+' --loop --input-ipc-server='+self.socket_file+' &'
        self.play_cmd = 'echo \'{ "command": ["set_property", "pause", "no"] }\' |socat - '+self.socket_file
        self.pause_cmd = 'echo \'{ "command": ["set_property", "pause", "yes"] }\' |socat - '+self.socket_file
        self.start()
    def start(self):
        os.system(self.start_cmd)
        os.system('sleep 3')
        os.system(self.pause_cmd)
    def music_play(self):
        os.system(self.play_cmd)
    def music_pause(self):
        os.system(self.pause_cmd)
    def playlist(self,playlist,start_song=0):
        play_cmd = 'mpv --no-video --playlist='+playlist+' --playlist-start='+str(start_song)+' --save-position-on-quit --loop &'
        os.system(play_cmd)
    def play_path(self):
        play_cmd = 'mpv --no-video '+self.path+' --loop &'
        os.system(play_cmd)
    def stop(self):
        stop_cmd='kill -9 `ps aux |grep mpv |grep -v "grep"|awk \'{print $2}\'`'
        os.system(stop_cmd)
