import os

import pytest
from starkware.starknet.testing.starknet import Starknet
CONTRACT_FILE = os.path.join("contracts", "array.cairo")

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
async def test_remove_last_emptyArray(contract):
    with pytest.raises(Exception) as execution_info:
        await contract.remove_last([]).invoke()
    assert "Empty array" in execution_info.value.args[1]["message"]


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
@pytest.mark.remove_first
async def test_remove_first_emptyArray(contract):
    with pytest.raises(Exception) as execution_info:
        await contract.remove_first([]).invoke()
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


# Searching 

@pytest.mark.asyncio
@pytest.mark.contains
async def test_contains(contract):
    execution_info = await contract.contains([1,2,3,4], 2).invoke()
    assert execution_info.result.contains == 1

@pytest.mark.asyncio
@pytest.mark.contains
async def test_contains_emptyArray(contract):
    execution_info = await contract.contains([], 2).invoke()
    assert execution_info.result.contains == 0

@pytest.mark.asyncio
@pytest.mark.contains
async def test_contains_withDuplicates(contract):
    execution_info = await contract.contains([1,2,3,2,4], 2).invoke()
    assert execution_info.result.contains == 1

@pytest.mark.asyncio
@pytest.mark.contains
async def test_contains_notInArray(contract):
    execution_info = await contract.contains([1,2,3,2,4], 5).invoke()
    assert execution_info.result.contains == 0


@pytest.mark.asyncio
@pytest.mark.index_of
async def test_index_of(contract):
    execution_info = await contract.index_of([1,2,3,4], 2).invoke()
    assert execution_info.result.index == 1

@pytest.mark.asyncio
@pytest.mark.index_of
async def test_index_of_emptyArray(contract):
    execution_info = await contract.index_of([], 2).invoke()
    assert execution_info.result.index == 3618502788666131213697322783095070105623107215331596699973092056135872020480

@pytest.mark.asyncio
@pytest.mark.index_of
async def test_index_of_withDuplicates(contract):
    execution_info = await contract.index_of([1,2,3,2,4], 2).invoke()
    assert execution_info.result.index == 1

@pytest.mark.asyncio
@pytest.mark.index_of
async def test_index_of_notInArray(contract):
    execution_info = await contract.index_of([1,2,3,2,4], 5).invoke()
    assert execution_info.result.index == 3618502788666131213697322783095070105623107215331596699973092056135872020480


@pytest.mark.asyncio
@pytest.mark.min
async def test_min(contract):
    execution_info = await contract.min([4,3,2,1,2,3,2,4]).invoke()
    assert execution_info.result.min == 1

@pytest.mark.asyncio
@pytest.mark.min
async def test_min_first(contract):
    execution_info = await contract.min([1,2,3,4]).invoke()
    assert execution_info.result.min == 1

@pytest.mark.asyncio
@pytest.mark.min
async def test_min_last(contract):
    execution_info = await contract.min([4,3,2,0]).invoke()
    assert execution_info.result.min == 0

@pytest.mark.asyncio
@pytest.mark.min
async def test_min_duplicates(contract):
    execution_info = await contract.min([4,2,3,2,5]).invoke()
    assert execution_info.result.min == 2


@pytest.mark.asyncio
@pytest.mark.min
async def test_min_emptyArray(contract):
    with pytest.raises(Exception) as execution_info:
        await contract.min([]).invoke()
    assert "Empty array" in execution_info.value.args[1]["message"]


@pytest.mark.asyncio
@pytest.mark.max
async def test_max(contract):
    execution_info = await contract.max([1,2,3,4,3,2,1]).invoke()
    assert execution_info.result.max == 4

@pytest.mark.asyncio
@pytest.mark.max
async def test_max_first(contract):
    execution_info = await contract.max([4,3,2,1]).invoke()
    assert execution_info.result.max == 4

@pytest.mark.asyncio
@pytest.mark.max
async def test_max_last(contract):
    execution_info = await contract.max([1,2,3,4]).invoke()
    assert execution_info.result.max == 4

@pytest.mark.asyncio
@pytest.mark.max
async def test_max_duplicates(contract):
    execution_info = await contract.max([4,2,3,2,5]).invoke()
    assert execution_info.result.max == 5


@pytest.mark.asyncio
@pytest.mark.max
async def test_max_emptyArray(contract):
    with pytest.raises(Exception) as execution_info:
        await contract.max([]).invoke()
    assert "Empty array" in execution_info.value.args[1]["message"]



