from brownie import SimpleStorage, accounts

# test that the contract starts at 0- calling retrive function
def test_deploy():
    # 1 arranging    (we arrange what we wanna test)
    account = accounts[0]

    # 2act   (deply the contract, and call the funct to test)
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrive()
    expected = 0  # assign the var here, because it is the act part (just to keep the structture mantained of testing)

    # 3assert    (compare and assert the testing values)

    assert starting_value == expected


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 15
    txn = simple_storage.store(expected, {"from": account})
    txn.wait(1)
    # Assert
    assert expected == simple_storage.retrive()
