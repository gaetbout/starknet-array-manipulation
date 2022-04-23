import os

import pytest
from starkware.starknet.testing.starknet import Starknet
CONTRACT_FILE = os.path.join("contracts", "array_manipulation.cairo")

@pytest.fixture
async def contract():
    starknet = await Starknet.empty()
    return await starknet.deploy(source=CONTRACT_FILE,)
    

@pytest.mark.asyncio
@pytest.mark.get_new_array
async def test_get_new_array(contract):
    execution_info = await contract.get_new_array().call()
    assert execution_info.result.arr == [] 


@pytest.mark.asyncio
@pytest.mark.add_last
async def test_add_last_emptyArray(contract):
    execution_info = await contract.add_last([], 1).invoke()
    assert execution_info.result.arr == [1] 


@pytest.mark.asyncio
@pytest.mark.add_last
async def test_add_last_arrayOfSizeOne(contract):
    execution_info = await contract.add_last([1], 2).invoke()
    assert execution_info.result.arr == [1,2] 


@pytest.mark.asyncio
@pytest.mark.add_last
async def test_add_last_arrayOfSizeThree(contract):
    execution_info = await contract.add_last([1,2,3], 4).invoke()
    assert execution_info.result.arr == [1,2,3,4] 


@pytest.mark.asyncio
@pytest.mark.add_first
async def test_add_first_emptyArray(contract):
    execution_info = await contract.add_first([], 1).invoke()
    assert execution_info.result.arr == [1] 

@pytest.mark.asyncio
@pytest.mark.add_first
async def test_add_first_arrayOfSizeOne(contract):
    execution_info = await contract.add_first([2], 1).invoke()
    assert execution_info.result.arr == [1,2] 

@pytest.mark.asyncio
@pytest.mark.add_first
async def test_add_first_arrayOfSizeThree(contract):
    execution_info = await contract.add_first([2,3,4], 1).invoke()
    assert execution_info.result.arr == [1,2,3,4] 


@pytest.mark.asyncio
@pytest.mark.add_at
async def test_add_at(contract):
    execution_info = await contract.add_at([1,3,4], 1,2).invoke()
    assert execution_info.result.arr == [1,2,3,4] 

@pytest.mark.asyncio
@pytest.mark.add_at
async def test_add_at_2(contract):
    execution_info = await contract.add_at([1,2,4], 2,3).invoke()
    assert execution_info.result.arr == [1,2,3,4] 


@pytest.mark.asyncio
@pytest.mark.add_at
async def test_add_at_first(contract):
    execution_info = await contract.add_at([2,3,4], 0,1).invoke()
    assert execution_info.result.arr == [1,2,3,4] 

@pytest.mark.asyncio
@pytest.mark.add_at
async def test_add_at_last(contract):
    execution_info = await contract.add_at([1,2,3], 3,4).invoke()
    assert execution_info.result.arr == [1,2,3,4] 


@pytest.mark.asyncio
@pytest.mark.add_at
async def test_add_at_outside(contract):
    with pytest.raises(Exception) as execution_info:
        await contract.add_at([1,2,3,4], 10,10).invoke()
    assert "Index out of range" in execution_info.value.args[1]["message"]


# Removing 

@pytest.mark.asyncio
@pytest.mark.remove_last
async def test_remove_last_arrayOfSizeOne(contract):
    execution_info = await contract.remove_last([1]).invoke()
    assert execution_info.result.arr == [] 


@pytest.mark.asyncio
@pytest.mark.remove_last
async def test_remove_last_arrayOfSizeThree(contract):
    execution_info = await contract.remove_last([1,2,3]).invoke()
    assert execution_info.result.arr == [1,2] 

@pytest.mark.asyncio
@pytest.mark.remove_last
async def test_remove_last_emptyArray(contract):
    with pytest.raises(Exception) as execution_info:
        await contract.remove_last([]).invoke()
    assert "Empty array" in execution_info.value.args[1]["message"]


