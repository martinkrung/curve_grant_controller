import ape
import pytest
import os

@pytest.fixture(scope="session")
def alice(accounts):
    return accounts[0]

@pytest.fixture(scope="session")
# manager address
def bob(accounts):
    return accounts[1]

@pytest.fixture(scope="session")
# recovery address
# backup manager address
def charlie(accounts):
    return accounts[2]

@pytest.fixture(scope="session")
def agent(accounts):
    CURVE_AGENT = os.getenv('CURVE_AGENT')
    agent = accounts[CURVE_AGENT]
    agent.balance = "1000 ETH"
    return agent

@pytest.fixture(scope="session")
def binance(accounts):
    # binance address with  CRV
    BINANCE = '0x5a52E96BAcdaBb82fd05763E25335261B270Efcb'
    binance = accounts[BINANCE]
    return binance
