file_path = "resources/learning_python.txt"
with open(file_path) as file:
    print(file.read())
    print()

with open(file_path) as file:
    for line in file.readlines():
        print(line.rstrip())
    print()

with open(file_path) as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())