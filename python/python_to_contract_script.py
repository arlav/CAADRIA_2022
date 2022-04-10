contract_address = "0x9f70575c34B3A734b619efC4e9C286a687Cf0fc3" #this should be the contract on Skale
wallet_address = "0x6F4ab987479Bd1981E702bf402Ae3c42b7eB9d70" #Skale account- replace with wallet and key credentials under .git ignore
wallet_private_key = "0x56033accd5dd93e4416d0564a76594fcda2a09f62afb69f92584110fd3101f5f"
infura_url = "https://rinkeby.infura.io/v3/029c7ec526724b59b345469899f0dd9e" #Theo's infura Node


#@dev: entries to use with the anaconda python inside blender/dynamo/Grrasshopper

#path = "~/Downloads/blender-2.92.0-linux64/2.92/python/lib/python3.7/site-package" # #enter your web3 location here - This is the Linux version (H1c0)
path = "/opt/anaconda3/lib/python3.8/site-packages" #enter your web3 location here - This is the macosx version
#path = "c:\\Users\\calys\\anaconda3\\envs\\Dynamo383\\Lib\\site-packages" #enter your web3 location here - This is the windows version

#@dev:insert here the compiled contract abi - change the json to one line and insert \" for every "
contract_abi =  " FILL IN THE CONTRACT ABI HERE"


import time
import sys
sys.path.append(path)
from web3 import Web3, HTTPProvider

#following linees make topologic work on linux with Blender
#from topologic import Vertex, Topology
#import cppyy

#v = Vertex.ByCoordinates(10,20,30)
string = str('ipfs://')
w3 = Web3(HTTPProvider(infura_url))

w3.isConnected()
w3.eth.isConnected()
w3.eth.get_balance('0x6F4ab987479Bd1981E702bf402Ae3c42b7eB9d70')
w3.api
w3.clientVersion
w3.eth.get_block('latest')
web3.eth.block_number()
w3.eth.block_number()

smartContract = w3.eth.contract(address=contract_address, abi=contract_abi)

receipts = []

#the next function call mints the NFT
nonce = w3.eth.get_transaction_count(wallet_address)
tx_dict = smartContract.functions.mintToken(address, string).buildTransaction({
    'chainId' : 4, #be careful when changing test networks- the chainID will change.
    'gas' : 9100000,  #some of this was throwing errors, double check gas amounts.
    'gasPrice' : w3.toWei('01', 'gwei'),
    'nonce' : nonce,
})



signed_tx = w3.eth.account.sign_transaction(tx_dict, wallet_private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash, timeout=120, poll_latency=0.1)
receipts.append(tx_receipt)



outputList = []
for tx_receipt in receipts:
    receipt = []
    receipt.append('blockHash: '+str(tx_receipt['blockHash']))
    receipt.append('blockNumber: '+str(tx_receipt['blockNumber']))
    receipt.append('contractAddress: '+str(tx_receipt['contractAddress']))
    receipt.append('cumulativeGasUsed: '+str(tx_receipt['cumulativeGasUsed']))
    receipt.append('from: '+str(tx_receipt['from']))
    receipt.append('gasUsed: '+str(tx_receipt['gasUsed']))
    receipt.append('logs: '+str(tx_receipt['logs']))
    receipt.append('to: '+str(tx_receipt['to']))
    receipt.append('transactionHash: '+str(tx_receipt['transactionHash']))
    receipt.append('tansactionIndex: '+str(tx_receipt['transactionIndex']))
    outputList.append(receipt)


#amend the outoput list if you are using Topologic on Dynamo.
print(outputList)
