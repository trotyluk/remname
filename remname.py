#!/usr/bin/python3
import os
import sys
il_arg = len(sys.argv)
list_arg = str(sys.argv)
if(il_arg>3):
  print('To many arguments')
  exit()
if(il_arg == 3):
  rem_text = sys.argv[1]
  put_text = sys.argv[2]
  print('change {} to {}'.format(rem_text, put_text))
if(il_arg == 2):
  rem_text = sys.argv[1]
  print(rem_text)
  put_text = ''
if(il_arg == 1):
  in_text = input('Input text to remove or enter to exit ')
  if in_text=='':
    exit()
  rem_text = in_text
  put_text = input('Input text to change for ')
  print(rem_text)
basedir = './'
for fn in os.listdir(basedir):
  sciezka = os.path.join(basedir, fn) 
  newname = sciezka.replace(rem_text, put_text)
  if(newname != sciezka):
    os.rename(sciezka, newname)
    print('changed '+ newname)
