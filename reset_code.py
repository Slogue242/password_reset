import random
import datetime
import sqlite3


def gen_code():
	#Connecting to the reset database.
	#This will hold the information for the reset code and the time.
	conn = sqlite3.connect('reset.db')
	c = conn.cursor()

	#Generates a random 6 digit code to be emailed to the user for resetting password
	reset_code = random.randint(100000, 999999)

	#Gets the current time and adds 30 minutes to this time.
	#If the password is not reset in 30 minutes a new code will need to be emailed
	now = datetime.datetime.now()
	now_plus_now = now + datetime.timedelta(minutes=30)

	c.execute("INSERT INTO password_reset VALUES (?, ?)", (reset_code, now_plus_now))
	conn.commit()

	conn.close()

if __name__ == '__main__':
	gen_code()