%lang starknet
from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.cairo.common.alloc import alloc
from contracts.utils import assert_index_in_array_length, assert_check_array_not_empty

# Creation

@view
func get_new_array{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}() -> (
    arr_len : felt, arr : felt*
):
    alloc_locals
    let (local arr : felt*) = alloc()
    return (0, arr)
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
    let (new_arr_len, new_arr) = get_new_array()
    return add_at_recursive(arr_len, arr, new_arr, index, item, 0, 0)
end

func add_at_recursive{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    old_arr_len : felt,
    old_arr : felt*,
    new_arr : felt*,
    index : felt,
    item : felt,
    current_index : felt,
    offset : felt,
) -> (arr_len : felt, arr : felt*):
    if old_arr_len + 1 == current_index:
        return (old_arr_len + 1, new_arr)
    end
    if index == current_index:
        assert new_arr[current_index] = item
        return add_at_recursive(
            old_arr_len, old_arr, new_arr, index, item, current_index + 1, offset + 1
        )
    end
    assert new_arr[current_index] = old_arr[current_index - offset]
    return add_at_recursive(old_arr_len, old_arr, new_arr, index, item, current_index + 1, offset)
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
    let (new_arr_len, new_arr) = get_new_array()
    return remove_at_recursive(arr_len, arr, new_arr, index, 0, 0)
end

func remove_at_recursive{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    old_arr_len : felt,
    old_arr : felt*,
    new_arr : felt*,
    index : felt,
    current_index : felt,
    offset : felt,
) -> (arr_len : felt, arr : felt*):
    if old_arr_len - 1 == current_index:
        return (old_arr_len - 1, new_arr)
    end
    if index == current_index:
        assert new_arr[current_index] = old_arr[current_index + 1]
        return remove_at_recursive(
            old_arr_len, old_arr, new_arr, index, current_index + 1, offset + 1
        )
    end
    assert new_arr[current_index] = old_arr[current_index + offset]
    return remove_at_recursive(old_arr_len, old_arr, new_arr, index, current_index + 1, offset)
end
