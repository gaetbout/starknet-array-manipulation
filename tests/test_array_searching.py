import os

import pytest
from starkware.starknet.testing.starknet import Starknet
CONTRACT_FILE = os.path.join("contracts", "array_searching.cairo")

@pytest.fixture
async def contract():
    starknet = await Starknet.empty()
    return await starknet.deploy(source=CONTRACT_FILE,)

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


@pytest.mark.asyncio
@pytest.mark.occurrences_of
async def test_occurrences_of(contract):
    execution_info = await contract.occurrences_of([4,2,3,2,5], 2).invoke()
    assert execution_info.result.occurrences == 2

@pytest.mark.asyncio
@pytest.mark.occurrences_of
async def test_occurrences_of_beginAndEnd(contract):
    execution_info = await contract.occurrences_of([2,4,3,5,2], 2).invoke()
    assert execution_info.result.occurrences == 2

@pytest.mark.asyncio
@pytest.mark.occurrences_of
async def test_occurrences_of_notThere(contract):
    execution_info = await contract.occurrences_of([4,2,3,2,5], 42).invoke()
    assert execution_info.result.occurrences == 0


@pytest.mark.asyncio
@pytest.mark.occurrences_of
async def test_occurrences_of_fullOf3(contract):
    execution_info = await contract.occurrences_of([3,3,3,3], 3).invoke()
    assert execution_info.result.occurrences == 4


