import csv

NUMBER_INDEX = 0
NAME_INDEX = 1

def main():
    try:
        file_name = "students.csv"

        number = input("Please enter an I-number:")

        number = number.replace("-", "")

        if number.isdigit() == False:
            print()
            print("Invalid I-number")
        elif len(number) < 9:
            print()
            print("Invalid I-Number: too few digits")
        elif len(number) > 9:
            print()
            print("Invalid I-Number: too many digits")
       
 
        students_dict = read_dictionary(file_name, NUMBER_INDEX)
 
 
        value = students_dict[number]
       
        name = value[NAME_INDEX]
 
        print(name)
 
    except KeyError as key_err:
        print()
        print("No such student")
 

 
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
        dictionary and return the dictionary.
   
        Parameters
            filename: the name of the CSV file to read.
            key_column_index: the index of the column
                to use as the keys in the dictionary.
        Return: a compound dictionary that contains
            the contents of the CSV file.
    """
    students_dict = {}
 
    with open(filename, "rt") as csv_file:
     
        reader = csv.reader(csv_file)
 
        next(reader)
 
        for line in reader:
            if len(line) != 0:
                key = line[key_column_index]
                students_dict[key] = line
    return students_dict
 
if __name__ == "__main__":
    main()