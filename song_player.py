import os
class song_player:
    def __init__(self,playlist):
        self.playlist = playlist
    def play(self,start_song=0):
        play_cmd = 'mpv --no-video --playlist='+self.playlist+' --playlist-start='+str(start_song)+' --save-position-on-quit --loop &'
        os.system(play_cmd)
    def stop(self):
        stop_cmd='kill -9 `ps aux |grep mpv |grep -v "grep"|awk \'{print $2}\'`'
        os.system(stop_cmd)
