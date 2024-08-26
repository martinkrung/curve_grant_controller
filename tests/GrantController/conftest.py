import ape
from ape import Contract
import pytest

@pytest.fixture(scope="module")
def token(project, alice):
    token = alice.deploy(project.TestToken)
    # mint token to alice
    token.mint(alice, 10 ** 19, sender=alice)
    token.approve(alice, 10 ** 19, sender=alice) 
    balance = token.balanceOf(alice)
    print(balance)
    return token

@pytest.fixture(scope="module")
def crv(project, alice, binance):
   
    crv = Contract('0xD533a949740bb3306d119CC777fa900bA034cd52')
    amount = 10 ** 19
    # send crv to alice
    crv.transfer(alice, amount, sender=binance)
    return crv

@pytest.fixture(scope="module")
def grant_controller(project, alice, bob, charlie, token):

    CURVE_AGENT =  bob
    GRANTEE = charlie
    TOKEN =  token

    grant_controller = alice.deploy(project.GrantController, CURVE_AGENT, GRANTEE, TOKEN)
    # token.approve(grant_controller, 10 ** 19, sender=bob) 
    return grant_controller

@pytest.fixture(scope="module")
def grant_controller_mich(project, alice, bob, charlie, token):
    grant_controller_mich = alice.deploy(project.GrantControllerMich)
    return grant_controller_mich
