class Seat:
    '''The constructor method initializes each seat object. 
    Sets seat to true for indicating seat is empty. containg empty string for occupant 
    meaning there is no one in seat.'''
 
    def __init__(self):
        self.free= True
        self.occupant= " "

    '''Method to assign a name to the seat.cheks if seat is free it will Assigns the name to
    occupant and sets free to False'''
    def set_occupant(self,name): 
        if self.free:
            self.occupant= name
            self.free = False

    '''This method is for remove the occupant from seat.it will check occupant name
        in seat and set free is true. and its returning name for occpant. 
        seat is free(True)'''      
    def remove_occupant(self):
        name = self.occupant
        self.occupant = " "
        self.free = True
        return name     

    '''It will return name for who is occupying seat before.'''
    def __str__(self):
        return f'{self.occupant} occupying the seat before'
    

class Table:
    ''' Table class initalise constructor capacity and crate list of seats based on capacity.'''
    def __init__(self,capacity):
        self.capacity= capacity
        self.seats=[]
        for i in range(capacity):
            self.seats.append(Seat())
    
    '''This method cheks for free spot. It will return true otherwise false'''  
    def has_free_spot(self):
        for i in self.seats:
            if i.free:
                return True
        return False
        
    '''This method is for assiging seats to occupants.Loops through each seat in the table.
    Its checking if seat is available if yes, it will return True otherwise false.'''
    def assign_seat(self,name):
        for t in self.seats:
            if t.free:
                t.set_occupant(name)
                return True
        return False
    
    '''Method used to count the number of free seats.'''
    def left_capacity(self):
        count= 0
        for s in self.seats:
            if s.free:
                count +=1
            
        return count

    def __str__(self):
        return f"Created table for {self.capacity} seats."
