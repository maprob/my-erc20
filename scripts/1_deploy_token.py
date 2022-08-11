from brownie import accounts, config, MyERC20Token

init_supply = 1e+18
token_name = "MyERC20Token"
token_symbol = "MYTKN"

def main():
    acc = accounts.add(config["wallets"]["from_key"])
    erc20 = MyERC20Token.deploy(
        init_supply, {"from": acc}, publish_source=True
    )