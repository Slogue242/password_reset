import uuid
import hashlib
import random
import sqlite3

hashes = []

conn = sqlite3.connect('reset.db')
c = conn.cursor()

c.execute("SELECT code FROM recovery_codes")

last_entry = c.fetchall()
for i in last_entry:
	for k in i:
		hashes.append(k)

conn.close()

random_code = random.randint(0, len(hashes))

def check_password(hashed_password, user_password):
	password, salt = hashed_password.split(':')
	return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

old_pass = input(f'Please enter code {random_code}: ')
if check_password(hashes[random_code], old_pass):
    print('You entered the right password')
else:
    print('I am sorry but the password does not match')

#https://www.pythoncentral.io/hashing-strings-with-python/