#  Array

Here is a simple lib to do some common array operations.  
Since cairo is memory immutable (once you write the value in a memory cell, this cell cannot  change anymore), each function requiring any memory change, will create a new array. So you can see each method as a copy method with some more extra logic.
Which is why I chose to standardise  this behavior by  always returning two elements the length of the new  array and the new array (arr_len, arr) even when it is not useful.  
Here is everything you can do:  

This library is divided in two files (so far).  
One is for actual array manipulation that will then create a new array as a response. While the other should just return a response but not affect the state of memory. 

## Array manipulation
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

## Array searching
4. Searching: All are O(N) complexity
    * contains(arr_len : felt, arr : felt*, item : felt) -> (contains : felt): Contains item
    * index_of(arr_len : felt, arr : felt*, item : felt) -> (index : felt): Index of the item or -1 if not (felt equivalent ==> 3618502788666131213697322783095070105623107215331596699973092056135872020480)
    * min(arr_len : felt, arr : felt*) -> (min : felt): Returns the min value of the array  
    Can throw an error when array empty
    * max(arr_len : felt, arr : felt*) -> (max : felt): Returns the max value of the array  
    Can throw an error when array empty
    * index_of_max(arr_len : felt, arr : felt*) -> (index : felt): Returns the index of the max value of the array  
    Can throw an error when array empty
    * index_of_min(arr_len : felt, arr : felt*) -> (index : felt): Returns the index of the min value of the array  
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
 - Flatten?  
 - Support of structure in a generic way?
 - Copy from to 

Make an interface?  
Make a better look   
Don't hesitate to request me any feature that could be missing