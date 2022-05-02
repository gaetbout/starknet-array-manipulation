%lang starknet
from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.cairo.common.alloc import alloc
from starkware.cairo.common.memcpy import memcpy
from contracts.utils import (
    assert_index_in_array_length,
    assert_check_array_not_empty,
    assert_from_smaller_then_to,
)
from contracts.array_searching import index_of_max

func get_new_array{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}() -> (
    arr_len : felt, arr : felt*
):
    alloc_locals
    let (local arr : felt*) = alloc()
    return (0, arr)
end

# Adding

@view
func add_first{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, item : felt
) -> (arr_len : felt, arr : felt*):
    alloc_locals
    let (new_arr_len, new_arr) = get_new_array()
    assert new_arr[0] = item
    memcpy(new_arr + 1, arr, arr_len)
    return (arr_len + 1, new_arr)
end

@view
func add_last{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, item : felt
) -> (arr_len : felt, arr : felt*):
    alloc_locals
    # We can't just assert at arr_len with the item
    let (new_arr_len, new_arr) = get_new_array()
    memcpy(new_arr, arr, arr_len)
    assert new_arr[arr_len] = item
    return (arr_len + 1, new_arr)
end

@view
func add_at{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, index : felt, item : felt
) -> (arr_len : felt, arr : felt*):
    alloc_locals
    assert_index_in_array_length(arr_len, index)
    let (new_arr_len, new_arr) = get_new_array()
    memcpy(new_arr, arr, index)
    assert new_arr[index] = item
    memcpy(new_arr + index + 1, arr + index, arr_len - index)
    return (arr_len + 1, new_arr)
end

# Removing

@view
func remove_first{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*
) -> (arr_len : felt, arr : felt*):
    alloc_locals
    assert_check_array_not_empty(arr_len)
    let (new_arr_len, new_arr) = get_new_array()
    memcpy(new_arr, arr + 1, arr_len - 1)
    return (arr_len - 1, new_arr)
end

@view
func remove_last{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*
) -> (arr_len : felt, arr : felt*):
    alloc_locals
    assert_check_array_not_empty(arr_len)
    let (new_arr_len, new_arr) = get_new_array()
    memcpy(new_arr, arr, arr_len - 1)
    return (arr_len - 1, new_arr)
end

@view
func remove_at{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, index : felt
) -> (arr_len : felt, arr : felt*):
    alloc_locals
    assert_check_array_not_empty(arr_len)
    assert_index_in_array_length(arr_len, index + 1)
    let (new_arr_len, new_arr) = get_new_array()
    memcpy(new_arr, arr, index)
    memcpy(new_arr + index, arr + index + 1, arr_len - index - 1)
    return (arr_len - 1, new_arr)
end

# Reverse

@view
func reverse{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*
) -> (arr_len : felt, arr : felt*):
    let (new_arr_len, new_arr) = get_new_array()
    return reverse_recursive(arr_len, arr, new_arr_len, new_arr, 0)
end

func reverse_recursive{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    old_arr_len : felt, old_arr : felt*, new_arr_len : felt, new_arr : felt*, current_index : felt
) -> (arr_len : felt, arr : felt*):
    if old_arr_len == current_index:
        return (new_arr_len, new_arr)
    end
    assert new_arr[current_index] = old_arr[old_arr_len - current_index - 1]
    return reverse_recursive(old_arr_len, old_arr, new_arr_len + 1, new_arr, current_index + 1)
end

# Sorting

@view
func sort{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*
) -> (arr_len : felt, arr : felt*):
    let (sorted_add_len, sorted_add) = get_new_array()
    return sort_recursive(arr_len, arr, sorted_add_len, sorted_add)
end

func sort_recursive{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    old_arr_len : felt, old_arr : felt*, sorted_arr_len : felt, sorted_arr : felt*
) -> (sorted_arr_len : felt, sorted_arr : felt*):
    alloc_locals
    # Array to be sorted is empty
    if old_arr_len == 0:
        return (sorted_arr_len, sorted_arr)
    end
    let (indexOfMax) = index_of_max(old_arr_len, old_arr)
    # Pushing the max occurence to the last available spot
    assert sorted_arr[sorted_arr_len] = old_arr[indexOfMax]
    # getting a new old array
    let (old_shortened_arr_len, old_shortened_arr) = remove_at(old_arr_len, old_arr, indexOfMax)
    return sort_recursive(old_shortened_arr_len, old_shortened_arr, sorted_arr_len + 1, sorted_arr)
end

# Join

@view
func join{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr1_len : felt, arr1 : felt*, arr2_len : felt, arr2 : felt*
) -> (arr_len : felt, arr : felt*):
    alloc_locals
    let (new_arr_len, new_arr) = get_new_array()
    memcpy(new_arr, arr1, arr1_len)
    memcpy(new_arr + arr1_len, arr2, arr2_len)
    return (arr1_len + arr2_len, new_arr)
end

@view
func copy_from_to{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, from_index : felt, to_index : felt
) -> (arr_len : felt, arr : felt*):
    alloc_locals
    assert_index_in_array_length(arr_len, from_index)
    assert_index_in_array_length(arr_len, to_index)
    assert_from_smaller_then_to(from_index, to_index)
    let (new_arr_len, new_arr) = get_new_array()
    memcpy(new_arr, arr + from_index, to_index - from_index)
    return (to_index - from_index, new_arr)
end
