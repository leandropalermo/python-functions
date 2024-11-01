BIRTHDAY_LETTER = """
Dear [name],

You are invited to my birthday this Saturday.

Hope you can make it!

Leandro
"""
LETTER_DEFAULT_NAME = f"letter_for_[name].txt"
letters_name = []
letters = []
with open("name.txt") as file:
    names = file.readlines()
    for name in names:
        letter_name = LETTER_DEFAULT_NAME.replace("[name]", name.strip())
        letter = BIRTHDAY_LETTER.replace("[name]", name.strip())
        with open(letter_name, mode="w") as f:
            f.write(letter)

