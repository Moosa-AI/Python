from subprocess import CREATE_NEW_CONSOLE


a=int(input("Enter your age: "))
# a=17
print("Your age is:", a)

# Conditional operators
# >, <=, <, >=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
if(18<a<90):
	print("you are eligible")
	print("yes")
else:
	print("Ineligible")
	print("no")

