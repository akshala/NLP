from nltk.tokenize import word_tokenize, SyllableTokenizer, LineTokenizer, TabTokenizer, SpaceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.probability import ConditionalFreqDist 

# tokenize syllables
tk = SyllableTokenizer() 
print(tk.tokenize("Gametophyte"))

#tokenize lines
tk = LineTokenizer(blanklines ='keep') # this insures that blanklines are also kept
print(tk.tokenize("The price\n\n of burger \nin BurgerKing is Rs.36.\n"))

#tokenize tabs
tk = TabTokenizer()
print(tk.tokenize("I\t am\t\t interested \t in NLP"))

#tokenise spaces
tk = SpaceTokenizer()
print(tk.tokenize("Hello world! This is me."))

text = "Natural language processing (NLP) is a field " + \
		"of computer science, artificial intelligence " + \
		"and computational linguistics concerned with " + \
		"the interactions between computers and human " + \
		"(natural) languages, and, in particular, " + \
		"concerned with programming computers to " + \
		"fruitfully process large natural language " + \
		"corpora. Challenges in natural language " + \
		"processing frequently involve natural " + \
		"language understanding, natural language" + \
		"generation frequently from formal, machine" + \
		"-readable logical forms), connecting language " + \
		"and machine perception, managing human-" + \
		"computer dialog systems, or some combination " + \
		"thereof."

#tokenize sentences
print("-------sentences-------", sent_tokenize(text)) 
#tokenize words
print("-------words-------", word_tokenize(text))

#frequency distribution in a dictionary
tk = ConditionalFreqDist()
text = "The big red fox, jumped on the big red box."
for word in word_tokenize(gfg): 
	condition = len(word) 
	tk[condition][word] += 1
print(tk)
