from operator import length_hint

print(len("12345"))

len("Hello")

print(type("12345"))
print(type(123))
print(type(123.4))
print(type(True))


name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letter in your name: ")) # str
print(type(length_of_name)) # int

print("Number of letter in your name: " + str(length_of_name))

