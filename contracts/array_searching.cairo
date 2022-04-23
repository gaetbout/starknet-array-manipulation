%lang starknet
from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.cairo.common.math_cmp import is_le
from contracts.utils import assert_check_array_not_empty

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
    let (indexOfMax) = index_of_max(arr_len, arr)
    return (arr[indexOfMax])
end

@view
func index_of_max{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*
) -> (index : felt):
    assert_check_array_not_empty(arr_len)
    return index_of_max_recursive(arr_len, arr, arr[0], 0, 1)
end

func index_of_max_recursive{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, current_max : felt, current_max_index : felt, current_index : felt
) -> (index : felt):
    if arr_len == current_index:
        return (current_max_index)
    end
    let (isLe) = is_le(current_max, arr[current_index])
    if isLe == 1:
        return index_of_max_recursive(
            arr_len, arr, arr[current_index], current_index, current_index + 1
        )
    end
    return index_of_max_recursive(arr_len, arr, current_max, current_max_index, current_index + 1)
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
