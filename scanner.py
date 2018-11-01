import os
import re

# Function to split input into tokens
def getTokens (text,tokens_reg):
    tokens = re.findall(tokens_reg,text)
    return tokens

def checkOthers(token,variable_or_reserved_regex):
    regexp = re.compile(variable_or_reserved_regex)
    if regexp.search(token) and token not in reserved_words:
        return True
    return False

# Read the input from file input.txt and put it in input string
filename = "input.txt"
filePath = os.path.abspath(filename)
mode = "rt"
openFile = open(filePath,mode)
myFileText = openFile.read()
openFile.close()

# Removing the omments between {}
inputWithoutComments = re.sub(r'{.*}',"",myFileText)
# Removing Blank Lines
inputWithoutComments_andWithoutNewLines = inputWithoutComments.strip('\n')

# Expression to Parse input into tokens
tokens_reg = '(\:=|\*|\+|\-|\;|\(|\)|\/|\>=|\!=|\==|\=|\>|\<=|\<|[a-zA-z_$][a-zA-Z_0-9$]*|[0-9][[\.][0-9]+]?|[0-9]+)'
# Lists of reserved words, special symbols
reserved_words = ['if','then','else','repeat','until','end','read','write']
special_symbols = ['=','<','<=','>','>=',':=','+','-','*','/',';','==','!=']
# Used in check others function to diff. between variable names and reserved words
variable_or_reserved_regex = "[a-zA-z_$][a-zA-Z_0-9$]*"

tokens = getTokens(inputWithoutComments_andWithoutNewLines,tokens_reg)
#print(tokens)

Dict = {}
for token in tokens:
    if token in reserved_words:
        Dict[token] = "Reserved Word"
    elif token in special_symbols:
        Dict[token] = "Special Symbol"
    elif checkOthers(token,variable_or_reserved_regex):
        Dict[token] = "Identifier"
    else:
        Dict[token] = "Number"

print(Dict)

output = open("output.txt", "wt")
output.write(str(Dict))
output.close()
