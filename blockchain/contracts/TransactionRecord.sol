// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TransactionRecord {
    struct Transaction {
        uint256 id;
        address buyer;
        address seller;
        string details;
        uint256 timestamp;
    }

    Transaction[] public transactions;
    uint256 public nextId = 1;

    event TransactionRecorded(uint256 id, address indexed buyer, address indexed seller, string details, uint256 timestamp);

    function recordTransaction(address _buyer, address _seller, string memory _details) public {
        transactions.push(Transaction({
            id: nextId,
            buyer: _buyer,
            seller: _seller,
            details: _details,
            timestamp: block.timestamp
        }));
        emit TransactionRecorded(nextId, _buyer, _seller, _details, block.timestamp);
        nextId++;
    }

    function getTransaction(uint256 _id) public view returns (Transaction memory) {
        require(_id > 0 && _id < nextId, "Transaction does not exist");
        return transactions[_id - 1];
    }

    function getAllTransactions() public view returns (Transaction[] memory) {
        return transactions;
    }
} 