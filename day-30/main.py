try:
    file = open("something.txt")
    a_dictionary = {"key": "value"}
    a_dictionary.get("new_key")
except FileNotFoundError:
    print("File does not exist.")
    with open("something.txt", mode="w") as file:
        print("The file has been created.")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print("It is passing here only if no exception thrown.")

    raise KeyError("Throwing this error just for example purpose.")
finally:
    file.close()
    print("It is always passing here.")


height = int(182)
weight = int(74)

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / (height ** 2)
print(bmi)