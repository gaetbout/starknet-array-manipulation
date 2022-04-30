#  Array

Here is a simple lib to do some common array operations.  
Since cairo is memory immutable (once you write the value in a memory cell, this cell cannot  change anymore), each function requiring any memory change, will create a new array. So you can see each method as a copy method with some more extra logic.
Which is why I chose to standardise  this behavior by  always returning two elements the length of the new  array and the new array (arr_len, arr) even when it is not useful.  
Here is everything you can do:  

This library is divided in two files (so far).  
Whenever the support for passing and returning structure is there, it  should be updated.

## Array manipulation

This file will always have to create a new array to return.  
Unless specified, these methods are all in O(N) complexity.  
All these methods are returning the same values 
**(arr_len : felt, arr : felt*):**  

| Function | Arguments |
| ------ | ----------- |
| add_last | (arr_len : felt, arr : felt*, item : felt) |
| add_first | (arr_len : felt, arr : felt*, item : felt)  |
| add_at | (arr_len : felt, arr : felt*, index : felt, item : felt) |
| remove_last | (arr_len : felt, arr : felt*) |
| remove_first | (arr_len : felt, arr : felt*) |
| remove_at | (arr_len : felt, arr : felt*, index : felt) |
| sort | (arr_len : felt, arr : felt*) |
| reverse | (arr_len : felt, arr : felt*) |

⚠️ Some remark(s):   
> For add_last, if you still have access to the array, and the memory isn't bounded already, please just do:  
 `arr[arr_len] = item`  
 it'll avoid the creation of a new array

> The sort method has a complexity of O(N(log(n)))

## Array searching
This consists of a bunch of function that of for puprose to go through the array and return what is asked.  
Unless specified, these methods are all in O(N) complexity.  


| Function | Arguments | Return |
| ------ | ----------- | ------ | 
| contains | (arr_len : felt, arr : felt*, item : felt) | (contains : felt) | 
| index_of | (arr_len : felt, arr : felt*, item : felt) | (index : felt) | 
| min | (arr_len : felt, arr : felt*) | (min : felt) | 
| index_of_min | (arr_len : felt, arr : felt*) | (index : felt) | 
| max | (arr_len : felt, arr : felt*) | (max : felt) |
| index_of_max | (arr_len : felt, arr : felt*) | (index : felt) |
| occurrences_of | (arr_len : felt, arr : felt*, item : felt) | (occurrences : felt) |

⚠️ Some remark(s):   
> index_of if  not found will return 3618502788666131213697322783095070105623107215331596699973092056135872020480 which is -1 in felt

> min, index_of_min, max, index_of_max will throw an error if the array is empty

## TODO

 - Removing 
    * All occurences of
    * First occurence of
    * Last occurence of 
 - Flatten?  
 - Support of structure in a generic way?
 - Copy from to 
 - Replace 
 - Joining 2 arrays 

Don't hesitate to request me any feature that could be missing or ping me when there is the support for structure