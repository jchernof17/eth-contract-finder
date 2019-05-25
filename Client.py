from web3 import Web3
from web3.contract import ConciseContract
class Client():

    def __init__(self, address, host, abi):
        self.web3 = Web3(Web3.HTTPProvider(host))
        if (self.web3.isConnected()):
            self.contract = self.web3.eth.contract(address=address, abi=abi)
            self.concise = ConciseContract(self.contract)
            # self.block = self.web3.eth.filter(fil) # should be logfilter
            self.blockNumber = self.web3.eth.blockNumber
        else:
            print('Unable to connect with host', host, 'and address', str(address))
            self.result = False
            return
        self.result = True

    def getFunctions(self):
        print(self.contract.all_functions())

    def getCode(self):
        a = (self.web3.eth.getCode("0xB9280B318A84df5891610F27625b0741951B94B4"))
        print(a.hex())

    def getResult(self):
        if (self.result):
            print("Connected")
        else:
            print("Not connected")

    def getContract(self):
        print(self.contract)

    def getTx(self, b, i):
        tx = self.web3.eth.getTransactionByBlock(b, i)
        # print("~~~~~~")
        # print("Transaction is",tx) # should not be none
        # print("~~~~~~")
        tx_contract = tx['to']
        # print(tx_contract)
        return tx_contract

    def getNumTransactions(self, b):
        a = self.web3.eth.getBlockTransactionCount(b)
        print("Block",b,"has",a,"transactions")
        return a

    def getHashes(self, b, i):
        tx = self.web3.eth.getTransactionByBlock(b, i)
        return (tx['blockHash'], tx['hash'])

    def getBlockNumber(self):
        return self.blockNumber

    def getReceipt(self, tx):
        receipt = self.web3.eth.getTransactionReceipt(tx)
        return receipt['contractAddress']
        