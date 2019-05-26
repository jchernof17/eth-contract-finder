# eth-contract-finder
Finds ethereum transactions and their corresponding blocks from a single contract using command-line interface. Uses web3 version 4.9.2 and Python 3.6.5.
# Setup
1. Install web3 from pip
```
pip install web3
```
2. Get an API key from https://infura.io/
3. (Optional, for testing) Add host address to Host file.
# Using the app
Run main.py with arguments contract | --host | hostURL
```
python main.py 0x_YOUR_CONTRACT_ADDRESS_HERE --host https://mainnet.io/v3/(YOUR_HOST_HERE)
```
# About
This app uses the binary search method to find a non-null bytecode corresponding to the given contract in O(logN) time. It then iterates through the transactions associated with the bytecode's block in O(t) for t transactions in the block, checking for the first transaction receipt with a contract address match. It returns the block hash and the transaction hash associated with the creation of the contract.
