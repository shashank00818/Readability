'''The Coleman-Liau index is a mathematical formula to determine 
grade level for reading a sentece or paragraph.
The formula is:
index = 0.0588 * L - 0.296 * S - 15.8'''

# asking user for input
txt = input('Text: ')

# calculating letters
letters = 0
for i in range(len(txt)):
    if txt[i].isalpha():
        letters += 1

# calculating words
words = 1
for i in range(len(txt)):
    if txt[i].isspace():
        words += 1

# calculating sentences
sentences = 0
for i in range(len(txt)):
    if txt[i] == '.' or txt[i] == '!' or txt[i] == '?':
        sentences += 1

L = 0
S = 0
index = 0

# calculating L and S
L = (letters * 100)/words
S = (sentences * 100)/words

# calculating index by using formula
index = 0.0588 * L - 0.296 * S - 15.8
x = round(index)

# printing grade based on different conditions
if x >= 1 and x <= 15:
    print('Grade', x)

elif x < 1:
    print('Before Grade 1')

elif x >= 16:
    print('Grade 16+')