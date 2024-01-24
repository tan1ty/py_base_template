import csv
import sys


def main():     
    try:
        if len(sys.argv) < 3:
            raise ValueError("You missed some file")
        csv_file = sys.argv[1]
        if not csv_file.endswith(".csv"):
            raise ValueError("The first file must be a CSV file")
        txt_file = sys.argv[2]
        if not txt_file.endswith(".txt"):
            raise ValueError("The second file must be a TXT file")
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)

   
    databases = []
    with open(csv_file, newline="") as data:
        reader = csv.DictReader(data)
        for row in reader:
            for key in row.keys():
                if key != "name":
                    row[key] = int(row[key])
            databases.append(row)
        str_subsequences = reader.fieldnames

    
    with open(txt_file, "r") as file:
        dna_sequence = file.read()

    suspect = {
        str_s: longest_match(dna_sequence, str_s)
        for str_s in str_subsequences
        if str_s != "name"
    }

    def find_match():
        match = False
        for person in databases:
            if {key: value for key, value in person.items() if key not in "name"} == suspect:
                print(person["name"])
                match = True
                return
        if not match:
            print("No match")

    find_match()


def longest_match(sequence, subsequence):
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0        
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length

            if sequence[start:end] == subsequence:
                count += 1          
            else:
                break                

        longest_run = max(longest_run, count)
    return longest_run

if __name__ == "__main__":
    main()
