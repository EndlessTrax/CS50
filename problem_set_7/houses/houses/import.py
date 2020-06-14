from sys import argv
import csv
import sqlite3


def fetch_student_data(file):
    data_dict = list()

    with open(file, "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            data_dict.append(line)

    return data_dict


def split_name(full_name):
    names = full_name.split(" ")
    return names


if __name__ == "__main__":

    # Check for the correct number of args
    if len(argv) != 2:  # The filename of the python file counts as the first [0]
        print("Provide 1 arguments, the CSV file")
        exit(1)

    CHARACTERS_CSV = argv[1]

    db = sqlite3.connect("students.db")
    c = db.cursor()

    data = fetch_student_data(CHARACTERS_CSV)

    for student in data:
        full_name = student["name"]
        names = split_name(full_name)
        if len(names) == 3:
            first = names[0]
            middle = names[1]
            last = names[2]
            c.execute(
                "INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                (first, middle, last, student["house"], student["birth"]),
            )
            db.commit()
        elif len(names) == 2:
            first = names[0]
            last = names[1]
            c.execute(
                "INSERT INTO students (first, last, house, birth) VALUES(?, ?, ?, ?)",
                (first, last, student["house"], student["birth"]),
            )
            db.commit()
        else:
            print("Something went wrong!")
            exit(1)
