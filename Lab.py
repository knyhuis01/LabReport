#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string #importing a new module to manipulate strings
# open the text file: 
f = open('relativity.txt')
# read the file and create a list of words (google split function in python):
#split seperates words into seperate strings
words = f.read().split()
f.close() #closes the open file
# calculate how many time each word is repeated (using dictionary):
word_counts = {} #creates an open dictionary
for word in words:# goes through each word with for loop
    word_counts[word] = word_counts.get(word, 0) + 1 # when the word is present more than once, it adds 1 to the total count
# get function gives the value with the key
# create a list of all words:
word_list = list(word_counts.keys()) #displays all the keys in the dictionary in a list

# sort the list of all words based on how many times they are repeated:
def dict_val(x): #defining new function with x as parameter
    return word_counts[x] #return the values of the dictionary
word_list.sort(key = dict_val, reverse = True) #sort the list where keys go with dict_val and do it in reverse order (word with highest frequency first)
# print the top 10 most frequently used words:
print("List of top 10 most frequently used words: ") #prints the string
print(word_list[ : 10])  #print the top ten most frequent words
###this doesn't provide much information about the text because all of these are stop words


###second attempt###
#contents = open('relativity.txt').read() #opens file and returns the specific amount of bytes in the text file
#translation_table = {ord(ch) : None  for ch in string.punctuation}#goes through each character besides punctuation
#contents = contents.translate(translation_table) #returns a string where each character is mapped to its corresponding character in the translation table
#words = contents.split() #splits words up into own strings

# create a list of all words in lower case:
lowercase_words = [word.lower() for word in words]#.lower makes all letters lowercase
# open the file containing all of the stop words in English language:
f = open('stopWords.txt') #opens a text file
# read the file create the list of all stop words in English language:
stop_words = f.read().split()#splits the words into seperate strings in the file and reads them


###remove stop words###
# create the list of non stop words by filtering out the stop words:
non_stop_words = [word for word in lowercase_words if word not in stop_words]#The code loops through every element and creates a new list that contains only the elements that meet the conditions "not in stop_words"
# now calculate the frequency of the non stop words:
word_counts = {} #creates new dictionary
for word in non_stop_words: #for loop through words in non_stop_words
    word_counts[word] = word_counts.get(word, 0) + 1 #counts how many times the word is present in non_stop_words

word_list = list(word_counts.keys()) #makes word_list into a list of the keys in word.counts
# sort the words again:
word_list.sort(key = dict_val, reverse = True) #sorts the list where keys go with dict_val and do it in reverse order (word with highest frequency first)
# prin the top 10 most frequently used words:
print("\nList of top 10 most frequently used non stop words: ") #prints the string
print(word_list[ : 10])#prints first 10 most frequent words in non stop 


