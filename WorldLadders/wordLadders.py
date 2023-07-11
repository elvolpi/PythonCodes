from collections import deque

#The purpose of this project is to implement a word ladder program that connects
#two words of the same length by words that are different from the preceeding
#word by one character.
#Inputs: Two files are taken in for the program. 'dictionary.txt' has a single
# word on each line and 'pairs.txt' has two words of the same length seperated
#by white space. Weused 'dictionary.txt' to build a list of words to search from.
#We can use any file like 'pairs.txt' to build word ladders. Words longer than
#length 6 may take extremely long.
# Also, we take user input for max length of word (recommended 6 characters) and 
#for minimum size of word (recommended 4)

#driver function.
# Gets user input, assigns files to variables, calls getWords and getPairs.
def main():
		dicFile = 'dictionary.txt'
		MAX_SIZE = int(input("What is the max size for words?"))
		MIN_SIZE = int(input("What is the min size for words?"))
		dic = getWords(dicFile, MAX_SIZE, MIN_SIZE)
		pairsFile = 'pairs.txt'
		getPairs(pairsFile,dic)

#Determines if two words are off by one letter.

#Pre: Words passed in must be of same length.

#Returns: True if the two words are different by one character. False if the
#lengths of the two words are not equal, if they are the same word, if different
#by more than one character.
def offByOne(word1,word2):
		if len(word1) != len(word2):
			return False
		numDifference = 0
		for i in range(len(word1)):
			if word1[i] != word2 [i]:
				numDifference += 1;
			if numDifference > 1:
					return False
		if numDifference != 1:
			return False
		else:
			return True
#Loads words from a file to composite a dictionary. Dictionary is keyed by
# by length of word (i.e. all words length four will be value in key 4).

#Parameters is the filename, the maxSize of the word, and the minSize of
#the word. Words are entered into dictionary words.

#Return: The dictionary named words.

def getWords(filename, maxSize, minSize):
	words = {}
	with open(filename) as f:
		for line in f:
			current = line.strip('\n')
			if (len(current) <= maxSize) and (len(current) >= minSize):
				if len(current) in words:
					words[len(current)].append(current)
				else:
					words[len(current)] = [current]
	f.close()
	return words

#searches through dictionary to find a ladder of words off by one character
# of two given words.

#Parameters: The word of the beginning of the ladder (wordFrom), the word at
#the end of the ladder (wordTo), and the dictionary object.

#Outputs: If no ladder between two words is found, a message will output.

#Process: Uses a list as a queue to keep track of ladders in process. The
#set usedWords keeps track of words we have already accounted for in the
#dictionary (meaning already within a list in our queue). Once we have
#built a ladder from wordFrom to wordTo the ladder gets returned.

def findLadder(wordFrom, wordTo, dict):
	if wordFrom == wordTo:
		return wordFrom
	key = len(wordFrom)
	searchWords = dict[key]
	usedWords = set([wordFrom])
	queue = []
	queue.append([wordFrom])
	while len(queue) != 0:
		currLadder = queue.pop(0)
		for word in searchWords:
			if word in usedWords:
				continue
			if offByOne(currLadder[-1],word):
				queue.append(currLadder + [word])
				usedWords.add(word)
				if word == wordTo:
					return currLadder+[word]
	print("No ladder found.")
	return [False]

if __name__ == '__main__': main()
		
