# Andrew Deba
# UWYO COSC 1010
# 11/21/2024
# Lab 10
# Lab Section: 18
# Sources, people worked with, help given to: 

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

#Stored Hash
try:
    stored_hash = get_hash("""You can use """)
except:
    print("PLACEHOLDER")

#Compare Against Passwords
try:
    path = Path('rockyou.txt')
    content = (path.read_text()).splitlines()
    for line in content:
        #print(line)
        hash_integral = get_hash(line)
        print(f"{hash_integral} \n")
        if hash_integral == stored_hash:
            print(f"Success on the line: {line}")
except FileNotFoundError:
    print("IDK")




# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.
