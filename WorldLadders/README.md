Project for Languages, Theory and Computation (CS 3400) 

#Project Prompt 
A Word Ladder program is similar to a "6 degrees of separation" or Oracle of (Kevin) BaconLinks to an external site. game, but using words rather than people or actors. Simply, from a given starting word, find the shortest "ladder" of single letter changes which leads to some final word, where each intermediate state is also a word.

For example:

clash, flash, flask, flack, flock, clock, crock, crook, croon, crown, clown.

As you might infer from the example above, there is no simple algorithm that generates a word ladder.   Rather, you have to search for a ladder by generating all of the possibilities. Doing so will give you an opportunity to use Python data structures like lists and dictionaries.

Your program should first read in the file dictionary.txt Download dictionary.txtgiving it a large collection of words to work with.  All of the examples in the tests that your program will be given will be of lengths 4, 5 and 6, so you can discard all words that are not of one of those lengths.  However, you should write the program so that it is general enough to make it easy for you to change it to handle other word lengths.

You must then read in lines containing pairs of words from a second file named pairs.txt and print out the ladder for each pair or an indication that no ladder exists.  You should check that the input words are of the same length and that that length is in the range described above.  You can assume that every line in the text file will contain two words; you only need to check for potential length problems, as described above.

You can download a pairs.txt Download pairs.txtfile for testing as you develop the program.  This one starts off with some simple cases and includes some pairs for which no ladder can be found.  The final line makes sure you test for the words being of different length. I may use a file with additional tests to grade your program, but if your program works for all of these examples, you should have any other tests covered.

The dictionary.txt file is quite large and the only way to find a solution is to do a breadth first search.  Make sure you use a queue of partial ladders properly to find the shortest possible solution. 

[pairs.txt](https://github.com/elvolpi/PythonCodes/files/12018047/pairs.txt)

#Score 50/50 perfect marks (see rubric) ![rubric_wordladders](https://github.com/elvolpi/PythonCodes/assets/44304662/2c2e9358-acaa-4665-9ac6-431cdff298d6)

