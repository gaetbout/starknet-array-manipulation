#  Array manipulation

Here is a simple manipulation to do some common array manipulation.  
Since cairo is memory immutable (once you write the value if a memory cell, this cell cannot  change anymore), each method changing the order, adding an item at a specific index, will result in a new array. So you can see each method as a copy method with some more extra logic.
Which is why I chose to standardise  this behavior by  always returning two elements the length of the new  array and the new array (arr_len, arr) even when it is not useful.  
Here is everything you can do:  

1. Creation
    * get_new_array() -> (arr_len : felt, arr : felt*): Creating an new empty array  
2. Adding: All are O(N) complexity
    * add_last(arr_len : felt, arr : felt*, item : felt) -> (arr_len : felt, arr : felt*): Adding at the last position  
     ⚠️ If you still have access to the array, and the memory isn't bounded already, please just do:  
     arr[arr_len] = item, it'll avoid the creation of a new array
    * add_first(arr_len : felt, arr : felt*, item : felt) -> (arr_len : felt, arr : felt*): Adding at the first position  
    * add_at(arr_len : felt, arr : felt*, index : felt, item : felt) -> (arr_len : felt, arr : felt*): Adding at a specific index  
3. Removing: All are O(N) complexity
    * remove_last(arr_len : felt, arr : felt*) -> (arr_len : felt, arr : felt*): Remove last 
    * remove_first(arr_len : felt, arr : felt*) -> (arr_len : felt, arr : felt*): Remove first
    * remove_at(arr_len : felt, arr : felt*, index : felt) -> (arr_len : felt, arr : felt*): Remove at a specific index
4. Searching: All are O(N) complexity
    * contains(arr_len : felt, arr : felt*, item : felt) -> (contains : felt): Contains item
    * index_of(arr_len : felt, arr : felt*, item : felt) -> (index : felt): Index of the item or -1 if not (felt equivalent ==> 3618502788666131213697322783095070105623107215331596699973092056135872020480)
    * min(arr_len : felt, arr : felt*) -> (min : felt): Returns the min value of the array  
    Can throw an error when array empty
    * max(arr_len : felt, arr : felt*) -> (max : felt): Returns the max value of the array  
    Can throw an error when array empty
    * index_of_max(arr_len : felt, arr : felt*) -> (index : felt): Returns the index of the max value of the array  
    Can throw an error when array empty
    * occurrences_of(arr_len : felt, arr : felt*, item : felt) -> (occurrences : felt): Counting occurrences of item
5. sort(arr_len : felt, arr : felt*) -> (arr_len : felt, arr : felt*): Sorting  
O(N log(n))  
From max to min
6. Replace 
7. reverse(arr_len : felt, arr : felt*) -> (arr_len : felt, arr : felt*): Reverse an array
8. Joining 2 arrays 

/!\ signal some might throw an exception!

## TODO
⚠️ USE OF MEMCPY  
⚠️ SPLIT INTO DIFFERENT FILES
 - Removing 
    * All occurences of
    * First occurence of
    * Last occurence of 
 - Searching
    * Index of min
 - Flatten?  
 - Support of structure in a generic way?
 - Copy from to 

Make an interface?  
Make a better look   
Don't hesitate to request me any feature that could be missing