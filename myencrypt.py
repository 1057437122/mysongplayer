#!/usr/bin/python
# -*- coding: utf8 -*-
import base64
import string
import random
import mytool
def create_random_letters(size=6,chars=string.ascii_uppercase + string.digits):
#create length random letter
	return ''.join(random.choice(chars) for _ in range(size))
def create_random_size(maxx):
#create size from 2 to maxx
	return random.randint(2,maxx)
def myencrypt(stri):
#1 base64 origin string as base64ed_string
#2 reverse base64ed_string
#3 create $length random letter and $begin_index (2<$begin_index<length_of_base64ed_string-1)
#4 insert $length to base64ed_string at [index 1]
#5 insert $begin_index to base64ed_string at [index 2],of course $begin_index must big than 2
	reversed_base64ed_string = base64.b64encode(stri)[::-1]
	mytool.mylog('bs64ed:'+reversed_base64ed_string)
	size = create_random_size(9)

	random_letters = create_random_letters(size)
	minx = len(reversed_base64ed_string)-1
	if minx > 9:
		minx = 9
	insert_index = random.randint(3,minx)
	encrypted_letter = reversed_base64ed_string[0]+str(insert_index)+str(size)+reversed_base64ed_string[1:insert_index]+random_letters+reversed_base64ed_string[insert_index:]
	return encrypted_letter
def mydecrypt(stri):
	insert_index = int(stri[1])
	size = int(stri[2])
	reversed_base64ed_string = stri[0]+stri[3:insert_index+2]+stri[insert_index+2+size:]
	return base64.b64decode(reversed_base64ed_string[::-1])
