# binrange

Partition a value range into a binary tree down to a specified minimum range.

The following produces a binary tree for the range of values between 0 and 10 billion, 
with the smallest subrange equal to 100 000:

```
from binrange import ValueRange, build_tree

tree = build_tree(ValueRange(0, 10e+9), 100e+3)
```

A simple walk function is provided for traversing the tree top down. It accepts
a callable as second argument. The callable receives the ValueRange at the current
node and can stop the walk by returning False, thus preventing exploration of this 
node's descendants. Conversely, it should return True to continue down from the
current node.
