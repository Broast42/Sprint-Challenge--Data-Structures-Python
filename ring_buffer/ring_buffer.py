class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_entries = 0
        self.entries = []
        self.current_index = 0
        

    def append(self, item):
        #if current_capacity is equal to limit
        if self.current_entries == self.capacity:
            if self.current_index == self.capacity:
                self.current_index = 0
            #remove the first item in the list
            self.entries.pop(self.current_index)
            #add item to 0 index of list overwiting oldest entry
            self.entries.insert(self.current_index, item)
            self.current_index +=1
        #else append item to list 
        else:
            self.entries.append(item)
            self.current_entries +=1
        

    def get(self):
        #return list of entries
        return self.entries
        