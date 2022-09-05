from __future__ import annotations
import math
from dataclasses import dataclass
from typing import Union, Callable

# We don't include complex numbers
# in our Numeric data type for simplicity's
# sake
Numeric = Union[int, float]

@dataclass
class ValueRange:
    minvalue: Numeric
    maxvalue: Numeric
        
    left : ValueRange = None
    right : ValueRange = None
        
    def __iter__(self):
        yield self
        if self.left is not None:
            for elem in self.left:
                yield elem
        if self.right is not None:
            for elem in self.right:
                yield elem
                
    def _range(self):
        return self.maxvalue - self.minvalue
    
    def __eq__(self, other: ValueRange):
        return self._range() == other._range()
    
    def __lt__(self, other: ValueRange):
        return self._range() < other._range()
    
    def __le__(self, other: ValueRange):
        return self._range() <= other._range()
    
    def __gt__(self, other: ValueRange):
        return self._range() > other._range()
    
    def __ge__(self, other: ValueRange):
        return self._range() >= other._range()

def build_tree(val_range: ValueRange, floor_range: Numeric) -> ValueRange:
    """
    Builds a binary tree partition starting from the val_range
    value range root. The floor_range sets the minimum range upon
    reaching which we form a leaf and abandon the current branch.

    Returns a ValueRange object, representing a binary tree.
    """

    minval, maxval = val_range.minvalue, val_range.maxvalue
    
    floors = ((maxval - minval) // 2) / floor_range
    if floors < 1:
        return val_range
    
    midval = minval + math.floor(floors)*floor_range
    val_range.left = build_tree(ValueRange(minval, midval), floor_range)
    val_range.right = build_tree(ValueRange(midval, maxval), floor_range)
    
    return val_range


def walk(val_range: ValueRange, fun: Callable[[ValueRange], bool]):
    """
    Walks the binary tree starting at val_range ValueRange node.

    The fun argument is a callable that can be used to terminate the walk
    by returning False. Since fun receives the current node when being called
    it can be used to check some conditions, filter nodes, etc, using side effects.
    """
    if not fun(val_range):
        return
    if val_range.left is not None:
        walk(val_range.left, fun)
    if val_range.right is not None:
        walk(val_range.right, fun)
