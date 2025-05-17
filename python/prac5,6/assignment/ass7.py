# 1. Create a new file, write content, close, and reopen to read

def create_and_read_file():
    with open("sample.txt", "w") as file:
        file.write("Hello, this is a sample file.\nWelcome to file handling in Python.")
    
    with open("sample.txt", "r") as file:
        content = file.read()
        print("File Content:\n", content)

# 2. Read numbers, separate odd and even numbers

def separate_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    with open("odd_numbers.txt", "w") as odd_file, open("even_numbers.txt", "w") as even_file:
        for num in numbers:
            if num % 2 == 0:
                even_file.write(f"{num}\n")
            else:
                odd_file.write(f"{num}\n")

# 3. Read a text file and print any 5 words

def read_five_words():
    with open("sample.txt", "r") as file:
        words = file.read().split()
        print("First 5 Words:", words[:5])

# 4. Generate and save a triangle pattern

def save_triangle_pattern():
    with open("triangle.txt", "w") as file:
        for i in range(1, 6):
            file.write(" " * (5 - i) + "*" * (2 * i - 1) + "\n")

    with open("triangle.txt", "r") as file:
        print("Triangle Pattern:\n", file.read())

# Execute functions
create_and_read_file()
separate_numbers()
read_five_words()
save_triangle_pattern()