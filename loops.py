# letters = ["a", "b", "c", "d", "e", "f"]

# for i in letters:
#     print(i)

# print(list(range(6)))
# for i in range(6):
#     print(i, letters[i])


# for i in "banana":
#     print(i)
#     print("---")

# while True:
#     print("I am running..!")
#     print(".......!")

word = "proliferate"
index = 0

# while True:

#     print(word[index])
#     index += 1

#     if index == len(word):
#         break

# word = "emancipation"

# for letter in word:

#     if letter == "p":
#         print("Yaayy!!!. Found letter (p)\n")
#         break
#     else:
#         print("Searching for p", "found", letter)

# else:
#     print("Sorry P was not found in", word)

sentence = "In this example, <iterable> is the list a, and <var> is the variable i. Each time through the loop, i takes on a successive item in a, so print() displays the values 'foo', 'bar', and 'baz', respectively. A for loop like this is the Pythonic way to process the items in an iterable."

word_list = sentence.split(" ")
place_holder = "" 

# for word in word_list:

#     if len(word ) > len(place_holder):
#         place_holder = word

# print(place_holder)

# index = 0

# while True:

#     if len(word_list[index]) > len(place_holder):
#         place_holder = word_list[index]  
    
#     index +=1

#     if index == len(word_list):
#         break


# print(place_holder)

# number = 0
# stop_value = 200

# while True:

#     print(number)
#     number += 1

#     if number == stop_value:
#         break

# WITH A STEP VALUE 

# step_value = 2
# number = 0
# stop_value = 200

# while True:

#     print(number)
#     number += step_value

#     if number >= stop_value + 1:
#         break

# for i in range(1,200,1):
#     print(i)

# COUNT DOWNTIMER

import time
import winsound

number_of_seconds = int(input("Enter time in seconds : "))

for i in reversed(range(number_of_seconds)):
    print(i)
    time.sleep(1)

winsound.Beep(500, 1000)
