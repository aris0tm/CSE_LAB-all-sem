# Prompt the user for the names of two text files
input_file = input("Enter the name of the input text file: ")
output_file = input("Enter the name of the output text file: ")

# Copy the contents of the input file to the output file
with open(input_file, 'r') as input_file_obj:
    with open(output_file, 'w') as output_file_obj:
        for line in input_file_obj:
            output_file_obj.write(line)

print("JOB DONE!!")
