#!/usr/bin/python

import os
import sys

os.system("clear && clear && clear")

menu = '''\033[0m
    {1}--Home
    {2}--Desktop
    {3}--Downloads
    {4}--Crips
    {5}--HiddenEye 
    {6}--Install & Update
    {7}--Comming soon
    {0}--Comming soon
    {99}-Exit                                                                                                                   
 '''

print menu

def quit():
            con = raw_input('Continue [Y/n] -> ')
            if con[0].upper() == 'N':
		print(os.getcwd())
		os.chdir("/root")
		print(os.getcwd())
                
            else:
                os.system("clear")
                print menu
                select()
           

def  select():
  try:
    choice = input("Menu~# ")
    if choice == 1:
	print("1")
	quit()

    elif choice == 2:
	print("2")
	quit()

    elif choice == 3:
	print("3")
	quit()
 
    elif choice == 0:
	print("0")
	quit()

    elif choice == 4:
	print("4")
	quit()

    elif choice == 5:
	print("5")
	quit()

    elif choice == 6:
	  os.system("clear")
	  print("This tool is only available for Linux and similar systems  ")
	  os.system("git clone https://github.com/GnussonNet/MyMenu.git")
	  os.system("cd MyMenu && sudo bash ./update.sh")
	  os.system("menu")

    elif choice == 7:
	print("7")
	quit()

  except(KeyboardInterrupt):
    print ""
select()
