import re
import json
import sys
from difflib import *
with open("exp.txt") as f:
    e1 = f.readlines()
with open("ref.txt") as f:
    r1 = f.readlines()
for line in unified_diff(e1, r1):
    sys.stdout.write(line)

s = SequenceMatcher(None, e1, r1)
m = s.find_longest_match(0, len(e1), 0, len(r1))
print(m)
b = s.get_matching_blocks()
print(b)

class CollectionHashableIterable:
    def __init__(self, l1):
        self.l1 = l1[slice(1,3)]
        self.str = ";".join(self.l1)
    def __iter__(self):
        return self.str.__iter__()
    def next(self):
        return self.l1.next()
    def __next__(self):
        return self.l1.__next__()
    def __hash__(self):
        return self.str.__hash__()
    def __repr__(self):
        return self.str.__repr__()
        #return self.str.__repr__()
    
#CollectionHashableIterable.__eq__ = lambda self,other : str(self) == str(other)
#CollectionHashableIterable.__str__ = lambda self : str(self)
#https://stackoverflow.com/questions/24527961/how-to-use-a-list-of-strings-which-may-contain-any-character-as-keys
#if the order matters, use tuple: 
#If the order must not matter, use frozenset: 
print("NOW ignore junk")
le1 = [ line.split(";")[2].rstrip("\n")  for line in e1 ]
lr1 = [ line.split(";")[2].rstrip("\n")  for line in r1 ]
#le1 = [ CollectionHashableIterable(line.split(";"))  for line in e1 ]
#lr1 = [ CollectionHashableIterable(line.split(";"))  for line in r1 ]
print(le1)
print(lr1)
#le1.__hash__ = funcBookHash
#lr1.__hash__ = funcBookHash

IsJunk = lambda x : re.match("^\[.*\]$", str(x)) is not None
sliceRef1 = slice(0, len(lr1))
print("Next sliceRef1: {}".format(sliceRef1))
for sliceExp1 in [slice(0,2), slice(2, 5), slice(5,len(le1))]:
    se1=le1[sliceExp1]
    sr1=lr1[sliceRef1]
    #smatcher = SequenceMatcher(None, se1, sr1, autojunk = False)
    smatcher = SequenceMatcher(IsJunk, se1, sr1, autojunk = False)
    m2 = smatcher.find_longest_match(0, len(se1), 0, len(sr1))
    print(m2)
    b2 = smatcher.get_matching_blocks()
    print(b2)
    
    lastMatch = None
    for match in b2:
        #Dump out all mismatch since the last match
        misBase = 0 if not lastMatch else lastMatch.a + lastMatch.size
        mismatchSlice = slice(misBase,  match.a)
        for index in range(mismatchSlice.start, mismatchSlice.stop):
            print("***{:d}: {}".format(sliceExp1.start + index, se1[index]))
        if not match.size: continue
        for index in range(0, match.size):
            print("{:d}: {}".format(sliceExp1.start + match.a + index, "=".join([se1[match.a + index], sr1[match.b + index]])))
        lastMatch = match
    sliceRef1 = slice(sliceRef1.start + lastMatch.b + lastMatch.size, len(lr1)) if lastMatch else sliceRef1
    print("Next sliceRef1: {}".format(sliceRef1))
