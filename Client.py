from web3 import Web3
from web3.contract import ConciseContract
from web3.auto import w3
import time
class Client():

    def __init__(self, address, host, abi):
        self.web3 = Web3(Web3.WebsocketProvider(host))

        if (self.web3.isConnected()):
            self.contract = self.web3.eth.contract(address=address, abi=abi)
            self.concise = ConciseContract(self.contract)
            self.result = True
            self.address = address
        else:
            print('Unable to connect with host', host, 'and address', str(address))
            self.result = False

    ''' Prints all functions applicable to Contract object '''
    def printFunctions(self):
        print(self.contract.all_functions())

    ''' Prints Connection Status '''
    def printConnectionResult(self):
        if (self.result):
            print("Connected")
        else:
            print("Not connected")

    ''' Gets Contract object '''
    def printContract(self):
        print(self.contract)

    ''' Gets Transaction hash from block and transaction index '''
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
        return self.web3.eth.blockNumber

    def getReceipt(self, tx):
        receipt = self.web3.eth.getTransactionReceipt(tx)
        return receipt['contractAddress']

    def createEventFilter(self):
        ''' self.contract '''
        events = self.contract.events
        filter = self.web3.eth.filter({'address': self.address})
        print("Successfully created filter",filter)

    def handle_event(event):
        print(event)
    def log_loop(event_filter, poll_interval):
        while True:
            for event in event_filter.get_new_entries():
                handle_event(event)
            time.sleep(poll_interval)    

    def listen(self):
        events = self.contract.events
        lst = []
        transfers = events.Transfer()
        #print(dir(transfers))

        print('~~Getting events log~~')
        print('')
        log_filter = transfers.createFilter(fromBlock=7829800, address=self.address)
        
        print(log_filter.get_all_entries())
        # print(events._events)