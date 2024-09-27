from utils.table import Table
import random

class Openspace:

    def __init__(self,number_of_tables,seats_of_table):
        self.tables= []
        for i in range(number_of_tables):
            self.tables.append(Table(seats_of_table))
       
    def organize(self,names):
        random.shuffle(names)
        for name in names:
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    break

    def display(self):
        pass

    def store(filename):
        pass


