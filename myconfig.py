config = {
  #'default_music_path':'/home/pi/backgroundmusic',
  'default_music_path':'/Users/Sunday/Downloads/church/backgroundmusic',
  'default_socket_file':'/tmp/mpvsocket',
}
syscmd = {
  'get_player_controller_process_count':'ps aux |grep python|grep player|grep -v grep |wc -l',
  'get_mpv_process_count':'ps aux |grep mpv|grep -v grep |grep -v python|wc -l',
  'kill_player_controller':'kill -9 `ps aux |grep python|grep player|grep -v grep |awk \'{print $2\'}`',
  'kill_mpv':'kill -9 `ps aux |grep mpv |grep -v python |grep -v grep |awk \'{print $2\'}`',
  'start_player_controller':'python /opt/mysong/mysong_player.py',


}
