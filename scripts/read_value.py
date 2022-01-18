from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[
        -1
    ]  # this will store the address of recently deployed contract to the variable! -1 coz it will be the recent added index
    # to interact with a contract, we need address and ABI of the contract
    # address we get from above code line, and brownei also knows the ABI in SimpleStorage.json
    # so the contract is readily available to interact with
    print(simple_storage.retrive())


def main():
    read_contract()
