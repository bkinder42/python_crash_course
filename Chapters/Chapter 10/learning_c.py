file_path = "resources/learning_python.txt"

with open(file_path) as file:
    for line in file.readlines():
        print(line.rstrip().replace("Python", "C"))
    print()
