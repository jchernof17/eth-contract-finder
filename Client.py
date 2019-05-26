from web3 import Web3
import Host
class Client():

    def __init__(self, address, host = Host.url):
        try:
            self.web3 = Web3(Web3.HTTPProvider(host))
        except Exception as e:
            print("Could not connect with host", host, "and address", str(address))
            raise e;

        if self.web3.isConnected():
            self.result = True
            self.address = address
        else:
            print('Unable to connect with host', host, 'and address', str(address))
            self.result = False
            exit()

    ''' Gets latest block (blockHeight) 
        returns: an integer block number. '''
    def getBlockNumber(self):
        return self.web3.eth.blockNumber

    '''Checks if block has seen this contract
        returns: True if contract appears in blockHeight block
        returns: False otherwise'''
    def containsContract(self, block):
        bytecode = self.web3.eth.getCode(self.address, hex(block))
        return True if bytecode else False
    
    '''Helper function to start recursive search
        returns: an integer block number'''
    def findFirstContractBlock(self):
        high = self.getBlockNumber()
        low = 0
        mid = (high + low + 1) // 2 # rounds up
        return self.search(high, low, mid)

    '''binary searches from blockNumber to find first block that contains
        the contract whose previous block does not contain the contract.
        returns: an integer block number.
        INVARIANTS: 
        - high ALWAYS contains contract (True)
        - low NEVER contains contract  (False)'''
    def search(self, high, low, mid):
        if high - low == 1:
            return high
        elif self.containsContract(mid): # if mid returns True (i.e., is too high)
            newMid = (mid + low) // 2
            return self.search(mid, low, newMid)
        else: # mid is too low
            newMid = (mid + high) // 2 # if mid returns False (i.e., is too low)
            return self.search(high, mid, newMid)

    '''gets block hash from block number and transaction hash that matches contract
        returns: tuple (hexCode hash of block, hexCode hash of transaction)'''
    def getHashes(self, b):
        block = self.web3.eth.getBlock(b)
        blockHash = block['hash'].hex()

        # find transaction in list of block's transactions
        assert(block['transactions']) # affirms that there are > 0 txns associated with the block
        for tx in block['transactions']:
            txHash = tx.hex()

            # get transaction receipt corresponding to transaction
            txReceipt = self.web3.eth.getTransactionReceipt(txHash)
            if (txReceipt['contractAddress'] == self.address):
                return (blockHash, txHash)
        return None
