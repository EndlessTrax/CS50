from math import floor


def count_letters(text):
    return len(text.replace(" ", "").replace("?", ""))


def count_sentence(text):
    s = 0
    for char in text:
        if char == "." or char == "?" or char == "!":
            s = s + 1
    return s


def count_words(text):
    w = text.split(" ")
    return len(w)


if __name__ == "__main__":
    text = input("Enter text: ")

    letters = count_letters(text)
    sentences = count_sentence(text)
    word_count = count_words(text)

    index = (
        0.0588 * (100.0 * letters / word_count)
        - 0.296 * (100.0 * sentences / word_count)
    ) - 15.8
    print(index)

    grade = floor(index)
    print(grade)

    if grade < 1:
        print("Before Grade 1")

    elif grade >= 16:
        print("Grade 16+")

    else:
        print(f"Grade {grade}")
