import { ethers } from "hardhat";
import { Signer } from "ethers";

import { expect } from "chai"
import { TreasureTriad, TreasureCardStructOutput } from "../typechain-types/TreasureTriad";
import { TreasureTriadCardStats } from "../typechain-types/TreasureTriadCardStats";


enum Player {
	nature = 0,
	user = 1,
	none = 2,
}



describe("TreasureTriad", function () {

    // declare some variables, and assign them in the `before` and `beforeEach` callbacks.
    let TreasureTriad
    let TreasureTriadCardStats
    let tTriad: TreasureTriad
    let ttCardStats: TreasureTriadCardStats
    let owner
    let addr1
    let addrs

    // `beforeEach` runs before each test, re-deploying the contract every time.
    beforeEach(async function () {
        // Get the ContractFactory and Signers here.
        TreasureTriad = await ethers.getContractFactory("TreasureTriad");
        TreasureTriadCardStats = await ethers.getContractFactory("TreasureTriadCardStats");
        [owner, addr1, ...addrs] = await ethers.getSigners();

        let gridSize = 3
        tTriad = await TreasureTriad.deploy();
        await tTriad.initialize(gridSize);
        ttCardStats = await TreasureTriadCardStats.deploy();
    });


	it("Lookup cards [ox, cow, donkey] have correct stats", async function () {
		try {
			await tTriad.stakeTreasureCard(0, 0, "ox");
		} catch(e) {
			console.log(e)
		}
		try {
			await tTriad.stakeTreasureCard(0, 1, "cow");
		} catch(e) {
			console.log(e)
		}
		try {
            await tTriad.stakeTreasureCard(0, 2, "donkey");
		} catch(e) {
			console.log(e)
		}
		const oxCard = await tTriad.getCardAtCell(0, 0);
		const cowCard = await tTriad.getCardAtCell(0, 1);
		const donkeyCard = await tTriad.getCardAtCell(0, 2);

		const ox = await ttCardStats.getCard(oxCard);
		const cow = await ttCardStats.getCard(cowCard);
		const donkey = await ttCardStats.getCard(donkeyCard);

		expect(ox.n.toNumber()).to.equal(5)
		expect(cow.n.toNumber()).to.equal(4)
		expect(donkey.n.toNumber()).to.equal(5)

	})


	it("Stakes cards and flips cards", async function () {

		const printGrid = async () => {
			const _c00 = await tTriad.getCardAtCell(0, 0);
			const _c01 = await tTriad.getCardAtCell(0, 1);
			const _c02 = await tTriad.getCardAtCell(0, 2);
			const _c10 = await tTriad.getCardAtCell(1, 0);
			const _c11 = await tTriad.getCardAtCell(1, 1);
			const _c12 = await tTriad.getCardAtCell(1, 2);
			const _c20 = await tTriad.getCardAtCell(2, 0);
			const _c21 = await tTriad.getCardAtCell(2, 1);
			const _c22 = await tTriad.getCardAtCell(2, 2);

			const row0 = [
				fmt(_c00.treasure, _c00.player),
				fmt(_c01.treasure, _c01.player),
				fmt(_c02.treasure, _c02.player)
			].join(",\t")
			const row1 = [
				fmt(_c10.treasure, _c10.player),
				fmt(_c11.treasure, _c11.player),
				fmt(_c12.treasure, _c12.player)
			].join(",\t")
			const row2 = [
				fmt(_c20.treasure, _c20.player),
				fmt(_c21.treasure, _c21.player),
				fmt(_c22.treasure, _c22.player)
			].join(",\t")
			console.log("[", row0, "]")
			console.log("[", row1, "]")
			console.log("[", row2, "]")
			console.log("\n")
		}

		console.log("\nBefore: ")
		await printGrid();


		const tryStakeAndPrint = async (row: number, col: number, treasure: string, player: string) => {
			try {
				if (player === 'nature') {
					await tTriad.stakeTreasureCardAsNature(row, col, treasure);
				} else {
					await tTriad.stakeTreasureCard(row, col, treasure);
				}
			} catch(e) {
				console.log(e)
			} finally {
				await printGrid();
			}
		}


		let c00: TreasureCardStructOutput
		let c01: TreasureCardStructOutput
		let c02: TreasureCardStructOutput
		let c10: TreasureCardStructOutput
		let c11: TreasureCardStructOutput
		let c12: TreasureCardStructOutput
		let c20: TreasureCardStructOutput
		let c21: TreasureCardStructOutput
		let c22: TreasureCardStructOutput


		console.log("Staking dragon tail in: ", [0,1])
		await tryStakeAndPrint(0, 1, "dragon tail", "nature");
		c01 = await tTriad.getCardAtCell(0, 1)
		expect(c01.treasure).to.equal("dragon tail")
		expect(c01.player).to.equal(Player.nature) // nature: 0


		console.log("Staking honeycomb in: ", [0,0])
		await tryStakeAndPrint(0, 0, "honeycomb", "user");
		c01 = await tTriad.getCardAtCell(0, 1)
		c00 = await tTriad.getCardAtCell(0, 0)
		expect(c01.treasure).to.equal("dragon tail")
		expect(c01.player).to.equal(Player.user)
		expect(c00.treasure).to.equal("honeycomb")
		expect(c00.player).to.equal(Player.user)


		console.log("Staking grin in: ", [1,0])
		await tryStakeAndPrint(1, 0, "grin", "nature");
		c00 = await tTriad.getCardAtCell(0, 0)
		c10 = await tTriad.getCardAtCell(1, 0)
		expect(c00.treasure).to.equal("honeycomb")
		expect(c00.player).to.equal(Player.user)
		expect(c10.treasure).to.equal("grin")
		expect(c10.player).to.equal(Player.nature)

		console.log("Staking ox in: ", [1,2])
		await tryStakeAndPrint(1, 2, "ox", "user");
		console.log("Staking bottomless elixer in: ", [0,2])
		await tryStakeAndPrint(0, 2, "bottomless elixer", "nature");
		c01 = await tTriad.getCardAtCell(0, 1)
		c02 = await tTriad.getCardAtCell(0, 2)
		c12 = await tTriad.getCardAtCell(1, 2)
		expect(c01.treasure).to.equal("dragon tail")
		expect(c01.player).to.equal(Player.nature)
		expect(c02.treasure).to.equal("bottomless elixer")
		expect(c02.player).to.equal(Player.nature)
		expect(c12.treasure).to.equal("ox")
		expect(c12.player).to.equal(Player.nature)

		console.log("Staking donkey in: ", [1,1])
		await tryStakeAndPrint(1, 1, "donkey", "user");
		c01 = await tTriad.getCardAtCell(0, 1)
		c10 = await tTriad.getCardAtCell(1, 0)
		c11 = await tTriad.getCardAtCell(1, 1)
		c12 = await tTriad.getCardAtCell(1, 2)
		expect(c01.treasure).to.equal("dragon tail")
		expect(c01.player).to.equal(Player.user)
		expect(c10.treasure).to.equal("grin")
		expect(c10.player).to.equal(Player.user)
		expect(c11.treasure).to.equal("donkey")
		expect(c11.player).to.equal(Player.user)
		expect(c12.treasure).to.equal("ox")
		expect(c12.player).to.equal(Player.user)

		console.log("Staking small bird in: ", [2,2])
		await tryStakeAndPrint(2, 2, "small bird", "nature");
		c12 = await tTriad.getCardAtCell(1, 2)
		c22 = await tTriad.getCardAtCell(2, 2)
		expect(c12.treasure).to.equal("ox")
		expect(c12.player).to.equal(Player.nature)
		expect(c22.treasure).to.equal("small bird")
		expect(c22.player).to.equal(Player.nature)

		console.log("Staking immovable stone in: ", [2,1])
		await tryStakeAndPrint(2, 1, "immovable stone", "user");
		c21 = await tTriad.getCardAtCell(2, 1)
		c22 = await tTriad.getCardAtCell(2, 2)
		expect(c21.treasure).to.equal("immovable stone")
		expect(c21.player).to.equal(Player.user)
		expect(c22.treasure).to.equal("small bird")
		expect(c22.player).to.equal(Player.user)


		console.log("Staking red feather in: ", [2,0])
		await tryStakeAndPrint(2, 0, "red feather", "nature");
		c20 = await tTriad.getCardAtCell(2, 0)
		c21 = await tTriad.getCardAtCell(2, 1)
		expect(c20.treasure).to.equal("red feather")
		expect(c20.player).to.equal(Player.nature)
		expect(c21.treasure).to.equal("immovable stone")
		expect(c21.player).to.equal(Player.nature)
	})

})



function fmt(treasure: string, player: number) {
	let _t =  treasure.trim() != "" ? treasure : "------------------"
	let _player = player === 0
		? "Nature"
		: player === 1
			?	"Player"
			: undefined

	if (!_player) {
		return _t
	} else {
		return _t + " " + `(${_player})`
	}
}
