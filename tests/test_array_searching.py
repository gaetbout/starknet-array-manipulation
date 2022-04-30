import os

import pytest
from starkware.starknet.testing.starknet import Starknet

MAX_VALUE = 3618502788666131213697322783095070105623107215331596699973092056135872020480
CONTRACT_FILE = os.path.join("contracts", "array_searching.cairo")

@pytest.fixture(scope="session")
async def contract(starknet):
    return await starknet.deploy(source=CONTRACT_FILE,)

@pytest.mark.asyncio
@pytest.mark.parametrize("input, item, result",[
    ([], 2, 0),
    ([1,2,3,4], 2, 1),
    ([1,2,3,2,4], 2, 1),
    ([1,2,3,2,4], 5, 0),
])
async def test_contains(contract, input, item, result):
    execution_info = await contract.contains(input, item).invoke()
    assert execution_info.result.contains == result

@pytest.mark.asyncio
@pytest.mark.parametrize("input, item, result",[
    ([1,2,3,4], 2, 1),
    ([1,2,3,2,4], 2, 1),
    ([], 2, MAX_VALUE),
    ([1,2,3,2,4], 5, MAX_VALUE),
])
async def test_index_of(contract, input, item, result):
    execution_info = await contract.index_of(input, item).invoke()
    assert execution_info.result.index == result

@pytest.mark.asyncio
@pytest.mark.parametrize("input, result",[
    ([4,3,2,0], 0),
    ([1,2,3,4], 1),
    ([4,2,3,2,5], 2),
    ([4,3,2,1,2,3,2,4], 1),
])
async def test_min(contract, input, result):
    execution_info = await contract.min(input).invoke()
    assert execution_info.result.min == result

@pytest.mark.asyncio
async def test_min_emptyArray(contract):
    with pytest.raises(Exception) as execution_info:
        await contract.min([]).invoke()
    assert "Empty array" in execution_info.value.args[1]["message"]


@pytest.mark.asyncio
@pytest.mark.parametrize("input, result",[
    ([2,1,2,3,4,3,2], 1),
    ([1,2,3,4],  0),
    ([4,3,2,1], 3),
    ([1,4,3,2,1], 4),
])
async def test_index_of_min(contract,input, result):
    execution_info = await contract.index_of_min(input).invoke()
    assert execution_info.result.index == result

@pytest.mark.asyncio
async def test_index_of_min_emptyArray(contract):
    with pytest.raises(Exception) as execution_info:
        await contract.index_of_min([]).invoke()
    assert "Empty array" in execution_info.value.args[1]["message"]

@pytest.mark.asyncio
@pytest.mark.parametrize("input, result",[
    ([4,3,2,1], 4),
    ([1,2,3,4], 4),
    ([4,2,3,2,5], 5),
    ([1,2,3,4,3,2,1], 4)
])
async def test_max(contract, input, result):
    execution_info = await contract.max(input).invoke()
    assert execution_info.result.max == result

@pytest.mark.asyncio
async def test_max_emptyArray(contract):
    with pytest.raises(Exception) as execution_info:
        await contract.max([]).invoke()
    assert "Empty array" in execution_info.value.args[1]["message"]


@pytest.mark.asyncio
@pytest.mark.parametrize("input, result",[
    ([1,2,3,4,3,2,1], 3),
    ([4,3,2,1], 0),
    ([1,2,3,4], 3),
    ([4,1,3,2,4], 4),
])
async def test_index_of_max(contract, input, result):
    execution_info = await contract.index_of_max(input).invoke()
    assert execution_info.result.index == result

@pytest.mark.asyncio
async def test_index_of_max_emptyArray(contract):
    with pytest.raises(Exception) as execution_info:
        await contract.index_of_max([]).invoke()
    assert "Empty array" in execution_info.value.args[1]["message"]


@pytest.mark.asyncio
@pytest.mark.parametrize("input, item,result",[
    ([4,2,3,2,5], 2, 2),
    ([2,4,3,5,2], 2, 2),
    ([4,2,3,2,5], 42, 0),
    ([3,3,3,3], 3, 4),
])
async def test_occurrences_of(contract, input, item,result):
    execution_info = await contract.occurrences_of(input, item).invoke()
    assert execution_info.result.occurrences == result
