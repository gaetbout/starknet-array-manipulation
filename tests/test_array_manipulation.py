import os

import pytest
from starkware.starknet.testing.starknet import Starknet

CONTRACT_FILE = os.path.join("contracts", "array_manipulation.cairo")

@pytest.fixture(scope="session")
async def contract(starknet):
    return await starknet.deploy(source=CONTRACT_FILE,)
  
@pytest.mark.asyncio
@pytest.mark.parametrize("input, item, result",[
    ([], 1, [1]),
    ([2], 1, [1,2]),
    ([2,3,4], 1, [1,2,3,4])
])
async def test_add_first(contract, input, item, result ):
    execution_info = await contract.add_first([], 1).invoke()
    assert execution_info.result.arr == [1] 
  

@pytest.mark.asyncio
@pytest.mark.parametrize("input, item, result",[
    ([], 1, [1]),
    ([1], 2, [1,2]),
    ([1,2,3], 4, [1,2,3,4])
])
async def test_add_last(contract, input, item, result):
    execution_info = await contract.add_last(input, item).invoke()
    assert execution_info.result.arr == result 



@pytest.mark.asyncio
@pytest.mark.parametrize("input, index, item, result",[
    ([1,3,4], 1, 2, [1,2,3,4]),
    ([1,2,4], 2, 3, [1,2,3,4]),
    ([2,3,4], 0, 1, [1,2,3,4]),
    ([1,2,3], 3, 4, [1,2,3,4]),
    ([1,2,3,5,6], 3, 4, [1,2,3,4,5,6])
])
async def test_add_at(contract, input, index, item, result):
    execution_info = await contract.add_at(input, index, item).invoke()
    assert execution_info.result.arr == result

@pytest.mark.asyncio
async def test_add_at_outside(contract):
    with pytest.raises(Exception) as execution_info:
        await contract.add_at([1,2,3,4], 10,10).invoke()
    assert "Index out of range" in execution_info.value.args[1]["message"]


# Removing 

@pytest.mark.asyncio
@pytest.mark.parametrize("input, result",[
    ([1], []),
    ([1,1,2,3], [1,2,3]),
])
async def test_remove_first(contract, input, result):
    execution_info = await contract.remove_first(input).invoke()
    assert execution_info.result.arr == result 

@pytest.mark.asyncio
async def test_remove_first_emptyArray(contract):
    with pytest.raises(Exception) as execution_info:
        await contract.remove_first([]).invoke()
    assert "Empty array" in execution_info.value.args[1]["message"]

@pytest.mark.asyncio
@pytest.mark.parametrize("input, result",[
    ([1], []),
    ([1,2,3,3], [1,2,3]),
])
async def test_remove_last(contract, input, result):
    execution_info = await contract.remove_last(input).invoke()
    assert execution_info.result.arr == result

@pytest.mark.asyncio
async def test_remove_last_emptyArray(contract):
    with pytest.raises(Exception) as execution_info:
        await contract.remove_last([]).invoke()
    assert "Empty array" in execution_info.value.args[1]["message"]

@pytest.mark.asyncio
@pytest.mark.parametrize("input, index, result",[
    ([1,2,3], 1, [1,3]),
    ([1,2,3,4], 2, [1,2,4]),
    ([1,2,3,4], 3, [1,2,3]),
    ([0,1,2,3,4], 0, [1,2,3,4]),
])
async def test_remove_at(contract, input, index, result):
    execution_info = await contract.remove_at(input, index).invoke()
    assert execution_info.result.arr == result
    
@pytest.mark.asyncio
async def test_remove_at_emptyArray(contract):
    with pytest.raises(Exception) as execution_info:
        await contract.remove_at([], 1).invoke()
    assert "Empty array" in execution_info.value.args[1]["message"]

@pytest.mark.asyncio
async def test_remove_at_outside(contract):
    with pytest.raises(Exception) as execution_info:
        await contract.remove_at([1], 2).invoke()
    assert "Index out of range" in execution_info.value.args[1]["message"]


# reverse

@pytest.mark.asyncio
@pytest.mark.parametrize("input, result",[
    ([1], [1]),
    ([1,2,3], [3,2,1]),
    ([0,1,2,3,4,5,6,7,8,9,10], [10,9,8,7,6,5,4,3,2,1,0])
])
async def test_reverse(contract, input, result):
    execution_info = await contract.reverse(input).invoke()
    assert execution_info.result.arr == result
    
# Sorting 

@pytest.mark.asyncio
@pytest.mark.parametrize("input, result",[
    ([], []),
    ([1,2,3], [3,2,1]),
    ([3,2,1], [3,2,1]),
    ([5,4,3,2,1,2,3,4,5], [5,5,4,4,3,3,2,2,1])
])
async def test_sort(contract, input, result):
    execution_info = await contract.sort(input).invoke()
    assert execution_info.result.arr == result

# Join 

@pytest.mark.asyncio
@pytest.mark.parametrize("input1, input2, result",[
    ([], [], []),
    ([1,2,3], [], [1,2,3]),
    ([], [1,2,3], [1,2,3]),
    ([1,2,3], [4,5,6],[1,2,3,4,5,6]),
    ([1,2], [3,4,5,6], [1,2,3,4,5,6]),
    ([1,2,3,4], [5,6], [1,2,3,4,5,6]),
])
async def test_join(contract, input1, input2, result):
    execution_info = await contract.join(input1, input2).invoke()
    assert execution_info.result.arr == result