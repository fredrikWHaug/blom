
def get_height():
    while True:
        try:
            height = int(input('Enter an integer between 1 and 8: '))
            if 1 <= height <= 8:
                return height
        except:
            ValueError

def print_pyramid(heigth):
    for i in range(heigth):
        spaces = (' ' * (heigth - i - 1))
        hashes = ('#' * (i + 1))
        print(spaces + hashes)

def main():
    heigth = get_height()
    print_pyramid(heigth)

if __name__ == '__main__':
    main()