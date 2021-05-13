
def profanity_checker(input):
    file = open(input, "r")
    checker = open ('checker.txt', "r")
    to_check = file.read()
    print("File: " + to_check + '\n')
    for x in checker:      
        word = x.split(':')
        if (word[0] in to_check):
            print("Word found: " + word[0])
            print("Description: " + word[1])
            print("Occurence: " + str(to_check.count(word[0])))
    
    file.close()
    checker.close()