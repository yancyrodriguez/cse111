import csv

def main():
    products_dict = read_dict("products.csv", 0)
    print(products_dict)

    with open("request.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

    
        REQUESTED_PRODUCT_INDEX = 0
        REQUESTED_QUANTITY_INDEX = 1

    
        PRODUCT_NAME_INDEX = 1
        PRODUCT_COST_INDEX = 2
        for row_list in reader:
            requested_product_number = row_list[REQUESTED_PRODUCT_INDEX]
            requested_quantity = row_list[REQUESTED_QUANTITY_INDEX]

            for key, product in products_dict.items():
                name = product[PRODUCT_NAME_INDEX]
                cost = product[PRODUCT_COST_INDEX]
                final_cost = float(cost) * float(requested_quantity)
                if requested_product_number == key:
                    print(
                        f"Item: {name}, Quantity: {requested_quantity}, Price: ${cost}")


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
   
    dictionary = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:

            key = row_list[key_column_index]
            price = row_list[2]

            dictionary[key] = row_list

    return dictionary

if __name__ == "__main__":
    main()