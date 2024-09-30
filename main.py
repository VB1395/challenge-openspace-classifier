import pandas as pd   #Imports the pandas library for handling CSV files.
from utils.openspace import Openspace  # Adjusted import statement

# Utility function to read names from a CSV file
'''Defines a function to read names from a CSV file. Attempts to read the CSV file into a 
DataFrame. Returns a list of names from the 'Name' column. Handles exceptions and prints 
an error message if reading fails, returning an empty list.'''
def read_names_from_csv(filepath):
    try:
        df = pd.read_csv(filepath)
        return df['Name'].tolist()
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return []

if __name__ == "__main__":   #Checks if the script is run as the main program.
    input_filepath = "utils/new_colleagues.csv"  # Path to the CSV file
    output_filename = "output.xlsx"  #Output file name

    # Create a list that contains all the colleagues' names
    names = read_names_from_csv(input_filepath)  #Calls the function to read names from the CSV.

    # Create an OpenSpace
    open_space = Openspace(6,4)

    # Assign colleagues randomly to a table
    open_space.organize(names)

    # Store output in file name output.xlsx
    open_space.store(output_filename)

    # Display assignments in the terminal
    open_space.display()
