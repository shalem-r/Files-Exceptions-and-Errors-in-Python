try:
    file_name = 'sample2.txt'
    file = open(file_name,'r')
    read_line = file.readlines()
    for index,line in enumerate(read_line,start=1):
        print(f"Line {index}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The File '{file_name}' was not found" )