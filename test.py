user_input = int(raw_input("please input a number : "))
if user_input > 0:
	print str(user_input) + " > 0"
elif user_input == 0:
	print str(user_input) + " = 0"
elif user_input < 0:
	print str(user_input) + " < 0"
else:
	print "eorr"