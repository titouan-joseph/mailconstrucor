import argparse

def mail(file):
    with open(file, "r") as data:
        data.readline()
        for line in data.readlines():
            field = line.split(';')
            email = field[2].lower().strip().replace(" ", "") +\
                    '.' + field[1].lower().strip().replace(" ", "") +\
                    "@insa-lyon.fr"

            with open("liste.txt", "a") as output:
                output.write(email + ";")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="csv file with ';' separator and gender;last name;fisrt name")
    args = parser.parse_args()
    mail(args.file)
