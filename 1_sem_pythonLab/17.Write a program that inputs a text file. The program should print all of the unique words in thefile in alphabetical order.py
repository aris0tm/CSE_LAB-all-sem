# before the name input create a new text file input the same name
# Input the name of the text file
filename = input("Enter the name of the text file: ")

# Set to store unique words
unique_words = set()

# Read the text file and extract unique words
try:
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                unique_words.add(word.strip())
except FileNotFoundError:
    print("File not found. Please make sure the file name is correct and try again.")
    exit()

# Print unique words in alphabetical order
print("Unique words in the file in alphabetical order:")
for word in sorted(unique_words):
    print(word)
