#based on chopping of prefixs and sufixs
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
   
ps = PorterStemmer() 
words = ["likes", "liked", "likely", "liking", "chocolate", "choco", "chocolatey"]

for w in words: 
	print(w, " : ", ps.stem(w)) 	

sentence = "Programers program with programing languages"
words = word_tokenize(sentence) 
   
for w in words: 
	print(w, " : ", ps.stem(w)) 