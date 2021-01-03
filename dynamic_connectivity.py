'''
This is a Python implementation of Dynamic Connectivity Algorithm
explained in Princeton "Algorithms, Parth 1" course:
https://www.coursera.org/learn/algorithms-part1/
'''

class UnionFind(object):
    def __init__(self, n):
        self._id = list(range(10))
        self._sz = [1] * n
        self._indexes = [i for i in range(n)]
        
    def plot(self):
        print("i   ", self._indexes)
        print("id  ", self._id)
        print("size", self._sz)
        
    def _root(self, i):
        while(i != self._id[i]):
            self._id[i] = self._id[self._id[i]]
            i = self._id[i]
        return i

    def find(self, p, q):
        return self._root(p) == self._root(q)

    def union(self, p, q):
        i = self._root(p)
        j = self._root(q)
        if i == j:
            pass
        elif(self._sz[i] < self._sz[j]):
            self._id[i] = j
            self._sz[j] += self._sz[i]
        else:
            self._id[j] = i
            self._sz[i] += self._sz[j]
        self.plot()