import csv
import os

def read_rows(path):
    with open (path, newline = "") as sponsor:
        sponsor_reader = csv.DictReader(sponsor)
        sponsorlist = list(sponsor_reader)
        return sponsorlist

def count_by(rows, key):
    counts = {}
    for row in rows:
        value = row[key]
        cleaned_value = value.strip().lower() #clean data by stripping and lowering 
        if cleaned_value in counts:
            counts[cleaned_value] += 1
        else:
            counts[cleaned_value] = 1
    return counts

def top_n(counts, n):
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:n]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, "data", "raw", "3112026uksponsor.csv")
if __name__ == "__main__":
    readlist = read_rows(path)
    countlist = count_by(readlist, "Town/City")
    print(top_n(countlist, 10))