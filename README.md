#  Array manipulation

Here is a simple manipulation to do some common array manipulation.  
Since cairo is memory immutable (once you write the value if a memory cell, this cell cannot  change anymore), each method changing the order, adding an item at a specific index, will result in a new array.   
Which is why I chose to standardise  this behavior by  always returning two elements the length of the new  array and the new array (arr_len, arr) even when it is not useful.  
Here is everything you can do:  
1. Creating an empty array
2. Adding
    * Adding at the end
    * Adding at  first position 
    * Adding at a specific index
3. Removing
    * Remove last 
    * Remove first
    * Remove at a specific index
    * All occurences of
4. Splice
5. Finding
    * index of
    * min
    * max
6. Counting occurences of 
7. Sorting
8. Replace 
9. Reverse 
10. Joining 2 arrays 

/!\ signal some might throw an exception!

## TODO
Flatten?  
Support of structure in a generic way?


Don't hesitate to request me any feature that could be missing