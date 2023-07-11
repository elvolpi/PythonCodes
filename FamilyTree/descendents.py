#GEDCOM parser design/pseudocode 

#Create empty dictionaries of individuals and families
#Ask user for a file name and open the gedcom file
#Read a line
#Skip lines until a FAM or INDI tag is found
	#Call functions to process those two types
#Print descendant chart when all lines are processed

##Processing Individual 
#Get pointer string
#Make dictionary entry for pointer with ref to Person object
#Find name tag and identify parts (surname, given names, suffix)
#Find FAMS and FAMC tags; store FAM references for later linkage
#Skip other lines

##Processing a family
#Get pointer string
#Make dictionary entry for pointer with ref to Family object
#Find HUSB WIFE and CHIL tags
	#Add included pointer to Family object
	#[Not implemented ] Check for matching references in referenced Person
	#object
		#Note conflicting info if found.
#Skip other lines

#Print info from the collect of Person objects
#Read in a person number
#Print pedigree chart
#---------------------------------------------------------------------------
class Family():
# Stores info about a family
# Created when an Family (FAM) GEDCOM record is processed.
#-------------------------------------------------------------------
	def __init__(self, ref):
	# Initializes a new Family object, storing the string (ref) by
	# which it can be referenced.
		self._id = ref
		self._husband = None
		self._wife = None
		self._children = []
		self._marriage = []

	def addHusband(self, personRef):
	# Stores the string (personRef) indicating the husband in this family
	  self._husband = personRef

	def addWife(self, personRef):
	# Stores the string (personRef) indicating the wife in this family
		self._wife = personRef

	def addChild(self, personRef):
	# Adds the string (personRef) indicating a new child to the list
		self._children += [personRef]

	def addMarriage(self, event):
		self._marriage += [event]

def printFamily(self, firstSpouse, prefix):
# Used by printDecendants in Person to print spouse
# and recursively invole printDescendants on children
	if prefix != '': prefix = prefix[:-2]+' '
	if self._husband == firstSpouse:
		if self._wife: # make sure value is not None
		print(prefix+ '+' +str(persons[self._wife]))
	else:
			if self._husband: # make sure value is not None
			print(prefix+ '+' +str(persons[self._husband]))
	for child in self._children:
		persons[child].printDescendants(prefix+'|--')

def __str__(self):
	if self._husband: # make sure value is not None
		husbString = ' Husband: ' + self._husband
	else: husbString = ''
	if self._wife: # make sure value is not None
		wifeString = ' Wife: ' + self._wife
	else: wifeString = ''
	if self._children != []: 
		childrenString = ' Children: ' +str(self._children)
	else: childrenString = ''
	return husbString + wifeString + childrenString

def searchDescendants(self,personID):
#calls isDescendant recursively to traverse through tree to
#determine if person is a descendant within that family.
#stops when there is no more children
isDescendant = False
	for child in self._children:
		isDescendant = persons[child].isDescendant(personID)
		if isDescendant:
			return True
		return False

def getParents(self):
	parents = []
	if self._wife:
		parents.append(self._wife)
	if self._husband:
		parents.append(self._husband)
	return parents

#-----------------------------------------------------------------------
class Event():
	def __init__(self, eventType):
		self._type = eventType
		self._date = ""
		self._place = ""

	def addDate(self, dateString):
		self._date = dateString
	
	def addPlace (self, placeString):
		self._place = placeString
	
	def __str__(self):
		return str(self._type) + ": " + str(self._date) + " " + str(self._place)

#----------------------------------------------------------------------
	def getPointer(line):
	# A helper function used in multiple places in the next two functions
	# Depends on the syntax of pointers in certain GEDCOM elements
	# Returns the string of the pointer without surrounding '@'s or trailing
		return line[8:].split('@')[0]

	def addEvent(eventType):
	#Used in processPerson for birth and death events
	#collects necessary data from file on dates and events
		global line
		newEvent = Event(eventType)
		line = f.readline()
		tag = line[2:6]
		while line[0] == '2':
			tag = line[2:6]
			if tag == 'DATE':
				newEvent._date = line[7:].strip('\n')
			if tag == 'PLAC':
				newEvent._place = line[7:].strip('\n')
			line = f.readline()
				return newEvent

	def processPerson(newPerson):
		global line
		line = f.readline()
		while line[0] != '0': # process all lines until next 0-level
			tag = line[2:6] # substring where tags are found in 0-level elements
			if tag == 'NAME':
				newPerson.addName(line[7:])
				#print(line[7:], " ")
			elif tag == 'FAMS':
				newPerson.addIsSpouse(getPointer(line))
			elif tag == 'FAMC':
				newPerson.addIsChild(getPointer(line))
			elif tag == 'BIRT':
				#print("birth")
				newPerson.addBirth(addEvent('n'))
				continue
			elif tag == 'DEAT':
				newPerson.addDeath(addEvent('d'))
				continue
			line = f.readline()
			# read to go to next line



	def processFamily(newFamily):
		global line
		line = f.readline()
		while line[0] != '0': # process all lines until next 0-level
			tag = line[2:6]
			if tag == 'HUSB':
				newFamily.addHusband(getPointer(line))
			elif tag == 'WIFE':
				newFamily.addWife(getPointer(line))
			elif tag == 'CHIL':
				newFamily.addChild(getPointer(line))
			elif tag == 'MARR':
				newEvent = Event("MA")
				line = f.readline()
				tag = line[2:6]
				if tag == 'DATE':
					newEvent._date = line[7:].strip('\n')
				if tag == 'PLAC':
					newEvent._place = line[7:].stip('\n')
				newFamily.addMarriage(newEvent)
				continue
		# read to go to next line
		line = f.readline()

---------------------------------------------------------------------------
##Main programs starts here 
persons = {} # to save references to all of the Person objects
families = {} # to save references to all of the Family objects
filename = "Kennedy.ged" # Set a default name for the file to be processed
### Uncomment the next line to make the program interactive

#filename = input("Type the name of the GEDCOM file:")

f = open (filename)
line = f.readline()
while line != '': # end loop when file is empty
	fields = line.strip().split(' ')
	# print(fields)
	if line[0] == '0' and len(fields) > 2:
		# print(fields)
		if (fields[2] == "INDI"):
			ref = fields[1].strip('@')
			persons[ref] = Person(ref) ## store ref to new Person
			processPerson(persons[ref])
		elif (fields[2] == "FAM"):
			ref = fields[1].strip('@')
			families[ref] = Family(ref) ## store ref to new Family
			processFamily(families[ref])
		else: # 0-level line, but not of interest -- skip it
			line = f.readline()
	else: # skip lines until next candidate 0-level line
		line = f.readline()

# Optionally print out all information stored about individuals
#for ref in sorted(persons.keys()):
	# print(ref+':', persons[ref])

# Optionally print out all information stored about families
#for ref in sorted(families.keys()):
	# print(ref+':', families[ref])

##person = "I46" # Default selection to work with Kennedy.ged file
### Uncomment the next line to make the program interactive
#person = input("Enter person ID for descendants chart: ")


import GEDtest
GEDtest.runtests(persons,families)







