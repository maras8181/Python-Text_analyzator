TEXTS = [
'''Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
registerred_users = {"bob" : 123, "ann" : "pass123", "mike" : "password123", "liz" : "pass123"}
separator = "=" * 40
while True:
    username = input("Enter your username: ")
    if not username:
        print(f"Empty input. Try again...")
    else:
        break
while True:
    password = input("Enter your password: ")
    if not password:
        print(f"Empty input. Try again...")
    else:
        break
print(separator)
if password == str(registerred_users.get(username)):
    print(f"Welcome to the application, {username.title()}")
else:
    print(f"You are not registerred, {username.title()}. Ending app...")
    exit()
print(f"We have {len(TEXTS)} texts to be analyzed.")
print(separator)
choosen_text = 0
while True:
    choice = input("Enter a number btw. 1 and 3 to select: ")
    if not choice:
        print(f"Empty input. Try again...")
    else:
        break
if choice.isnumeric():
    choice = int(choice)
    if choice < 1 or choice > 3:
        print(f"{choice} is not btw numbers 1-3. Ending app...")
        exit()
    else:
        choosen_text = TEXTS[choice - 1]
elif '-' in choice:
    choice = choice.replace('-','')
    if choice.isnumeric():
        choice = int(choice)
        choice *= -1
        print(f"{choice} is a negative number. Ending app...")
        exit()
else:
    print(f"{choice} is not a number. Ending app...")
    exit()
splited_text = choosen_text.split()
splited_text_clear = [word.strip(',.?!') for word in splited_text]
numbers_of_length = [len(word) for word in splited_text_clear]
title_case = [word for word in splited_text_clear if word.istitle() and word.isalpha()]
upper_case = [word for word in splited_text_clear if word.isupper() and word.isalpha()]
lower_case = [word for word in splited_text_clear if word.islower() and word.isalpha()]
numeric = [word for word in splited_text_clear if word.isnumeric()]
numeric_int = [int(number) for number in numeric]
print(separator)
print(f"There are {len(splited_text)} words in the selected text.")
print(f"There are {len(title_case)} titlecase words.")
print(f"There are {len(upper_case)} uppercase words.")
print(f"There are {len(lower_case)} lowercase words.")
print(f"There are {len(numeric)} numeric strings.")
print(f"The sum of all the numbers {sum(numeric_int)}.")
print(separator)
print(f"LEN | OCCURENCES | NR.")
star = '*'
space = ' '
set_of_numbers = set(numbers_of_length)
frequency_numbers = []
for cislo in set_of_numbers:
    frequency_numbers.append(numbers_of_length.count(cislo))
highest_number = max(frequency_numbers)
for num in set_of_numbers:
    count_of_spaces = highest_number - numbers_of_length.count(num)
    print(f"{num} | {star * numbers_of_length.count(num)} {space * count_of_spaces} | {numbers_of_length.count(num)}")