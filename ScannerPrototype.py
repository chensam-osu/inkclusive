#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
This python script loads in any specified text file from the device.
The program then goes through every line of text in the text file to search for 
specified discriminatory language. If the program successfully detects a word(s)
as discriminatory, it will flag it and add the word to a list.

This is a prototype script. Currently console application. 
"""

from pathlib import Path
import sys, random, filecmp, os
import time, hashlib, string



def fileload():
    
    #file1 is the standard stored list of profanities
    #file2 is the txt file loaded to be checked for racism
    #file3 is an output file of detect profanities from file 2 using file1 as the guide
    
    
    f1= open("file1.txt", "r")  #standard stored list in the system
    print(f1.read())
    d= set(f1.readlines())
   # print(f1.read())  #checking to make sure the file is accurate
    
   #open("file3.txt", "w") #write file for detected similarities
    
    while True:
        
        print("Please enter the file name you wish to scan: ")  #input file2.txt
        
        filename = input()
        print(filename)
        
        try:
            with open(filename, 'r') as f2:
                #print(f2.read())
                e=set(f2.readlines())
                #print (my_file)
                print("Success, file has been successfully accessed! ")
                
                
            for line1 in f1:
                i += 1
                f2 = open(filename)
                for line2 in f2:
                # matching line1 from both files
                    if line1 == line2:  
            # print IDENTICAL if similar
                        print("Line ", i, ": IDENTICAL")       
                    else:
                        print("Line ", i, ":")
            # else print that line from both files
                        print("\tFile 1:", line1, end='')
                        print("\tFile 2:", line2, end='')
                    break
            
            
            f1.close()                                       
            f2.close() 
                
                
                
                    
            return f2
        
        except FileNotFoundError:
            print("No file found.\n")     
            
            
        
#         # if not filename.exists():
#         #     print("ERROR, file doesn't exist!")
#         # else:
#         #     print("The file exists!")

#     # file1 = "file1.txt"
#     # file2 = "file2.txt"
#     # file3 = "file3.txt"

#     with open("f1") as f1, open("f2") as f2: 
#

#f1= open("file1.txt", "r")  #reading from the list of racist words
#print(f1.read())

#f3 = open("file3.txt", "w") #write file for detected similarities


    
def main():
    
    path= os.getcwd()
    print(path)
    
    print("WELCOME TO INKclusive!\n")
    print("This program scans for discriminatory language in any uploaded text file.\n ")
    
    
    fileload()
    

    
main()
