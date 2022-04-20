%lang starknet
#
# Imports
#
from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.cairo.common.alloc import alloc
from starkware.cairo.common.math_cmp import is_le

# creating new array

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
    arr_len : felt, arr : felt*, item_to_add : felt
) -> (arr_len : felt, arr : felt*):
    return add_at(arr_len, arr, arr_len, item_to_add)
end

@view
func add_first{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, item_to_add : felt
) -> (arr_len : felt, arr : felt*):
    return add_at(arr_len, arr, 0, item_to_add)
end

@view
func add_at{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, index_to_add : felt, item_to_add : felt
) -> (arr_len : felt, arr : felt*):
    let (isValid) = is_le(index_to_add, arr_len)
    with_attr error_message("Index out of range"):
        assert isValid = 1
    end
    let (new_arr_len, new_arr) = get_new_array()
    return add_at_recursive(arr_len, arr, new_arr, index_to_add, item_to_add, 0)
end

func add_at_recursive{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    old_arr_len : felt,
    old_arr : felt*,
    new_arr : felt*,
    index_to_add : felt,
    item_to_add : felt,
    current_index : felt,
) -> (arr_len : felt, arr : felt*):
    if old_arr_len == current_index:
        # TODO could be enhanced somehow?
        # We need this because it could be that the array is already limited in memory so
        if index_to_add == current_index:
            assert new_arr[current_index] = item_to_add
            return (old_arr_len + 1, new_arr)
        end
        return (old_arr_len, new_arr)
    end

    if index_to_add == current_index:
        assert new_arr[current_index] = item_to_add
        return add_at_recursive(
            old_arr_len + 1, old_arr, new_arr, index_to_add, item_to_add, current_index + 1
        )
    end
    let (addLater) = is_le(current_index, index_to_add)
    if addLater == 1:
        assert new_arr[current_index] = old_arr[current_index]
        return add_at_recursive(
            old_arr_len, old_arr, new_arr, index_to_add, item_to_add, current_index + 1
        )
    end
    assert new_arr[current_index] = old_arr[current_index - 1]
    return add_at_recursive(
        old_arr_len, old_arr, new_arr, index_to_add, item_to_add, current_index + 1
    )
end
