//SPDX-License-Identifier: MIT
//original code is from nftschool.dev
// deployed at rinkeby 0x77357b8F73Fe0300E0990438F977Eb77D57Fc7CE


pragma solidity ^0.7.0;

// @dev change the openzeppelin paths if you are using this contract locally with hardhat
// @dev uncomment the following line if you are using hardhat locally 

// import "hardhat/console.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v3.4/contracts/token/ERC721/ERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v3.4/contracts/utils/Counters.sol";

contract UrbanMinter is ERC721 {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    constructor(string memory tokenName, string memory symbol) ERC721(tokenName, symbol) {
        _setBaseURI("ipfs://");
    }

    function mintToken(address owner, string memory metadataURI)
    public
    returns (uint256)
    {
        _tokenIds.increment();

        uint256 id = _tokenIds.current();
        _safeMint(owner, id);
        _setTokenURI(id, metadataURI);

        return id;
    }
}
