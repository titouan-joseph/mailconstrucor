import argparse
import os


def mail(file, domain, outputFile):

    if os.path.exists(outputFile):
        print("Error file exists")
        exit(-1)

    if not outputFile.endswith(".txt"):
        outputFile = outputFile + ".txt"

    with open(file, "r") as data:
        data.readline()
        for line in data.readlines():
            field = line.split(';')
            email = field[2].lower().strip().replace(" ", "") +\
                    '.' + field[1].lower().strip().replace(" ", "") +\
                    "@" + domain

            with open(outputFile, "a") as output:
                output.write(email + ";")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="csv file with ';' separator and gender;last name;fisrt name")
    parser.add_argument("-d", "--domain", help="domain of email example: domain.com", default="insa-lyon.fr")
    parser.add_argument("-o", "--output", help="output file", default="output.txt")
    args = parser.parse_args()
    mail(args.file, args.domain, args.output)
