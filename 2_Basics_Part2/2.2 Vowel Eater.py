word = input('Enter a word. I will eat the vowels. Yum.')

for letter in word:
    if letter in 'aeiou':
        continue
    else:
        print(letter)
