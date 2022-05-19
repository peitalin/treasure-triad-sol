//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.0;
import '@openzeppelin/contracts/token/ERC20/IERC20.sol';
import '@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol';

enum Skill {
    fireball,
    watergun,
    stun
}

// open-source contract for community members to fork and create art for
// then they apply to be "monster of the week" and we deploy it.
contract WorldBoss2 {

    mapping(address => uint) participants;
    mapping(address => uint) hasClaimed;

    using SafeERC20 for IERC20;

    uint head_HP;
    uint arm_HP;
    uint body_HP;
    uint leg_HP;
    string background = "";
    string boss_art = "";
    IERC20 public magic;
    address monsterCreator;

    constructor() {
        head_HP = 50;
        arm_HP = 50;
        body_HP = 100;
        leg_HP = 100;
        background = "ipfs://some_gree_myth_background.png";
        boss_art = "ipfs://some_greek_myth_boss.npng";
        monsterCreator = msg.sender;
    }

    function isBossStillAlive() public view returns ( bool ) {
        if (head_HP > 0) return true;
        if (arm_HP > 0) return true;
        if (body_HP > 0) return true;
        if (leg_HP > 0) return true;
        return false;
    }

    function claimRewardsOnDeath() public {
        if (!isBossStillAlive()) {
            if (msg.sender == monsterCreator) {
                magic.safeTransferFrom(address(this), monsterCreator, 10_000);
            } else {
                if (participants[msg.sender] == 1) {
                    if (hasClaimed[msg.sender] == 0) {
                        magic.safeTransferFrom(address(this), msg.sender, 40);
                        hasClaimed[msg.sender] = 1;
                    }
                }
            }
        }
    }

    modifier alreadyParticipated() {
        if (participants[msg.sender] == 1) revert("already participated");
        _;
    }

    function attackHead(Skill _skill) public alreadyParticipated() {
        if (head_HP > 0) {
            head_HP -= 1;
            participants[msg.sender] = 1;
            // register this life as a participant for reward
        }
    }

    function attackArms(Skill _skill) public alreadyParticipated() {
    }

    function attackBody(Skill _skill) public alreadyParticipated() {
    }

    function attackLeg(Skill _skill) public alreadyParticipated() {
    }
}

