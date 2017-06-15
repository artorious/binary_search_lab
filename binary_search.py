
class BinarySearch(list):

    def __init__(self, length, step):
        """takes two integers as parameters, *length* of the 
        list to be created and  the *step* or difference between 
        consecutive values
        
        initializes an instance variablelength, that returns the 
        number of elements in the array"""
        
        # init super class
        super(BinarySearch, self).__init__()

        # Populate class
        for element in range(1, length + 1):
            self.append(element * step)

        # init length attribute
        self.length = len(self)
        
    def search(self, the_value ):
        """Method takes one argument which is the *the_value* to locate through
        a binary search. 
        
        Return a dictionary object e.g {'count': int, 'index': int} 
        The *count * key is number of times the binary search function iterated 
        to find the *index* key, which represents the position of the value.
        """
        # Init counter, first and last indices
        counter = 0
        first_index = 0
        last_index = len(self) - 1
        value_index = 0
        located = False
        
        # Check for *the_value* at *first_index* and *last_index*
        if the_value == self[first_index]:
            value_index = first_index
            located = True
        elif the_value == self[last_index]:
            value_index = last_index
            located = True

        # Check for *the_value* in the list
        if the_value not in self:
            located = True
            value_index = -1

        # Binary search
        while first_index <= last_index and not located:
            mid_range = (first_index + last_index) // 2
            if self[mid_range] == the_value:
                located = True
                value_index = mid_range
            else:
                counter += 1 # Counter update with each iteration
                if the_value < self[mid_range]:
                    last_index = mid_range - 1
                else: # if the_value > self[mid_range]
                    first_index = mid_range + 1
        return {'count': counter, 'index': value_index} 
