from brownie import accounts, config, SimpleStorage, network
from brownie.network.gas.strategies import GasNowStrategy

gas_strategy = GasNowStrategy("fast")


def deploy_simple_storage():
    account = get_account()
    print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrive()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrive()
    print(updated_stored_value)


def get_account():  #  check if its on development network, else pull the key from config file
    if network.show_active() == "development":  # network is a brownie keyword
        return accounts[0]

    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()


# 0xCABFC5FC6B490EBCC6FFE3A44885B0AE17242C1D
# 0xCA0BAC32979610CBE79A00E93E5095FEA56E2142
# 0xCA0BAC32979610CBE79A00E93E5095FEA56E2142
