import os
import click

from ape import project

from ape.cli import ConnectedProviderCommand, account_option

CURVE_AGENT = os.getenv('CURVE_AGENT')
GRANTEE = os.getenv('GRANTEE')
TOKEN = os.getenv('TOKEN')

@click.group()
def cli():
    pass

@click.command(cls=ConnectedProviderCommand)
@account_option()
def info(ecosystem, provider, account, network):
    click.echo(f"ecosystem: {ecosystem.name}")
    click.echo(f"network: {network.name}")
    click.echo(f"provider_id: {provider.chain_id}")
    click.echo(f"connected: {provider.is_connected}")
    click.echo(f"account: {account}")


@click.command(cls=ConnectedProviderCommand)
@account_option()
def deploy(ecosystem, provider, account, network):

    if ecosystem.name is "arbitrum":
        click.echo("do this")

    deploy = account.deploy(project.GrantController, CURVE_AGENT, GRANTEE, TOKEN, max_priority_fee="1000 wei", max_fee="0.1 gwei", gas_limit="100000")

cli.add_command(info)
cli.add_command(deploy)