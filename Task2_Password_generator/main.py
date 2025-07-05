import random
import string

# Greet the user
print("🔐 Welcome to the Password Generator!")

length = int(input("How long should the password be? Enter a number: "))

letters = string.ascii_letters     # Includes both lowercase and uppercase letters
digits = string.digits             # Numbers from 0 to 9
symbols = string.punctuation       # Special characters like !, @, #, etc.

# Combine everything into one big set of characters
all_characters = letters + digits + symbols

# Now randomly pick characters one by one to create the password
password = ''.join(random.choice(all_characters) for _ in range(length))

print(f"\n🔑 Your new password is:\n{password}")
