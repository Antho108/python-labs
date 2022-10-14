# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.




word = "tweezers"
# word[1:3] + " " + word[6:] + word[2:4] + " " +  word[0:1] + word[5:6]+ word[2:4]+ word[6:]
x = ( word[1:3] + " " + word[7:] + word[2:4] + " " +  word[0:1] + word[6:7]+ word[2:4]+ word[7:] )
print(x)
