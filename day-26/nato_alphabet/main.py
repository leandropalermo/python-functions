import pandas

data_df = pandas.read_csv("nato_phonetic_alphabet.csv")


def generate_phonetic():
    name = input("type your name\n")

    words_dict = {row.letter: row.code for (index, row) in data_df.iterrows()}
    try:
        name_coded = [words_dict[letter.upper()] for letter in name]
    except KeyError as error_message:
        print(error_message)
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(name_coded)


generate_phonetic()

