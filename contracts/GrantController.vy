# @pragma version ^0.4.0
"""
@title GrantController
@author martinkrung for curve.fi
@license MIT
@notice grant controller allows curve dao some control over grants
"""

from ethereum.ercs import IERC20

GRANTEE: immutable(address)
CURVE_AGENT: immutable(address)
TOKEN: immutable(address)

on: public(bool)

@deploy
def __init__(curve_agent: address, grantee: address, token: address):
    CURVE_AGENT = curve_agent
    GRANTEE = grantee
    TOKEN = token
    self.on = True

@external
def switch():
    assert msg.sender == CURVE_AGENT, 'dev: only curve agent can call this function'

    self.on = not self.on
    
@external
def withdraw():
    """
    @notice send all tokens to the grantee or the agent
    """
    assert self.on, 'dev: contract is off'
    assert msg.sender in [CURVE_AGENT, GRANTEE], 'dev: only agent or grantee can call this function'

    amount: uint256 = staticcall IERC20(TOKEN).balanceOf(self)

    assert extcall IERC20(TOKEN).approve(self, amount)
    assert extcall IERC20(TOKEN).transferFrom(self, msg.sender, amount, default_return_value=True)