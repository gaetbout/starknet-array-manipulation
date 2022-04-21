#  Array manipulation

Here is a simple manipulation to do some common array manipulation.  
Since cairo is memory immutable (once you write the value if a memory cell, this cell cannot  change anymore), each method changing the order, adding an item at a specific index, will result in a new array. So you can see each method as a copy method with some more extra logic.
Which is why I chose to standardise  this behavior by  always returning two elements the length of the new  array and the new array (arr_len, arr) even when it is not useful.  
Here is everything you can do:  

1. Creation
    * get_new_array() -> (arr_len : felt, arr : felt*): Creating an new empty array  
2. Adding: All are O(N) complexity
    * add_last(arr_len : felt, arr : felt*, item : felt) -> (arr_len : felt, arr : felt*): Adding at the last position  
    * add_first(arr_len : felt, arr : felt*, item : felt) -> (arr_len : felt, arr : felt*): Adding at the first position  
    * add_at(arr_len : felt, arr : felt*, index : felt, item : felt) -> (arr_len : felt, arr : felt*): Adding at a specific index  
3. Removing: All are O(N) complexity
    * remove_last(arr_len : felt, arr : felt*) -> (arr_len : felt, arr : felt*): Remove last 
    * remove_first(arr_len : felt, arr : felt*) -> (arr_len : felt, arr : felt*): Remove first
    * remove_at(arr_len : felt, arr : felt*, index : felt) -> (arr_len : felt, arr : felt*): Remove at a specific index
4. Searching: All are O(N) complexity
    * contains(arr_len : felt, arr : felt*, item : felt) -> (contains : felt): Contains item
    * index_of(arr_len : felt, arr : felt*, item : felt) -> (index : felt): Index of item
    * min(arr_len : felt, arr : felt*) -> (min : felt): Returns the min value of the array
    * max(arr_len : felt, arr : felt*) -> (max : felt): Returns the max value of the array
    * Counting occurrences of 
5. Sorting
6. Replace 
7. Reverse 
8. Joining 2 arrays 

/!\ signal some might throw an exception!

## TODO
 - Removing 
    * All occurences of
    * First occurence of
    * Last occurence of 
 - Searching
    * Index of min
    * index of max
 - Flatten?  
 - Support of structure in a generic way?
 - Copy from to 

Make an interface?
Don't hesitate to request me any feature that could be missing