import argparse
import os


def mail(file, domain, outputFile, overwrite):

    if not outputFile.endswith(".txt"):
        outputFile = outputFile + ".txt"

    if os.path.exists(outputFile) and not overwrite:
        print("Error file exists")
        exit(-1)
    elif overwrite:
        os.remove(outputFile)

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
    parser.add_argument("--overwrite", help="overwrite output file", action='store_true')
    args = parser.parse_args()
    if args.overwrite:
        mail(args.file, args.domain, args.output, True)
    else:
        mail(args.file, args.domain, args.output, False)
