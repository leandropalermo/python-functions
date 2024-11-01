file = open("test_file.txt")
print(file.read())
file.close()

# To do not have the necessity of use file.close function, could do it like this:
with open("test_file.txt") as file:
    print(file.read())

#To write content on file, is necessery to inform the mode type:
with open("test_file.txt", mode="w") as file:
    file.write("I am overwriting the file content.")

#Mode type: w = overwrite, r = read, a = append
with open("test_file.txt", mode="a") as file:
    file.write("I am appending new content on file")

with open("test_file.txt") as file:
    print(file.read())

