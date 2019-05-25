from web3 import Web3
from web3.contract import ConciseContract
class Client():

    def __init__(self, address, host, abi):
        self.web3 = Web3(Web3.HTTPProvider(host))
        if (self.web3.isConnected()):
            self.contract = self.web3.eth.contract(address=address, abi=abi)
            self.concise = ConciseContract(self.contract)
        else:
            print('Unable to connect with host', host, 'and address', str(address))
            self.result = False
            return
        self.result = True

    def getFunctions(self):
        print(self.contract.all_functions())

    def getResult(self):
        if (self.result):
            print("Connected")
        else:
            print("Not connected")

    def getContract(self):
        print(self.contract)
