import csv
import sys
if len(sys.argv) == 3:
    if sys.argv[1][-3:] == "csv":#
        try:
            with open(sys.argv[1], 'r') as file:
                reader = csv.DictReader(file)
                with open(sys.argv[2], 'w', newline="") as filew:
                    writer = csv.DictWriter(filew, fieldnames=["first","last","house"])
                    writer.writeheader()
                    for row in reader:
                        row["first"] = row.pop("name")             
                        last_name, first_name = row["first"].split(", ")
                        row["first"] = first_name
                        row["last"] = last_name
                        writer.writerow(row)  
        except FileNotFoundError:
             sys.exit(f"Could not read {sys.argv[1]}")
if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
if len(sys.argv) == 4:
    sys.exit("Too many command-line arguments")