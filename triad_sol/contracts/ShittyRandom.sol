//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.0;
import "hardhat/console.sol";



contract ShittyRandom {

    function requestRandomNumber(uint number) public view returns (uint) {
        bytes memory packedStr = abi.encodePacked(block.timestamp, block.difficulty, msg.sender, number);
        uint randomInt = uint(keccak256(packedStr));
        // console.log("randomHash: ");
        // console.logBytes32(randomHash);
        return randomInt % number;
    }
}