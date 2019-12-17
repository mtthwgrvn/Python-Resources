def count(word, letter):
    """"
    Counts the number of times a given letter appears in a word
    Input:  word -- the word in question
            letter -- the letter in the word to count
    Output:prints the number of letters
    """
    counter = 0

    for character in word:
        if character == letter:
            counter = counter + 1
    print(counter)

input_word = input('Enter the word: ')
input_letter = input('Enter the letter: ')
count(input_word, input_letter)
