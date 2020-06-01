def check_valid_int(input):
    height = int(input)
    if height > 0 and height < 9:
        return False
    else:
        return True


if __name__ == "__main__":

    height = input("Height: ")

    while check_valid_int(height):
        height = input("Height: ")

    hashes = 1
    height = int(height)

    while hashes <= height:
        spaces = height - hashes
        print("." * spaces + "#" * hashes + "  " + "#" * hashes + "." * spaces)
        hashes = hashes + 1
