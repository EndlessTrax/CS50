from sys import argv, exit
import csv


def fetch_database_data(file):
    data_dict = list()

    with open(file, "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            data_dict.append(line)

    return data_dict


def get_nucleotides(file):
    nucleotides = list()
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter=",")
        headers = next(reader)
        for h in headers:
            if h != "name":
                nucleotides.append(h)

    return nucleotides


def fetch_dna_sequence(file):
    with open(file, "r") as f:
        dna = f.readline()

    return dna


def compare_STR(dna, sub_str):
    seq_len = len(sub_str)
    count = 0

    while True:
        if dna.count(sub_str * (count + 1)) == 0:
            return count
        else:
            count += 1

    return count


if __name__ == "__main__":

    # Check for the correct number of args
    if len(argv) != 3:  # The filename of the python file counts as the first [0]
        print("Provide 2 arguments, database and sequence file paths")
        exit(1)

    # Globals
    DATABASE = argv[1]
    SEQUENCE = argv[2]

    nucleotides = get_nucleotides(DATABASE)
    dna = fetch_dna_sequence(SEQUENCE)
    data = fetch_database_data(DATABASE)

    seq_counts = {}

    for nu in nucleotides:
        count = compare_STR(dna, nu)
        seq_counts[f"{nu}"] = count

    for person in data:
        matches = 0
        for k, v in person.items():
            try:
                if int(v) == seq_counts[k]:
                    matches += 1
            except:
                pass

        if matches == len(seq_counts):
            print(person["name"])
            exit(1)

    print("No Match")
