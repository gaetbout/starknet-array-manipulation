%lang starknet
from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.cairo.common.math_cmp import is_le, is_not_zero
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
