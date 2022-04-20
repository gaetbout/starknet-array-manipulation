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
    print (execution_info.result.arr)
    assert execution_info.result.arr == [] 


@pytest.mark.asyncio
@pytest.mark.add_last
async def test_add_last_onEmptyArray():
    execution_info = await pytest.contract.add_last([], 1).invoke()
    print (execution_info.result.arr)
    assert execution_info.result.arr == [1] 


@pytest.mark.asyncio
@pytest.mark.add_last
async def test_add_last_onArrayOfSizeOne():
    execution_info = await pytest.contract.add_last([1], 2).invoke()
    print (execution_info.result.arr)
    assert execution_info.result.arr == [1,2] 


@pytest.mark.asyncio
@pytest.mark.add_last
async def test_add_last_onArrayOfSizeThree():
    execution_info = await pytest.contract.add_last([1,2,3], 4).invoke()
    print (execution_info.result.arr)
    assert execution_info.result.arr == [1,2,3,4] 


@pytest.mark.asyncio
@pytest.mark.add_first
async def test_add_first_onEmptyArray():
    execution_info = await pytest.contract.add_first([], 1).invoke()
    print (execution_info.result.arr)
    assert execution_info.result.arr == [1] 

@pytest.mark.asyncio
@pytest.mark.add_first
async def test_add_first_onArrayOfSizeOne():
    execution_info = await pytest.contract.add_first([2], 1).invoke()
    print (execution_info.result.arr)
    assert execution_info.result.arr == [1,2] 

@pytest.mark.asyncio
@pytest.mark.add_first
async def test_add_first_onArrayOfSizeThree():
    execution_info = await pytest.contract.add_first([2,3,4], 1).invoke()
    print (execution_info.result.arr)
    assert execution_info.result.arr == [1,2,3,4] 


@pytest.mark.asyncio
@pytest.mark.add_at
async def test_add_at():
    execution_info = await pytest.contract.add_first([2,3,4], 1).invoke()
    print (execution_info.result.arr)
    assert execution_info.result.arr == [1,2,3,4] 
