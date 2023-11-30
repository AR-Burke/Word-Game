########################
#
# Python Term Project
# Class Section: CS 135
# Name: Aria Burke
# Insturctor: Qiping Yan
# Assignment Lab #3
# Submission Date : 4/12/2023
#
########################

import math
import random
import string
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
WORDLIST_FILENAME = "words.txt"
LETTER_VALUES = {
    'a': 3, 'b': 2, 'c': 2, 'd': 2, 'e': 3, 'f': 2, 'g': 2, 'h': 2, 'i': 3, 'j': 2, 'k': 2, 'l': 2, 'm': 2, 'n': 2, 'o': 2, 'p': 2, 'q': 2, 'r': 2, 's': 2, 't': 2, 'u': 3, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2
    }

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loding Words Please Wait..")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print (" ", len(wordList), "words loaded.")
    return wordList

def get_frequency_dict(sequence):
        freq = {}
        for x in sequence:
            freq[x] = freq.get(x,0) + 1
        return freq

def get_word_score(word, n):
    word = word.lower()
    first_component = 0
    for letter in word:
        first_component += LETTER_VALUES[letter]
    
    second_component = 7 * len(word) - 3 * (n - len(word))
    if second_component < 1:
        second_component = 1
        
    return first_component + second_component

def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')
    print()

def deal_hand(n):
    hand={}
    num_vowels = 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def is_valid_word(word, hand, word_list):
    word = word.lower()
    words = []
    
    lw = list(word)
    if '*' in lw:
        position = lw.index('*')
        for letter in VOWELS:
            lw[position] = letter
            words.append("".join(lw))
    else:
        words.append(word)
    
    found = False
    for w in words:
        if w in word_list:
            found = True
    
    if not found:
        return False
    
    word_freq_dict = get_frequency_dict(word)
    for letter, freq in word_freq_dict.items():
        if freq > hand.get(letter, 0):
            return False
    
    return True
    
def calculate_handlen(hand):
    letters=0
    
    for key, value in hand.items():
        letters += value

    return letters

def play_hand(hand, word_list):

    total_score = 0
    while calculate_handlen(hand) > 0:
        print("Current Hand:", end= " ")
        display_hand(hand)
        word = input('Enter word, or "end" to end the game: ')
        if word == 'end':
            break
        else:
            if is_valid_word(word, hand, word_list):
                word_score = get_word_score(word, calculate_handlen(hand))
                total_score += word_score
                print('"' + word + '"', "earned", word_score, "points. Total:", total_score, "points")
            else:
                print("Sorry! That is not a valid word. Please choose another word.")
    print("Total score for this hand:", total_score, "points")
    print("-"*10)
    return total_score


def play_game(word_list):
    total_hands = 7
    final_score = 0
    
    for n in range(total_hands):
        hand = deal_hand(HAND_SIZE) 
        hand_score = play_hand(hand, word_list)
        final_score += hand_score
        
    print("Total score over all hands:", final_score)

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)