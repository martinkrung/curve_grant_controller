import ape
import pytest
import sys


def test_grant_controller_on(alice, grant_controller):
    assert grant_controller.on() == True


def test_grant_controller_switch(bob, grant_controller):
    # bob is the curve agent
    assert grant_controller.on() == True
    assert grant_controller.switch(sender=bob)
    assert grant_controller.on() == False

def test_grant_controller_withdraw(alice, bob, charlie, token, grant_controller):
    # charlie is the grantee
    amount = 10 ** 18 # 1 token
    # token to contract
    token.transfer(grant_controller, amount, sender=alice)
    # check if grant_controller has the token
    assert token.balanceOf(grant_controller) == amount
    # withdraw from contract
    grant_controller.withdraw(sender=charlie)
    # check if charlie has the token
    assert token.balanceOf(charlie, sender=alice) == amount
    # check if grant_controller has no token
    assert token.balanceOf(grant_controller) == 0

def test_grant_controller_withdraw_agent(alice, bob, charlie, token, grant_controller):
    # bob is the curve agent
    amount = 10 ** 18 # 1 token
    # token to contract
    token.transfer(grant_controller, amount, sender=alice)
    # check if grant_controller has the token
    assert token.balanceOf(grant_controller) == amount
    # switch off
    assert grant_controller.switch(sender=bob)
    # withdraw from contract
    grant_controller.withdraw(sender=bob)
    # check if bob has the token
    assert token.balanceOf(bob) == amount
    # check if grant_controller has no token
    assert token.balanceOf(grant_controller) == 0

def test_grant_controller_revert(alice, bob, grant_controller):
    # bob is the curve agent
    # charlie is the grantee
    assert grant_controller.switch(sender=bob)

    with ape.reverts("dev: only agent on off"):
        grant_controller.withdraw(sender=alice)