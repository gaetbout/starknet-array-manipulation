%lang starknet
from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.cairo.common.alloc import alloc
from starkware.cairo.common.math_cmp import is_le, is_not_zero

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

# Searching
@view
func contains{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, item : felt
) -> (contains : felt):
    let (index) = index_of(arr_len, arr, item)
    if index == -1:
        return (0)
    end
    return (1)
end

@view
func index_of{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, item : felt
) -> (index : felt):
    return index_of_recursive(arr_len, arr, item, 0)
end

func index_of_recursive{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, item : felt, current_index : felt
) -> (index : felt):
    if arr_len == current_index:
        # Returning -1 because it is very very unlikely that we have an array that big
        return (-1)
    end
    if arr[current_index] == item:
        return (current_index)
    end
    return index_of_recursive(arr_len, arr, item, current_index + 1)
end

@view
func min{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*
) -> (min : felt):
    assert_check_array_not_empty(arr_len)
    return min_recursive(arr_len, arr, arr[0], 1)
end

func min_recursive{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, current_min : felt, current_index : felt
) -> (min : felt):
    if arr_len == current_index:
        return (current_min)
    end
    let (isLe) = is_le(arr[current_index], current_min)
    if isLe == 1:
        return min_recursive(arr_len, arr, arr[current_index], current_index + 1)
    end
    return min_recursive(arr_len, arr, current_min, current_index + 1)
end

@view
func max{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*
) -> (max : felt):
    assert_check_array_not_empty(arr_len)
    return max_recursive(arr_len, arr, arr[0], 1)
end

func max_recursive{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, current_max : felt, current_index : felt
) -> (max : felt):
    if arr_len == current_index:
        return (current_max)
    end
    let (isLe) = is_le(current_max, arr[current_index])
    if isLe == 1:
        return max_recursive(arr_len, arr, arr[current_index], current_index + 1)
    end
    return max_recursive(arr_len, arr, current_max, current_index + 1)
end

@view
func occurrences_of{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, item : felt
) -> (occurrences : felt):
    return occurrences_of_recursive(arr_len, arr, item, 0, 0)
end

@view
func occurrences_of_recursive{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, item : felt, current_occurrences : felt, current_index : felt
) -> (occurrences : felt):
    if arr_len == current_index:
        return (current_occurrences)
    end
    if arr[current_index] == item:
        return occurrences_of_recursive(
            arr_len, arr, item, current_occurrences + 1, current_index + 1
        )
    end
    return occurrences_of_recursive(arr_len, arr, item, current_occurrences, current_index + 1)
end

# Checking

func assert_index_in_array_length{
    syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr
}(arr_len : felt, index : felt):
    let (res) = is_le(index, arr_len)
    with_attr error_message("Index out of range"):
        assert res = 1
    end
    return ()
end

func assert_check_array_not_empty{
    syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr
}(arr_len : felt):
    let (res) = is_not_zero(arr_len)
    with_attr error_message("Empty array"):
        assert res = 1
    end
    return ()
end
