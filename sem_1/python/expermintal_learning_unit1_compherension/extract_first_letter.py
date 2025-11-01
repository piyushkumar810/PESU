# Create a set of first letters of each word in a given paragraph.

user=input("enter the paragraph ").strip()
# print(user)

spliting_each_word=user.split()
print(spliting_each_word)

extract_first_letter_from_each_word=[letter[0].lower() for letter in spliting_each_word if letter.isalpha()]
print(extract_first_letter_from_each_word)