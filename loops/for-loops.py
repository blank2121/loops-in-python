# Here are a few examples of for loops and how you can use them



# 1) runing over code x times

for i in range(10):
    print(i)

# 2) looping over the indices of a string

mySentence = "Loops are helpful!"

for letter in mySentence:
    print(letter)

# or you can do this:


stringLen = len(mySentence)

for index in range(stringLen):
    print(mySentence[index])

