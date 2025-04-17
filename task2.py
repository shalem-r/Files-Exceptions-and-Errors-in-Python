#Takes user input and writes it to a file named output.txt.
content = input("Enter text to write to the file: ")
with open('output.txt', 'w') as file:
    file.write(content+'\n')
    print("Data successfully written to output.txt\n")

#Appends additional data to the same file.
append_content = input("Enter additional text to append: ")
with open('output.txt','a') as file:
    file.write(append_content)
    print("Data successfully appended\n")

#Reads and displays the final content of the file.
with open('output.txt','r') as file:
    print("Final content of output.txt:")
    file_content = file.read()
    print(file_content)
    file.close()

