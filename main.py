import random
password_symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_len = int(input("Enter password len: "))
generated_password = ""
for _ in range(password_len):
    generated_password += random.choice(password_symbols)
print("Generated password: ", generated_password)
