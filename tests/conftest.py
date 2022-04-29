
import pytest
import asyncio
from starkware.starknet.testing.starknet import Starknet

'''Fix asyncio crash'''
@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()
    
@pytest.fixture(scope="session")
async def starknet():
    return await Starknet.empty()
    