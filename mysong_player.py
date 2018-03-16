#!/usr/bin/python
#import argparse
from signal import pause
from gpiozero import Button,LED
from song_player import song_player
from myconfig  import config

#parser = argparse.ArgumentParser()
#parser.add_argument('--path',default='default',help='default_path')
#parser.add_argument('--socket_file',default='default',help='default_socket_file')
#args = parser.parse_args()
#playlist = args.playlist
#path = args.path
#socket_file = args.socket_file
button = Button(2)
song=song_player()
button.when_pressed = song.music_play
button.when_released = song.music_pause

pause()
