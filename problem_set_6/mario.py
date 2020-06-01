from cs50 import get_int

def check_valid_int(input):
    if height > 0 and height < 9:
        return False
    else:
        return True


if __name__ == '__main__':

    height = get_int("Height: ")

    while check_valid_int(height):
        height = get_int("Height: ")
    
    hashes = 1
    height = int(height)

    while hashes <= height:
        spaces = height - hashes
        print(' ' * spaces + '#' * hashes + '  ' + '#' * hashes)
        hashes = hashes + 1