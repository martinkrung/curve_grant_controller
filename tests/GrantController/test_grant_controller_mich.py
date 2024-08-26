import ape
import pytest
import sys


def test_grant_controller_on(alice, grant_controller_mich):
    assert grant_controller_mich.enabled() == True


def test_grant_controller_enabled(bob, agent, grant_controller_mich):
    assert grant_controller_mich.set_enabled(True, sender=agent)
    assert grant_controller_mich.enabled() == True
    assert grant_controller_mich.set_enabled(False, sender=agent)
    assert grant_controller_mich.enabled() == False

def test_grant_controller_enabled_revert(bob, grant_controller_mich):
    with ape.reverts():
        assert grant_controller_mich.set_enabled(True, sender=bob)

def test_grant_controller_enabled(alice, bob, crv, grant_controller_mich):
    quantity = 10 ** 18 # 1 token
    # token to contract
    crv.transfer(grant_controller_mich, quantity, sender=alice)
    # check if grant_controller_mich has the token
    assert crv.balanceOf(grant_controller_mich) == quantity
    balance = crv.balanceOf("0xE4F02AcCC88A3000f11aFeC71C04896127a3aeB5") 
    # withdraw from contract
    grant_controller_mich.claim_all(sender=bob)
    # check if charlie has the token
    assert crv.balanceOf("0xE4F02AcCC88A3000f11aFeC71C04896127a3aeB5") == balance + quantity
    # check if grant_controller_mich has no token
    assert crv.balanceOf(grant_controller_mich) == 0


def test_grant_controller_disabled(alice, bob, agent, crv, grant_controller_mich):
    assert grant_controller_mich.set_enabled(False, sender=agent)
    assert grant_controller_mich.enabled() == False

    quantity = 10 ** 18 # 1 token
    # token to contract
    crv.transfer(grant_controller_mich, quantity, sender=alice)
    # check if grant_controller_mich has the token
    assert crv.balanceOf(grant_controller_mich) == quantity
    balance = crv.balanceOf("0x40907540d8a6C65c637785e8f8B742ae6b0b9968") 
    # withdraw from contract
    grant_controller_mich.claim_all(sender=bob)
    # check if charlie has the token
    assert crv.balanceOf("0x40907540d8a6C65c637785e8f8B742ae6b0b9968") == balance + quantity
    # check if grant_controller_mich has no token
    assert crv.balanceOf(grant_controller_mich) == 0
