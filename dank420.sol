// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Dank420Token is ERC20, Ownable {
    uint256 public constant INITIAL_SUPPLY = 4_200_000_000 * 10 ** 18; // 4.2 billion tokens
    uint256 public constant BURN_AMOUNT = 4.2 * 10 ** 18; // 4.20 tokens per transaction

    // Events
    event TokensBurned(address indexed from, uint256 amount);

    constructor() ERC20("Dank420", "DANK") {
        _mint(msg.sender, INITIAL_SUPPLY); // Mint initial supply to contract deployer
    }

    // Override transfer function to include burn logic
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 burnAmount = (amount >= BURN_AMOUNT) ? BURN_AMOUNT : 0; // Ensure burn amount is available
        uint256 sendAmount = amount - burnAmount; // Deduct burn amount from transfer amount

        if (burnAmount > 0) {
            _burn(_msgSender(), burnAmount);
            emit TokensBurned(_msgSender(), burnAmount);
        }

        return super.transfer(recipient, sendAmount);
    }

    // Override transferFrom function to include burn logic for allowances
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        uint256 burnAmount = (amount >= BURN_AMOUNT) ? BURN_AMOUNT : 0;
        uint256 sendAmount = amount - burnAmount;

        if (burnAmount > 0) {
            _burn(sender, burnAmount);
            emit TokensBurned(sender, burnAmount);
        }

        return super.transferFrom(sender, recipient, sendAmount);
    }

    // Additional functionality for staking or DAO governance can be added later
    // Placeholder for staking implementation
}
