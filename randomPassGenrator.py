import random
import string

pass_len = 6
char_val = (string.ascii_letters + string.digits  )  # +string.punctuation

#try second method :- list cmprehension

val = "".join([random.choice(char_val) for i in range(pass_len) ])
print("your password suggesion is :",val)


#normal method :

#password = " "
#for i in range(pass_len):
#    password += random.choice(char_val)

#print("your password suggesion is :",password)
