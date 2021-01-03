'''
This is a Python implementation of Percolation problem
from Princeton "Algorithms, Part 1" course:
https://www.coursera.org/learn/algorithms-part1/

Important Note: I wrote this code having no idea about time complexity.
I'll probably alter it later on when I know more about it.
Feedback would be greatly appreciated!
'''

from random import randint

class Percolation(object):

    # creates n-by-n grid, with all sites initially blocked
    def __init__(self, n):
        self._num = n
        self._num_open = 0
        self._top_id = []
        self._bottom_id = []
        self._reset()
        
    # reset sys/id arrays and num of open sites in case it was opened before    
    def _reset(self):
        self._sys = [0 for i in range(self._num * self._num)]
        self._id = [i for i in range(self._num * self._num)]
        self._sz = [1] * self._num ** 2
        self._num_open = 0
    
    #get index of element in list by row/col
    def _get_index(self, row, col):
        return(col + self._num * row)
    
    #finds the root of the site
    def _root(self, i): # id[i]
        while(i != self._id[i]):
            self._id[i] = self._id[self._id[i]]
            i = self._id[i]
        return i         
    
    #establishes union between two neighboring open sites
    def _union(self, p, q):
        i = self._root(p)
        j = self._root(q)
        if i == j:
            pass
        elif(self._sz[i] <= self._sz[j]):
            self._id[i] = j
            self._sz[j] += self._sz[i]
        else:
            self._id[j] = i
            self._sz[i] += self._sz[j]
        pass
    
    #is one site connected to the other?
    def isConnected(self, row1, col1, row2, col2):
        p = self._get_index(row1, col1)
        q = self._get_index(row2, col2)
        return self._root(p) == self._root(q)
                
    # is the site (row, col) open?
    def isOpen(self, row, col):
        i = self._get_index(row, col)
        return self._sys[i] == 1
    
    # opens the site (row, col) if it is not open already
    def open(self, row, col):
        i = self._get_index(row, col)
        if (self._sys[i] == 0):
            self._sys[i] = randint(0, 1)
            # adding count to a new open site
            if self._sys[i] == 1:
                self._num_open += 1
        # establishing union with neighboring sites (left and top)
        if self.isOpen(row, col) and self.isOpen(row-1, col):
            if row != 0:
                self._union(i, i-self._num)
            else: pass
        if self.isOpen(row, col) and self.isOpen(row, col-1):
            if col != 0:
                self._union(i, i-1)
            else: pass
    
    # opens all sites in the system one by one
    def open_all(self):       
        self._reset()
        [self.open(i, j) for i in range(self._num)
                        for j in range(self._num)]
        self.plot_all()
                
    # is the site (row, col) full?
    def isFull(self, row, col):
        i = self._get_index(row, col)
        return self._id[i] in self._top_id

    # returns the number of open sites
    def numberOfOpenSites(self):
        return self._num_open

    # does the system percolate?
    def percolates(self):
        self._top_id = self._id[:self._num]
        self._bottom_id = self._id[-self._num:]
        for i in self._bottom_id:
            if i in self._top_id:
                return True
            else: continue
        return False
    
    #plots system and id matrices
    def plot_all(self):
        def plot(lst):
            for i in range(0, len(self._sz), self._num):
                x = i
                print (lst[x : x+self._num])              
        print("System:")
        plot(self._sys)        
        print("\nId matrix:")
        plot(self._id)

size = 10
pc = Percolation(size)
pc.open_all()
print(pc.percolates())
print(pc.numberOfOpenSites())