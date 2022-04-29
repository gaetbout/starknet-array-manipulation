%lang starknet
from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.cairo.common.alloc import alloc
from contracts.utils import assert_index_in_array_length, assert_check_array_not_empty
from contracts.array_searching import index_of_max
from contracts.structures import Array

func get_new_array{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}() -> (
    arr : Array
):
    alloc_locals
    let (local arr : felt*) = alloc()
    return (Array(0, arr))
end

# Adding

@view
func add_last{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, item : felt
) -> (arr_len : felt, arr : felt*):
    # We can't just assert at arr_len with the item (try it, a test should be failing :))
    return add_at(arr_len, arr, arr_len, item)
end

@view
func add_first{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, item : felt
) -> (arr_len : felt, arr : felt*):
    return add_at(arr_len, arr, 0, item)
end

@view
func add_at{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, index : felt, item : felt
) -> (arr_len : felt, arr : felt*):
    assert_index_in_array_length(arr_len, index)
    let (new_arr) = get_new_array()
    return add_at_recursive(Array(arr_len, arr), new_arr, index, item, 0, 0)
end

func add_at_recursive{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    old_arr : Array, new_arr : Array, index : felt, item : felt, current_index : felt, offset : felt
) -> (arr_len : felt, arr : felt*):
    if old_arr.length + 1 == current_index:
        return (old_arr.length + 1, new_arr.values)
    end
    if index == current_index:
        assert new_arr.values[current_index] = item
        return add_at_recursive(old_arr, new_arr, index, item, current_index + 1, offset + 1)
    end
    assert new_arr.values[current_index] = old_arr.values[current_index - offset]
    return add_at_recursive(old_arr, new_arr, index, item, current_index + 1, offset)
end

# Removing

@view
func remove_last{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*
) -> (arr_len : felt, arr : felt*):
    assert_check_array_not_empty(arr_len)
    return remove_at(arr_len, arr, arr_len - 1)
end

@view
func remove_first{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*
) -> (arr_len : felt, arr : felt*):
    assert_check_array_not_empty(arr_len)
    return remove_at(arr_len, arr, 0)
end

@view
func remove_at{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, index : felt
) -> (arr_len : felt, arr : felt*):
    assert_check_array_not_empty(arr_len)
    assert_index_in_array_length(arr_len, index + 1)
    let (new_arr) = get_new_array()
    return remove_at_recursive(Array(arr_len, arr), new_arr, index, 0, 0)
end

func remove_at_recursive{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    old_arr : Array, new_arr : Array, index : felt, current_index : felt, offset : felt
) -> (arr_len : felt, arr : felt*):
    if old_arr.length - 1 == current_index:
        return (old_arr.length - 1, new_arr.values)
    end
    if index == current_index:
        assert new_arr.values[current_index] = old_arr.values[current_index + 1]
        return remove_at_recursive(old_arr, new_arr, index, current_index + 1, offset + 1)
    end
    assert new_arr.values[current_index] = old_arr.values[current_index + offset]
    return remove_at_recursive(old_arr, new_arr, index, current_index + 1, offset)
end

# Reverse
@view
func reverse{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*
) -> (arr_len : felt, arr : felt*):
    let (new_arr) = get_new_array()
    return reverse_recursive(Array(arr_len, arr), new_arr, 0)
end

func reverse_recursive{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    old_arr : Array, new_arr : Array, current_index : felt
) -> (arr_len : felt, arr : felt*):
    if old_arr.length == current_index:
        return (old_arr.length, new_arr.values)
    end
    assert new_arr.values[current_index] = old_arr.values[old_arr.length - current_index - 1]
    return reverse_recursive(old_arr, new_arr, current_index + 1)
end

# Sorting

@view
func sort{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*
) -> (arr_len : felt, arr : felt*):
    let (arr_sorted) = get_new_array()
    return sort_recursive(Array(arr_len, arr), arr_sorted)
end

func sort_recursive{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    old_arr : Array, arr_sorted : Array
) -> (arr_sorted_len : felt, arr_sorted : felt*):
    alloc_locals
    # Array to be sorted is empty
    if old_arr.length == 0:
        return (arr_sorted.length, arr_sorted.values)
    end
    let (indexOfMax) = index_of_max(old_arr.length, old_arr.values)
    # Pushing the max occurence to the last available spot
    assert arr_sorted.values[arr_sorted.length] = old_arr.values[indexOfMax]
    # getting a new old array
    let (old_arr_shortened_len, old_arr_shortened) = remove_at(
        old_arr.length, old_arr.values, indexOfMax
    )
    return sort_recursive(
        Array(old_arr_shortened_len, old_arr_shortened),
        Array(arr_sorted.length + 1, arr_sorted.values),
    )
end
