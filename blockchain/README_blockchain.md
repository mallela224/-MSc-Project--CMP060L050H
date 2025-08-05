# Blockchain Integration Guide

## 1. Compile the Solidity Contract

Use Remix IDE or solc to compile `TransactionRecord.sol` in `blockchain/contracts/`.
- Export the ABI as `TransactionRecord_abi.json`.
- Export the bytecode as `TransactionRecord_bytecode.txt`.
- Save both files in `blockchain/contracts/`.

## 2. Deploy the Contract (using web3.py or Remix)
- Deploy to Ganache (http://127.0.0.1:7545).
- Save the deployed contract address in `TransactionRecord_address.txt` in the same folder.

## 3. Python Integration
- The utility `buyers/utility/eth_blockchain.py` loads the ABI, bytecode, and address to interact with the contract.
- Use the `record_transaction`, `get_transaction`, and `get_all_transactions` functions in your Django views.

## 4. Ganache Setup
- Download and run Ganache (https://trufflesuite.com/ganache/).
- Use the default RPC server (http://127.0.0.1:7545).
- Use one of the provided accounts and private keys for testing.

## 5. Django Integration Example
- In your buyer/seller views, import and call `record_transaction` after a successful purchase or sale.
- Pass the buyer and seller Ethereum addresses, transaction details, and the private key of the sender.

---

**Note:** Never expose private keys in production. This setup is for local testing only. 