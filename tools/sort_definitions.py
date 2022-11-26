import csv
import sys

if len(sys.argv) < 2:
    print("Usage: python sort_definitions.py <input_file>")
    sys.exit(1)

with open(sys.argv[1], "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    # remove duplicates
    terms = {}
    for tup in terms:
        key = tup[0]
        # keep term w/ longest definition if duplicates
        if key not in terms or len(terms[key][1]) < len(tup[1]):
            terms[key] = tup

    terms = {tup[0]: tup for tup in data}.values()
    # sort by term
    terms = sorted(terms, key=lambda tup: tup[0])

with open(sys.argv[1], "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(terms)
