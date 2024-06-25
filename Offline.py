import os, platform, time, sys
print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mChecking For Update...')
os.system('git pull --quiet 2>/dev/null')
os.system('xdg-open https://chat.whatsapp.com/KThLuumIszgD0UCJz3T33C')
mrMani = platform.architecture()[0]
if mrMani== '64bit':
 os.system('xdg-open https://github.com/Villan11223344/hum> OFFLINE64")

 print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Device is 64bit');time.sleep(2)
 os.system('chmod 777 OFFLINE64 && ./OFFLINE64')
elif mrMani== '32bit':
 print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Devive is Not Supported');time.sleep(2);exit()
 
