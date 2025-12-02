sentence = str(input("Enter a sentence:"))

count = 0

for i in sentence:
    if i in "aeiouAEIOU":
        count = count + 1

print("TOTAL VOWEL: ", count)