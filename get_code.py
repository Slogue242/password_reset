import random
import datetime
import sqlite3



def recover_code():
	#Connecting to the reset database.
	#This will hold the information for the reset code and the time.
	conn = sqlite3.connect('reset.db')
	c = conn.cursor()

	c.execute("SELECT * FROM password_reset ORDER BY expire_date DESC LIMIT 1")

	last_entry = c.fetchone()

	conn.close()

	expire_time = last_entry[1]
	recovery_code = last_entry[0]
	datetime_object = datetime.datetime.strptime(expire_time, '%Y-%m-%d %H:%M:%S.%f')
	
	return recovery_code


if __name__ == '__main__':
	recover_code()



"""
right_now = datetime.datetime.now()

if right_now <= datetime_object:
	print("Still able to reset password")
else:
	print("Time expired. You will need to send a new code")
"""