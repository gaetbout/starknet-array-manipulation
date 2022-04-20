import os

import pytest
from starkware.starknet.testing.starknet import Starknet
CONTRACT_FILE = os.path.join("contracts", "array.cairo")

@pytest.fixture(autouse=True)
async def setup():
    starknet = await Starknet.empty()
    contract = await starknet.deploy(source=CONTRACT_FILE,)
    contract = await starknet.deploy(source=CONTRACT_FILE,)
    pytest.starknet = starknet
    pytest.contract = contract
    

@pytest.mark.asyncio
@pytest.mark.get_new_array
async def test_get_new_array():
    execution_info = await pytest.contract.get_new_array().call()
    assert execution_info.result.arr == [] 


@pytest.mark.asyncio
@pytest.mark.add_last
async def test_add_last_onEmptyArray():
    execution_info = await pytest.contract.add_last([], 1).invoke()
    assert execution_info.result.arr == [1] 


@pytest.mark.asyncio
@pytest.mark.add_last
async def test_add_last_onArrayOfSizeOne():
    execution_info = await pytest.contract.add_last([1], 2).invoke()
    assert execution_info.result.arr == [1,2] 


@pytest.mark.asyncio
@pytest.mark.add_last
async def test_add_last_onArrayOfSizeThree():
    execution_info = await pytest.contract.add_last([1,2,3], 4).invoke()
    assert execution_info.result.arr == [1,2,3,4] 


@pytest.mark.asyncio
@pytest.mark.add_first
async def test_add_first_onEmptyArray():
    execution_info = await pytest.contract.add_first([], 1).invoke()
    assert execution_info.result.arr == [1] 

@pytest.mark.asyncio
@pytest.mark.add_first
async def test_add_first_onArrayOfSizeOne():
    execution_info = await pytest.contract.add_first([2], 1).invoke()
    assert execution_info.result.arr == [1,2] 

@pytest.mark.asyncio
@pytest.mark.add_first
async def test_add_first_onArrayOfSizeThree():
    execution_info = await pytest.contract.add_first([2,3,4], 1).invoke()
    assert execution_info.result.arr == [1,2,3,4] 


@pytest.mark.asyncio
@pytest.mark.add_at
async def test_add_at():
    execution_info = await pytest.contract.add_at([1,3,4], 1,2).invoke()
    assert execution_info.result.arr == [1,2,3,4] 

@pytest.mark.asyncio
@pytest.mark.add_at
async def test_add_at_2():
    execution_info = await pytest.contract.add_at([1,2,4], 2,3).invoke()
    assert execution_info.result.arr == [1,2,3,4] 


@pytest.mark.asyncio
@pytest.mark.add_at
async def test_add_at_first():
    execution_info = await pytest.contract.add_at([2,3,4], 0,1).invoke()
    assert execution_info.result.arr == [1,2,3,4] 

@pytest.mark.asyncio
@pytest.mark.add_at
async def test_add_at_last():
    execution_info = await pytest.contract.add_at([1,2,3], 3,4).invoke()
    assert execution_info.result.arr == [1,2,3,4] 


@pytest.mark.asyncio
@pytest.mark.add_at
async def test_add_at_outside():
    with pytest.raises(Exception) as execution_info:
        await pytest.contract.add_at([1,2,3,4], 10,10).invoke()
    assert "Index out of range" in execution_info.value.args[1]["message"]
