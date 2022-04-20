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
    assert arr[arr_len] = item_to_add
    return (arr_len + 1, arr)
end

@view
func add_first{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, item_to_add : felt
) -> (arr_len : felt, arr : felt*):
    return add_at(arr_len, arr, new_arr, item_to_add, 0, 0)
end

@view
func add_at{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    arr_len : felt, arr : felt*, item_to_add : felt, index_to_add : felt
) -> (arr_len : felt, arr : felt*):
    # TODO Ensure array bigger then  where you want to add
    let (new_arr_len, new_arr) = get_new_array()
    return add_at_recursive(arr_len, arr, new_arr, item_to_add, index_to_add, 0)
end

func add_at_recursive{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
    old_arr_len : felt,
    old_arr : felt*,
    new_arr : felt*,
    item_to_add : felt,
    index_to_add : felt,
    current_index : felt,
) -> (arr_len : felt, arr : felt*):
    if old_arr_len == current_index:
        # TODO finish
        return (old_arr_len + 1, new_arr)
    end
    if index_to_add == current_index:
        assert new_arr[current_index] = item_to_add
        return add_at_recursive(arr_len + 1, arr, item_to_add, index_to_add, current_index + 1)
    end
    let (addLater) = is_le(index_to_add, current_index)
    if addLater == 1:
        assert new_arr[current_index] = old_arr[current_index]
        return add_at_recursive(arr_len, arr, item_to_add, index_to_add, current_index + 1)
    end
    assert arr[current_index] = item_to_add
    return add_at_recursive(arr_len + 1, arr, item_to_add, index_to_add, current_index + 1)
end
