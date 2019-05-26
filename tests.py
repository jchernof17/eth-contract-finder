import Client as c
import Host

def testHashes(contractID, desiredBlockHash, desiredTxHash):
    client = c.Client(contractID, Host.url)
    assert(client.result)
    firstBlock = client.findFirstContractBlock()
    hashes = client.getHashes(firstBlock)
    assert(hashes == (desiredBlockHash, desiredTxHash))

# high-transaction contract
testHashes("0xDd806c4fDAd2949a97Fda79036cfbb8750181b37", "0xc34c71d35dfd976c4d127fdaba0d2e162c97f022dfc0ee7d63b485e662e1569e", "0x66bb8f89495649d752392edf850278ebb51d724a889cfb146d872fee7457f5ca")

# relatively new contract
testHashes("0x95cEe155a405c45B1C5fE5328B4618AcEDd9BE8D", "0x40f800aa5c65e7c417b2a52f096b547dedc9c3341a3c13d9b701666b22b5b3df","0x152de91756abcc4db6c2d91bc0dec83292e141a27a528fe36b5e227601bf6a63")

# very old contract 
testHashes("0x0C5aE4C0b13f935085C4B204d132111f571a17c2", "0x9936df789378469def378bcacc01cd1bc8dbcc0244e83ddf5860f527a5dd6c85", "0x71d634cd5067810c9c35285be77a3a3be6a48231a945d6cf1f1a595c4164be5a")