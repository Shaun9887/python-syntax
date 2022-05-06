def print_upper_words(words, letters):
    """Print words but in all CAPS"""
    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print(word.upper())

print_upper_words(['Jared', 'Shaun', 'Eric', 'Elijah', 'Josh'], ['J', 'Y'])