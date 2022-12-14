word = "Hello"

reverse_word = " "

for index in range(len(word) -1, -1, -1):
   reverse_word += word[index]

print(reverse_word)   

# reverse_word = word[4] + word[3] + word[2] + word[1] + word[0]
# print(reverse_word)

# reverse_word = word[len(word) -1]

# print(reverse_word)
