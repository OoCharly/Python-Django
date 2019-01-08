def numbers():
    with open("numbers.txt", "r") as file:
        content = file.read().split(',')
        for number in content:
            print(number.strip())

if __name__ == "__main__":
    numbers()