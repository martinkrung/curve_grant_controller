# @pragma version ^0.4.0

from ethereum.ercs import IERC20

ADMIN: public(constant(address)) = 0x40907540d8a6C65c637785e8f8B742ae6b0b9968
RECEIVER: public(constant(address)) = 0xE4F02AcCC88A3000f11aFeC71C04896127a3aeB5
TOKEN: public(constant(address)) = 0xD533a949740bb3306d119CC777fa900bA034cd52

enabled: public(bool)


@deploy
def __init__():
    self.enabled = True


@external
def set_enabled(toggle: bool):
    assert msg.sender == ADMIN
    self.enabled = toggle


@external
def claim_all():
    quantity: uint256 = staticcall IERC20(TOKEN).balanceOf(self)
    recipient: address = ADMIN
    if self.enabled:
        recipient = RECEIVER
    extcall IERC20(TOKEN).transfer(recipient, quantity)
    
@external
def claim_all_limited():
    quantity: uint256 = staticcall IERC20(TOKEN).balanceOf(self)
    recipient: address = ADMIN
    if self.enabled:
        recipient = RECEIVER
        extcall IERC20(TOKEN).transfer(recipient, quantity)
    else:
        assert msg.sender == ADMIN
        extcall IERC20(TOKEN).transfer(recipient, quantity)