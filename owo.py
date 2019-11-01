#Calculate the owo
#By Sam

def owofied(sentence):
	sentence = sentence.replace("i","wi")
	sentence = sentence.replace("e","we")
	return sentence + " owo"

e = owofied(input("Enter a sentence to owofied >>> "))

print(e)