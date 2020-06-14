from sys import argv
import sqlite3


if __name__ == "__main__":

    # Check for the correct number of args
    if len(argv) != 2:  # The filename of the python file counts as the first [0]
        print("Provide 1 arguments, the CSV file")
        exit(1)

    HOUSE = argv[1]

    db = sqlite3.connect("students.db")
    c = db.cursor()

    data = c.execute("SELECT * FROM students WHERE house=? ORDER BY last;", [HOUSE])

    for row in data:
        first = row[1]
        last = row[3]
        year = row[5]
        if row[2] == None:
            middle = ""
        else:
            middle = row[2] + " "

        print(f"{first} {middle}{last}, born {year}")
