import ape
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
def grant_controller(project, alice, bob, charlie, token):

    CURVE_AGENT =  bob
    GRANTEE = charlie
    TOKEN =  token

    grant_controller = alice.deploy(project.GrantController, CURVE_AGENT, GRANTEE, TOKEN)
    # token.approve(grant_controller, 10 ** 19, sender=bob) 
    print(grant_controller)
    return grant_controller