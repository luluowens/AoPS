class Map(object):
    def __init__(self, L1, L2):
        """ L1 is a list of unique int elements
            L2 is a list of unique lowercase str elements
            
            Creates two data attributes. 
            * map, a dict data attribute where the keys are each int in 
              L1 and the value associate with a key is the sorted list 
              of all words in L2 whose length equals that key. 
      
            * unused_list, a list data attribute containing elements in 
              L2 whose length do not equal any of the int values in L1. 
              Elements are sorted in lexicographical order. """
        self.map = {}
        unsorted_map = {}
        self.unused_list = []
        L1.sort()
        
        for element in L2 :
            length = len(element)
            if length not in L1 :
                self.unused_list.append(element)
            else :
                if length not in unsorted_map :
                    unsorted_map[length] = [element]
                else :
                    unsorted_map[length].append(element)
        
        for key in unsorted_map :
            unsorted_map[key].sort()

        for integer in L1 :
            if integer not in unsorted_map :
                self.map[integer] = []
            else :
                self.map[integer] = unsorted_map[integer]
        
        self.unused_list.sort()

    def get_map(self):
        """ Returns a copy of the map of ints to list of strings. """
        return self.map.copy()

    def get_unused_list(self):
        """ Returns a copy of the list of unused strings. """
        return self.unused_list.copy()
    
    def __add__(self, other):
        """ Returns a new Map object whose map data attribute is a merge
        of self and other's maps. When merging, if self and other have 
        the same key, raise a ValueError. Otherwise, the new Map object's 
        map data attribute is all the keys in self and other along with 
        the keys' values. The new Map object's unused_list data attribute 
        is the sorted unique elements from the unused_lists of self and 
        other that are not in the new Map's map. """
        other_map = other.get_map()
        other_unused = other.get_unused_list()
        new_map = Map([], [])
        
        for key in self.map :
            if key in other_map :
                raise ValueError("Both maps have a shared key!")
            else :
                new_map.map[key] = self.map[key]
        
        for other_key in other_map :
            new_map.map[other_key] = other_map[other_key]
        
        values = new_map.map.values()
        all_values = [element for value in values for element in value]

        for element in self.unused_list :
            if element not in all_values :
                new_map.unused_list.append(element)
        
        for element in other_unused :
            if element not in all_values :
                new_map.unused_list.append(element)

        return new_map



# testing
a = Map([1,2,3], ["abc", "def", 'z', 'nmop'])
print(a.get_map())  # prints {1: ['z'], 2: [], 3: ['abc', 'def']}
print(a.get_unused_list())  # ['nmop']


b = Map([4], ["abc", "xyz", 'z', 'nmop', 'abcd'])
c = a+b
print(c.get_map())  # prints {1: ['z'], 2: [], 3: ['abc', 'def'], 4: ['abcd', 'nmop']}
print(c.get_unused_list())  # prints ['xyz']