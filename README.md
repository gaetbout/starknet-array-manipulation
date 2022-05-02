![Tests](https://github.com/gaetbout/starknet-array-manipulation/actions/workflows/python-app.yml/badge.svg)

#  Array

Here is a simple lib to do some common array operations.  
Since cairo is memory immutable (once you write the value in a memory cell, this cell cannot  change anymore), each function requiring any memory change, will create a new array. So you can see each method as a copy method with some more extra logic.  

This library is divided in two parts.  
To know how to use each function, don't hesitate to refer to the tests.  

Here is everything you can do:  

## Array manipulation

This file will always have to create a new array to be returned.  
Unless specified, these methods are all in O(N) complexity.  
All these methods are returning the same values  
`(arr_len : felt, arr : felt*):`  

| Function | Arguments |
| ------ | ----------- |
| add_first | (arr_len : felt, arr : felt*, item : felt)  |
| add_last | (arr_len : felt, arr : felt*, item : felt) |
| add_at | (arr_len : felt, arr : felt*, index : felt, item : felt) |
| remove_first | (arr_len : felt, arr : felt*) |
| remove_last | (arr_len : felt, arr : felt*) |
| remove_at | (arr_len : felt, arr : felt*, index : felt) |
| sort | (arr_len : felt, arr : felt*) |
| reverse | (arr_len : felt, arr : felt*) |
| join | (arr1_len : felt, arr1 : felt*, arr2_len : felt, arr2 : felt*) |
| copy_from_to | (arr_len : felt, arr : felt*, from_index : felt, to_index : felt)  |

⚠️ Some remarks:   
> For add_last, if you still have access to the array, and the memory isn't bounded already, please just do:  
 `arr[arr_len] = item`  
 it'll avoid the creation of a new array  

> The sort method has a complexity of O(N(log(n)))  

> remove_first, remove_last, remove_at will fail if the array is empty  

> add_at, remove_at will fail if the index is out of range  

> copy_from_to can fail for 3 different reasons. The From index or To index being  out of range and To index being smaller or equal to From index

## Array searching
These are all the functions that will iterate through the array and return what is asked.  
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

⚠️ Some remarks:   
> index_of if  not found will return 3618502788666131213697322783095070105623107215331596699973092056135872020480 which is -1 in felt

> min, index_of_min, max, index_of_max will fail if the array is empty

## Tests

To run the test suite, copy this repository and put yourself at the root.  
Compile the contracts using `make build` or `nile compile`.  
Run the tests using `make test` or, for more details, `pytest -v`.   
For more  details check the Actions tab of this GitHub repository.


## TODO

 - Removing 
    * All occurences of
    * First occurence of
    * Last occurence of 
 - Flatten?  
 - Support of structure in a generic way?
 - Replace 

Don't hesitate to request me any feature that could be missing or ping me when there is the support for structure
