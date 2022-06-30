import pandas as pd
import random

def create_dataset():

    # Creates a dataframe based on excel file informed by the user
    file_name = input('Insert the file name in excel format:')
    df = pd.read_excel(file_name)

    # Gets the list of relevant columns and split the columns into a list of strings
    columns = input('Inform the column names to be used (separate each column by comma)')
    list_columns = columns.split(",")

    # Gets the number of rows
    number_rows = int(input('Inform the number of rows the table needs to have'))

    # Gets the data from the df based on the columns
    my_dict = {}
    for col in list_columns:
        col = col.strip()
        my_dict[col] = [cell for cell in df[col].tolist() if cell != None or pd.isna(cell) == False]

    # Gets distinct values from these columns
    for key in my_dict:
        my_dict[key] = list(set(my_dict[key]))

    # Creates the dataframe with random values based on this data
    for key in my_dict:
        my_dict[key] = [ my_dict[key][random.randint(0, len(my_dict[key]) -1 )] for i in range(number_rows) ]

    new_df = pd.DataFrame(my_dict)

    # Creates excel file
    new_df.to_excel('fake_dataset.xlsx', sheet_name='sheet1', index=False)

create_dataset()