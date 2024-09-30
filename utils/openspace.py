from utils.table import Table
import random
import pandas as pd

class Openspace:
    '''class openspace takes arguments for number of table and number of seats. Created list 
    of table and Table object is created with the specified number of seats (seats_of_table).
    This object is then added to the self.tables list. '''
    def __init__(self,number_of_tables,seats_of_table):
        self.tables= []
        for i in range(number_of_tables):
            self.tables.append(Table(seats_of_table))

    ''' Method to organize the seating.Randomly shuffles the list of names.Loops through each 
    name in the shuffled list.Loops through each table to find a free spot.If a free spot is 
    found, assigns the name to that seat and breaks out of the loop.'''  
    def organize(self,names):
        random.shuffle(names)
        for name in names:
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    break
        
                
    '''Method to display the seating arrangement.Loops through the tables with their indexes.
        Prints the table number.Loops through each seat in the current table.Select the occupant
        or marks the seat as "Empty". Prints the occupant's name or "Empty".'''
    def display(self):
        for i, table in enumerate(self.tables):
            print(f"Table {i + 1}:")
            for seat in table.seats:
                if seat.free:
                    occupant = "Empty"
                else:
                    occupant = seat.occupant
                print(f"  Seat: {occupant}")
            print("Team Leader: ", seat.occupant)
            #print(random.choice())
            print()
    

        

    '''Method for storing ouput in excel file. It takes filename as parameter.This checks if 
    the seat is free it will assign empty else it will assign occupant name for seat.'''
    def store(self, filename):
        data = []     #This list will be used to collect information about each seat in each table.
        for i, table in enumerate(self.tables): # This loop iterates over self.tables, which contains the Table objects
            for seat in table.seats:   #This nested loop goes through each seat in the current table.
                if seat.free:
                    occupant= "Empty"
                else:
                    occupant =seat.occupant
                data.append({'Table': i + 1, 'Seat': occupant})
        ''' This creates a dictionary with the current table number (i + 1, to start counting 
        from 1 instead of 0) and the occupant status. This dictionary is then appended to the 
        data list.'''

        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
'''After collecting all the seat information, a pandas DataFrame (df) is created from the 
data list. This organizes the data into a tabular format.And saves the DataFrame to an Excel 
file with the specified filename. The index=False argument ensures that the row indices are 
not written to the Excel file.'''

