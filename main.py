import sys
import Client as c

'''
argv => [main.py, contractID, --host, host]
'''

# parse input
if len(sys.argv) != 4:
    print("Enter transaction and address, e.g.:")
    print("python main.py 0x... --host https://mainnet.infura.io/v3/[YOUR_ADDRESS_HERE]")
    exit()
else:
    contractID = sys.argv[1]
    # sets Host.url to the host we were provided 
    url = sys.argv[3]

# establish connection to server with host and store contract address
client = c.Client(contractID, url)
assert(client.result)

firstBlock = client.findFirstContractBlock()
hashes = client.getHashes(firstBlock) # tuple of hashes

if not hashes[0] or not hashes[1]:
    print("Problem finding transaction.")
else:
    print("Block:", hashes[0])
    print("Transaction:", hashes[1])

