#Evey Kriter/CSCI0101/11.7.2019/Lab 8

import random

def read_filename(filename):
    ''' opens a text file, reads and prints each line one by one, returns a dictionary'''
    file = open(filename, encoding='utf-8') #Open the file called filename
    capitals = {} #make the dictionary
    for line in file: #Read each line in the file one at a time
        line = line.strip("\n")
        line = line.split("," , -1)
        capitals[line[0]] = line[1]
    return capitals
        
#read_filename('state_capitals.csv')

def game(filename):
    '''The function takes as argument a string with a file name and returns nothing'''
    capitals = read_filename(filename)
    random_states = random.sample(capitals.keys(), len(capitals.keys()))
    correct = 0
    total = 0
    for keys in random_states:
        print('What is the capital of ' + keys + "?")
        answer = input()
        answer = answer.capitalize() #makes sure answer is correct even without capitalization
        if answer == capitals[keys]:
            print("Congrats you are correct!")
            correct = correct + 1
            total = total + 1
        elif answer == "Exit":
            break
        else:
            print("Sorry, the correct answer is " + capitals[keys] + ".")
            total = total + 1
    print("Your score was " + str(correct) + "/" + str(total) + " which is " + str(correct/total*100) + "%")

game('state_capitals.csv')