import random

lower_case="abcdefghijklmnopqrstuvwxyz"
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="!/?<>*&^%$#@_()"

alltogether=lower_case + upper_case + numbers + symbols
length=int(input("Enter length for password: "))

pass_code=''.join(random.sample(alltogether,length))
print("Here is your generated password:",pass_code)