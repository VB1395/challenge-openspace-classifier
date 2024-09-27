class Seat:
    '''The class seat containing '''
    def __init__(self):
        self.free= True
        self.occupant= None
    
    def set_occupant(self,name):
        if self.free:
            self.occupant= name
            self.free = False
            
    def remove_occupant(self):
        name= self.occupant
        self.free= True
        self.occupant=None  
        return name     


    def __str__(self):
        return f'{self.occupant} occupying the seat before'
    

class Table:
    def __init__(self,capacity):
        self.capacity= 4
        self.seats=[]
        for i in range(capacity):
            self.seats.append(Seat())
      
    def has_free_spot(self):
        for i in self.seats:
            if i.free:
                return True
        return False
        

    def assign_seat(self,name):
        for t in self.seats:
            if t.free:
                t.set_occupant(name)
                return True
        return False

    def left_capacity(self):
        count= 0
        for s in self.seats:
            if s.free:
                count +=1
            
        return count

    def __str__(self):
        "Created table for 4 seats."
       

# Testing the Table and Seat classes
if __name__ == "__main__":
    table = Table(4)  # Create a table with 4 seats

    # Display initial state
    print("Initial seating:")
    for i in range(len(table.seats)):
        if table.seats[i].occupant:
            print(f"Seat {i + 1}: {table.seats[i].occupant}")
        else:
            print(f"Seat {i + 1}: Empty")

    # Assign seats
    table.assign_seat("Alice")
    table.assign_seat("Bob")

    # Display state after assigning
    print("\nSeating after assigning Alice and Bob:")
    for i in range(len(table.seats)):
        if table.seats[i].occupant:
            print(f"Seat {i + 1}: {table.seats[i].occupant}")
        else:
            print(f"Seat {i + 1}: Empty")

    # Remove an occupant
    table.seats[0].remove_occupant()  # Remove Alice

    # Display final state
    print("\nSeating after removing Alice:")
    for i in range(len(table.seats)):
        if table.seats[i].occupant:
            print(f"Seat {i + 1}: {table.seats[i].occupant}")
        else:
            print(f"Seat {i + 1}: Empty")
