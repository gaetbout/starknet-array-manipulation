![Tests](https://github.com/gaetbout/starknet-array-manipulation/actions/workflows/python-app.yml/badge.svg)

Here is a simple lib to do some common array operations.  
Since cairo is memory immutable (once you write the value in a memory cell, this cell cannot change anymore), each function requiring any memory change, will create a new array. So you can see each function as a copy function with some more extra logic.  

This library is divided multiple parts.
Here is everything you can do:  

# Array manipulation

These functions will always have to create a new array to be returned.  
All these functions are returning the same values  
`(arr_len : felt, arr : felt*):`  
| Function | Arguments |
| ------ | ----------- | 
| [add_first](#add_first) | (arr_len : felt, arr : felt*, item : felt)  |
| [add_last](#add_last)| (arr_len : felt, arr : felt*, item : felt) |
| [add_at](#add_at) | (arr_len : felt, arr : felt*, index : felt, item : felt) |
| [remove_first](#remove_first) | (arr_len : felt, arr : felt*) |
| [remove_last](#remove_last) | (arr_len : felt, arr : felt*) |
| [remove_at](#remove_at) | (arr_len : felt, arr : felt*, index : felt) |
| [remove_first_occurence_of](#remove_first_occurence_of) | (arr_len : felt, arr : felt*, item : felt) |
| [remove_last_occurence_of](#remove_last_occurence_of) | (arr_len : felt, arr : felt*, item : felt) |
| [remove_all_occurences_of](#remove_all_occurences_of) | (arr_len : felt, arr : felt*, item : felt) |
| [sort](#sort) | (arr_len : felt, arr : felt*) |
| [reverse](#reverse) | (arr_len : felt, arr : felt*) |
| [join](#join) | (arr1_len : felt, arr1 : felt*, arr2_len : felt, arr2 : felt*) |
| [copy_from_to](#copy_from_to) | (arr_len : felt, arr : felt*, from_index : felt, to_index : felt) |
| [replace](#replace) | (arr_len : felt, arr : felt*, old_item : felt, new_item : felt) |


# Array searching
These are all the functions that will iterate through the array and return what is asked.
| Function | Arguments | Return |
| ------ | ----------- | ------ | 
| [contains](#contains) | (arr_len : felt, arr : felt*, item : felt) | (contains : felt) | 
| [index_of](#index_of) | (arr_len : felt, arr : felt*, item : felt) | (index : felt) | 
| [min](#min) | (arr_len : felt, arr : felt*) | (min : felt) | 
| [index_of_min](#index_of_min) | (arr_len : felt, arr : felt*) | (index : felt) | 
| [max](#max) | (arr_len : felt, arr : felt*) | (max : felt) |
| [index_of_max](#index_of_max) | (arr_len : felt, arr : felt*) | (index : felt) |
| [occurrences_of](#occurrences_of) | (arr_len : felt, arr : felt*, item : felt) | (occurrences : felt) |



# Tests

*Prerequisite - Have a working cairo environment.*  
To run the test suite, copy this repository and put yourself at the root.  
Compile the contracts using `make build` or `nile compile`.  
Run the tests using `make test` or, for more details, `pytest -v`.   
For more  details check the Actions tab of this GitHub repository.


# TODO
 - Flatten?  
 - Support of structure in a generic way?

**Don't hesitate to request me any feature that could be missing or ping me whenever there is the support for returning structure (with felt\*)**

# Detailed description 

## Array manipulation functions
<a id="add_first"></a>
___
add_first(arr_len : felt, arr : felt*, item : felt) -> (arr_len : felt, arr : felt*)  
___
Creates a new array with the *item* at the first position.  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified  
item - the felt that needs to be added

**Returns:**  
arr_len - the length of the new array  
arr - the new array  

**Complexity:**  
O(N)  
<a id="add_last"></a>
___
add_last(arr_len : felt, arr : felt*, item : felt) -> (arr_len : felt, arr : felt*)  
___
Creates a new array with the *item* at the last position.  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified  
item - the felt that needs to be added

**Returns:**  
arr_len - the length of the new array  
arr - the new array  

**Remark:**  
If you still have access to the array, and the memory isn't bounded already, consider doing:  
 `arr[arr_len] = item`  
 it'll avoid the creation of a new array  

**Complexity:**  
O(N)   
<a id="add_at"></a>
___
add_at(arr_len : felt, arr : felt*, index : felt, item : felt) -> (arr_len : felt, arr : felt*)  
___
Creates a new array with the *item* at the *index* position.  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified
index - the index the *item* needs to be added  
item - the felt that needs to be added

**Returns:**  
arr_len - the length of the new array  
arr - the new array  

**Remark:**  
Will fail if the array is empty or if the index is out of range.

**Complexity:**  
O(N)  
<a id="remove_first"></a>
___
remove_first(arr_len : felt, arr : felt*) -> (arr_len : felt, arr : felt*)  
___ 
Creates a new array without first item.  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified

**Returns:**  
arr_len - the length of the new array  
arr - the new array  

**Remark:**  
Will fail if the array is empty

**Complexity:**  
O(N)  
<a id="remove_last"></a>    
___
remove_last(arr_len : felt, arr : felt*) -> (arr_len : felt, arr : felt*)  
___
Creates a new array without last item.  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified

**Returns:**  
arr_len - the length of the new array  
arr - the new array  

**Remark:**  
Will fail if the array is empty

**Complexity:**  
O(N)  
<a id="remove_at"></a>
___
remove_at(arr_len : felt, arr : felt*, index : felt) -> (arr_len : felt, arr : felt*)  
___
Creates a new array without the item at the position *index*.  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified  
index - the index of the felt that needs to be removed  

**Returns:**  
arr_len - the length of the new array  
arr - the new array  

**Remark:**  
Will fail if the array is empty or if the index is out of range.  

**Complexity:**  
O(N)  
<a id="remove_first_occurence_of"></a>
___
remove_first_occurence_of(arr_len : felt, arr : felt*, item : felt) -> (arr_len : felt, arr : felt*)  
___
Creates a new array without the first occurence of *item*.  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified  
item - the item that needs to be removed  

**Returns:**  
arr_len - the length of the new array  
arr - the new array  

**Remark:**  
Will fail if the array is empty or if the index is out of range.  

**Complexity:**  
O(N)  
<a id="remove_last_occurence_of"></a>
___
remove_last_occurence_of(arr_len : felt, arr : felt*, item : felt) -> (arr_len : felt, arr : felt*)  
___
Creates a new array without the last occurence of *item*.  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified  
item - the item that needs to be removed  

**Returns:**  
arr_len - the length of the new array  
arr - the new array  

**Remark:**  
Will fail if the array is empty.  

**Complexity:**  
O(N)  
<a id="remove_all_occurences_of"></a>
___
remove_all_occurences_of(arr_len : felt, arr : felt*, item : felt) -> (arr_len : felt, arr : felt*)  
___
Creates a new array without all occurences of *item*.  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified  
item - the item that needs to be removed  

**Returns:**  
arr_len - the length of the new array  
arr - the new array  

**Remark:**  
Will fail if the array is empty.  

**Complexity:**  
O(N)  
<a id="sort"></a>
___
sort(arr_len : felt, arr : felt*) -> (arr_len : felt, arr : felt*)  
___
Creates a new array sorted from the biggest felt to the smallest felt.  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified

**Returns:**  
arr_len - the length of the new array  
arr - the new array  

**Complexity:**  
O(N log(N))   
<a id="reverse"></a>
___
reverse(arr_len : felt, arr : felt*) -> (arr_len : felt, arr : felt*)  
___
Creates a new array that is the reverse of the *arr* given as parameter.  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified

**Returns:**  
arr_len - the length of the new array  
arr - the new array  

**Complexity:**  
O(N)   
<a id="join"></a>
___
join(arr1_len : felt, arr1 : felt*, arr2_len : felt, arr2 : felt*) -> (arr_len : felt, arr : felt*)  
___
Creates a new array that will join the *arr1* with *arr2* by putting all elements of *arr1* in an array then adding all elements of *arr2*.  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified

**Returns:**  
arr1_len - the length of the first  array  
arr1 - the first array  
arr2_len - the length of the second  array  
arr2 - the second array

**Complexity:**  
O(2N)   
<a id="copy_from_to"></a>
___
copy_from_to(arr_len : felt, arr : felt*, from_index : felt, to_index : felt) -> (arr_len : felt, arr : felt*)  
___
Creates a new array that will copy the elements of the *arr* from (*from_index* included) an index to (*to_index* excluded) another index.  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified  
from_index - the starting array the items needs to be copied from  
to_index - the last index the copy must stop (can also be seen as number of elements to copy)

**Returns:**  
arr_len - the length of the new array  
arr - the new array  

**Remark:**  
Will fail if:
 - the *to_index* is smaller or equal to the *from_index*
 - the *from_index* or *to_index* is out of range  

**Complexity:**  
O(N)  
<a id="replace"></a>
___
replace(arr_len : felt, arr : felt*, old_item : felt, new_item : felt) -> (arr_len : felt, arr : felt*)  
___
Creates a new array with all occurences of *old_item* replaced with another value *new_item*.  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified  
old_item - the old value that needs to be replaced  
new_item - the new value that the old value will be replaced with

**Returns:**  
arr_len - the length of the new array  
arr - the new array  

**Complexity:**  
O(N)  

## Array searching functions
<a id="contains"></a>
___
contains(arr_len : felt, arr : felt*, item : felt) -> (contains : felt) 
___
Will check if *arr* contains the *item*  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified  
item - the item that needs to be looked for  

**Returns:**  
contains - 1 if contains the *item* otehrwise 0   

**Complexity:**  
O(N)  
<a id="index_of"></a>
___  
index_of(arr_len : felt, arr : felt*, item : felt) -> (index : felt)    
___
Will check if *arr* contains the *item* and return its index  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified  
item - the item that needs to be looked for   

**Returns:**  
index -  the index of the *item* or 3618502788666131213697322783095070105623107215331596699973092056135872020480

**Remark:**  
It can return 3618502788666131213697322783095070105623107215331596699973092056135872020480 if the *item* isn't found (which is -1 in felt value)

**Complexity:**  
O(N)  
<a id="min"></a>
___
min(arr_len : felt, arr : felt*) -> (min : felt)  
___
Will return the minimum value ot the *arr*  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified  
**Returns:**  
min - the minimum value of the array  

**Remark:**  
Will fail if the array is empty 

**Complexity:**  
O(N)  
<a id="index_of_min"></a>
___
index_of_min(arr_len : felt, arr : felt*) -> (index : felt)  
___
Will return the index of the minimum value ot the *arr*  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified  
**Returns:**  
index - the index of the minimum value of the array  

**Remark:**  
Will fail if the array is empty 

**Complexity:**  
O(N)  
<a id="max"></a>
___
max(arr_len : felt, arr : felt*) -> (max : felt)  
___
Will return the maximum value ot the *arr*  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified  

**Returns:**  
max - the maximum value of the array  

**Remark:**  
Will fail if the array is empty 

**Complexity:**  
O(N)  
<a id="index_of_max"></a>
___
index_of_max(arr_len : felt, arr : felt*) -> (index : felt)  
___
Will return the index of the maximum value ot the *arr*  

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified  

**Returns:**  
index - the index of the maximum value of the array  

**Remark:**  
Will fail if the array is empty 

**Complexity:**  
O(N)  
<a id="occurrences_of"></a>
___
occurrences_of(arr_len : felt, arr : felt*, item : felt) -> (occurrences : felt)  
___
Will return all the occurences of the *item*

**Parameters:**  
arr_len - the length of the array   
arr - the array that needs to be modified  
item - the item for which  the occurences need to be counter  

**Returns:**   
occurences - the amount of time the *item* is present in the array  

**Complexity:**  
O(N)  