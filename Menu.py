#!/usr/bin/python

import os
import sys

os.system("clear && clear && clear")

menu = '''\033[0m
  	 {1}--Home					~~ Home directory
   	 {2}--Desktop					~~ Desktop directory
   	 {3}--Downloads					~~ Download directory
  	 {4}--Crips					~~ Launch Crips
   	 {5}--HiddenEye 				~~ Launch HiddenEye
   	 {6}--Install & Update				~~ Install & Update
       	 {7}--Comming soon				~~
       	 {8}--Comming soon				~~
       	 {9}--Comming soon				~~
    	 {0}--Comming soon				~~
   	 {99--Exit                                                                                                                  
 '''

logo = '''\033[0m 
      =======================================================================

	.88b  d88. d88888b d8b   db db    db  	db     .d88b.      .d88b.  
	88'YbdP`88 88'     888o  88 88    88 	o88    .8P  88.    .8P  88. 
	88  88  88 88ooooo 88V8o 88 88    88 	 88    88  d'88    88  d'88 
	88  88  88 88~~~~~ 88 V8o88 88    88 	 88    88 d' 88    88 d' 88 
	88  88  88 88.     88  V888 88b  d88 	 88 db `88  d8' db `88  d8' 
	YP  YP  YP Y88888P VP   V8P ~Y8888P' 	 VP VP  `Y88P'  VP  `Y88P'  

      =============================== By Gnusse =============================                                   
                                                            
'''

print logo
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

    elif choice == 8:
	print("8")
	quit()


    elif choice == 9:
	print("9")
	quit()


    elif choice == 0:
	print("0")
	quit()

  except(KeyboardInterrupt):
    print ""
select()