@pytest.mark.asyncio
@pytest.mark.remove_first
async def test_remove_first_arrayOfSizeOne(contract):
    execution_info = await contract.remove_first([1]).invoke()
    assert execution_info.result.arr == [] 

@pytest.mark.asyncio
@pytest.mark.remove_first
async def test_remove_first_arrayOfSizeThree(contract):
    execution_info = await contract.remove_first([1,1,2,3]).invoke()
    assert execution_info.result.arr == [1,2,3]

@pytest.mark.asyncio
@pytest.mark.remove_first
async def test_remove_first_emptyArray(contract):
    with pytest.raises(Exception) as execution_info:
        await contract.remove_first([]).invoke()
    assert "Empty array" in execution_info.value.args[1]["message"]

@pytest.mark.asyncio
@pytest.mark.remove_at
async def test_remove_at_1(contract):
    execution_info = await contract.remove_at([1,2,3],1).invoke()
    assert execution_info.result.arr == [1,3]

@pytest.mark.asyncio
@pytest.mark.remove_at
async def test_remove_at_2(contract):
    execution_info = await contract.remove_at([1,2,3,4],2).invoke()
    assert execution_info.result.arr == [1,2,4]

@pytest.mark.asyncio
@pytest.mark.remove_at
async def test_remove_at_3(contract):
    execution_info = await contract.remove_at([1,2,3,4],3).invoke()
    assert execution_info.result.arr == [1,2,3]
    
@pytest.mark.asyncio
@pytest.mark.remove_at
async def test_remove_at_emptyArray(contract):
    with pytest.raises(Exception) as execution_info:
        await contract.remove_at([], 1).invoke()
    assert "Empty array" in execution_info.value.args[1]["message"]

@pytest.mark.asyncio
@pytest.mark.remove_at
async def test_remove_at_outside(contract):
    with pytest.raises(Exception) as execution_info:
        await contract.remove_at([1], 2).invoke()
    assert "Index out of range" in execution_info.value.args[1]["message"]


# reverse

@pytest.mark.asyncio
@pytest.mark.reverse
async def test_reverse(contract):
    execution_info = await contract.reverse([1,2,3]).invoke()
    assert execution_info.result.arr == [3,2,1]

@pytest.mark.asyncio
@pytest.mark.reverse
async def test_reverse_array_size_1(contract):
    execution_info = await contract.reverse([1]).invoke()
    assert execution_info.result.arr == [1]

@pytest.mark.asyncio
@pytest.mark.reverse
async def test_reverse_emptyArray(contract):
    execution_info = await contract.reverse([]).invoke()
    assert execution_info.result.arr == []

@pytest.mark.asyncio
@pytest.mark.reverse
async def test_reverse_long(contract):
    execution_info = await contract.reverse([0,1,2,3,4,5,6,7,8,9,10]).invoke()
    assert execution_info.result.arr == [10,9,8,7,6,5,4,3,2,1,0]

# Sorting 

@pytest.mark.asyncio
@pytest.mark.sort
async def test_sort(contract):
    execution_info = await contract.sort([1,2,3]).invoke()
    assert execution_info.result.arr == [3,2,1]

@pytest.mark.asyncio
@pytest.mark.sort
async def test_sort_alreadySorted(contract):
    execution_info = await contract.sort([3,2,1]).invoke()
    assert execution_info.result.arr == [3,2,1]

@pytest.mark.asyncio
@pytest.mark.sort
async def test_sort_withMultipleMaxs(contract):
    execution_info = await contract.sort([5,4,3,2,1,2,3,4,5]).invoke()
    assert execution_info.result.arr == [5,5,4,4,3,3,2,2,1]

@pytest.mark.asyncio
@pytest.mark.sort
async def test_sort_emptyArray(contract):
    execution_info = await contract.sort([]).invoke()
    assert execution_info.result.arr == []