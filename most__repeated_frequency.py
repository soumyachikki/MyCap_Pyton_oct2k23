def most_frequent(input_string):
    # Create an empty dictionary to store letter frequencies
    letter_frequency = {}
    
    # Convert the input string to lowercase to make the comparison case-insensitive
    input_string = input_string.lower()
    
    # Iterate through the string and count letter frequencies
    for letter in input_string:
        if letter.isalpha():  # Check if the character is a letter
            if letter in letter_frequency:
                letter_frequency[letter] += 1
            else:
                letter_frequency[letter] = 1
    
    # Sort the dictionary by values (frequencies) in decreasing order
    sorted_frequency = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)
    
    # Print the letters and their frequencies
    for item in sorted_frequency:
        print(f"{item[0]} = {item[1]}", end=" ")
    
# Example usage
input_string = input("Enter a string:")
most_frequent(input_string)
