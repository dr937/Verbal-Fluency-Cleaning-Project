# -*- coding: utf-8 -*-
"""

Quality assurance code for the WHICAP item-level data TO-DO
1) Changing plural words into singular -> DONE (check later)

2) automated spellchecking -> current task 
    - to do: find ways to fix two word animals (e.g. mantaray -> mantra,
                                                                 sea lion -> stallion)
    - edit the words that have a suffix (- R, - S) without removing the suffix -> partly DONE
    
3) Fix the bug of the new excel sheet containing an index.

4) Implement possibly some sort of user interface that can directly interact with excel
in order to check the words.

5) WordNet implementation in order to boost the accuracy of the Spellchecker

6) Increase optimization as much as possible (currently runs at a snail's pace).

@author: david
"""

#download(nltk)
from spellchecker import SpellChecker #Third party library that implements a spellchecker
from nltk.stem.wordnet import WordNetLemmatizer #Third party library used to lemmatize the words
import pandas as pd
import re

Lem = WordNetLemmatizer() #Turns words into their singular forms
spell = SpellChecker() #Spellchecker for words
changes = [] #Marks the spellchecked changes
singularized_changes = [] #Marks the final changes in the excel sheet
alls = [] # for testing

"""
Main (and really only) function of the whole code. For right now, what it does-in order-
is the following:
    1) Takes the original entry and checks if its a string (so it doesn't try 
    to spellcheck the dates or subject ID's). IF it is not a string, returns 
    the original entry.
    
    2) If it is a string, it strips any whitespace at the end and front that
    might have been inputed and then it strips the - R, - O, - I markings so that
    the base word can be checked (while saving the original form of the entry 
    with the markings).
        -Need to fix the regex to account for people also writing -R, -O, and
        -I
    
    3) Using the third party spell checker, the function verifies if the word 
    is spelled correctly and if it doesn't it offers a correction. I append 
    that change to an array called 'changes' in order for me to see what 
    corrections are made.
        -Currently only works for english words, but could be adapted for 
        spanish if I could find a suitable third party program or if needed 
        find a spanish word corpus and apapt the spellchecker to take in spanish 
        words in some way.
    
    4) An analogous process is carried out to lematize the word (turn it into 
    singular form)
                                                                
    5) Finally, since the spellchecker does not always offer the correct 
    solution (especially since they are contextless nouns), I have instead 
    decided to mark the misspelled words with a (c) and include both the 
    original word and corrected word on the excel sheet in order for a user to
    make the final call on whether the suggested word is appropriate or not.
        - Two different solutions/additions I am eventually planning to add in
        order to potentially limit the need of user interaction:
            ~Using WordNet to check if the word is an animal or not, if it's not, 
            then I could prompt the Spellchecker to suggest a different solution.
            ~Offering more than one possible correction in the spellchecker so 
            users have an easier time of finding a possible correct answer.
"""
def grammar_singularize(orig_word):
    if type(orig_word) == str:                                  #Step 1
        orig_word = orig_word.strip()                           #Step 2
        word = re.sub('\- R$', '', orig_word)
        word = re.sub('\- O$', '', word)
        word = re.sub('\- I$', '', word)
        word = re.sub('\((.*)', '', word)
        base_word = word.strip()
        if len(base_word) > 1:
            fix_word = spell.correction(base_word)              #Step 3
            if base_word != fix_word:
                changes.append((base_word,fix_word))
                
            fin_word = Lem.lemmatize(fix_word)                  #Step 4
            
            if base_word != fix_word:                           #Step 5
                fin_word = orig_word + "->" + fin_word + "(c)"
                singularized_changes.append(fin_word)

            return fin_word
        else:
            return orig_word
    else:
        return orig_word

"""
Line by Line, this code does the following:
    1) Reads in the original csv with the data and turns it into a pandas data frame
                    (only works with the file being in the same folder as code)
    2) Applies the function above to the entire excel sheet.
    3) Exports the processed data frame into a new excel sheet.
"""
#This line would include the original csv from which data is being extracted
item_level_data_df = pd.read_csv('')

#data_df_copy = item_level_data_df.copy()

finalized_df = item_level_data_df.applymap(lambda x: grammar_singularize(x), na_action='ignore')

#This line would inclue the filepath to the new document with the processed data
finalized_df.to_csv(r'', header=True)
