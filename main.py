import random

print("we have 3 kategory animals,countries,colors")
print("choose a category")
print("1: animals!")
print("2: countries!")
print("3: colors")
choice=input("choose 1,2 or 3  ")


mapping={
    "1": "animals.txt",
    "2": "countries.txt",
    "3": "colors.txt"
}

file_name=mapping.get(choice)
        
if not file_name:
    print("please try agen") 
    exit()


with open(file_name, "r") as file:
    word_list = file.read().splitlines()
    
word_guess = random.choice(word_list).casefold()
word_len=len(word_guess)
new=int(word_len)*["*"]
print("".join(new))

def play_game():
    while True:
        my_letter=input("write letter->").casefold()
        if my_letter in word_guess:
            indexes = [i for i,x in enumerate(word_guess) if my_letter == x]
            for i in indexes:
                new[i] = my_letter
            if "".join(new)==word_guess:
                print("".join(new))
                break
        else:
            print("wrong letter let's try again")
        print("".join(new))
play_game()


