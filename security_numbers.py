import uuid
import hashlib
import random
import sqlite3

num_list = []
hashes = []

def number_gen():
    num = random.randint(100000, 999999)
    num_list.append(str(num))

for i in range(20):
    number_gen()
 
def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


for j in num_list:
	print(j)
	hashed_password = hash_password(j)
	hashes.append(hashed_password)


def database_con():
	conn = sqlite3.connect('reset.db')
	c = conn.cursor()
	for k in hashes:
		c.execute("INSERT INTO recovery_codes (code) VALUES (?)", (k,))
		conn.commit()
	conn.close()

database_con()