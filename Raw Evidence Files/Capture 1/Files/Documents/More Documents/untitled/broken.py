import re

def fileToString(pathToFile):
	f = open(pathToFile, "r")
	strs = ""
	#adds each line of the file to the strs string
	for line in f.readlines():
		strs+=line
	return strs

def ASCII():
	#number of ASCII characters
	NumOfASCII = 128
	#returns list of all ASCII characters
	return "".join([chr(i) for i in range(NumOfASCII)])

def sumName(name):
	sums=0
	#sums the indices in ASCII of all the characters in name
	for x in name:
		sums+=ord(x)
	return sums

def indexInFile(password, name):
	indices = []
	ASCIIArray = ASCII()
	#populates an array of indices to be used by the encoder
	for chrs in password:
		indices.append(ASCIIArray.index(chrs)+sumName(name)*2)
	return indices

def indexInASCII(name, encoded):
	indices = []
	ASCIIArray = ASCII()
	#split on all non-numeric characters
	#remove first index because it is blank
	indexList = re.split("[^\d]",encoded)[1:]
	#converts encoded characters to ASCII
	for index in indexList:
		indices.append(ASCIIArray[int(index) - (sumName(name)*2)])
	#returns decoded message
	return "".join(indices)

def encode(password,name):
	#returns a list of indices to be used for encoding
	indices = indexInFile(password,name)
	#convert file associated with name to a string
	bill = fileToString("./%s.txt"%name)
	encoded = ""
	#add letter in file plus index of the letter in the file to the encoded string
	for index in indices:
		encoded+=bill[index]+str(index)

	return encoded

print(indexInASCII("BillOfRights", "i2454 2497d2496n2502 2470 2500 2507o2436s2452 2500s2503n2502l2487e2456 2497 2500h2485l2487 2470b2490e2491a2501m2466 2483a2501a2501e2505 2497 2500a2486"))