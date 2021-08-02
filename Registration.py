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


n=1
while n<2:
	a=str(input(blue+"Enter Your Passowrd :"+color_off))
	b=str(input(yellow+"Confirm Your Passowrd :"+color_off))
	if a==b:
		print(green+"============================================================              ✔★Your registration Complit★✔")
		n=3
	else:
		print("\t✘☞ PASSOWRD RONG ✘"+color_off)
		n=0