import { ethers } from "hardhat";
import { Signer } from "ethers";

import { expect } from "chai"
import { TreasureTriad, TreasureCardStructOutput } from "../typechain-types/TreasureTriad";
import { TreasureTriadCardStats } from "../typechain-types/TreasureTriadCardStats";
import { ShittyRandom } from "../typechain-types/ShittyRandom";


enum Player {
    nature = 0,
    none = 1,
    range = 2,
    fighter = 3,
    spellcaster = 4,
    seige = 5,
    assassin = 6,
    riverman = 7,
    numeraire = 8,
    common = 9
}



describe("TreasureTriad", function () {

    // declare some variables, and assign them in the `before` and `beforeEach` callbacks.
    let TreasureTriad
    let TreasureTriadCardStats
    let ShittyRandom

    let tTriad: TreasureTriad
    let ttCardStats: TreasureTriadCardStats
    let sRandom: ShittyRandom

    let owner
    let addr1
    let addrs

    // `beforeEach` runs before each test, re-deploying the contract every time.
    beforeEach(async function () {
        // Get the ContractFactory and Signers here.
        TreasureTriad = await ethers.getContractFactory("TreasureTriad");
        TreasureTriadCardStats = await ethers.getContractFactory("TreasureTriadCardStats");
        ShittyRandom = await ethers.getContractFactory("ShittyRandom");

        [owner, addr1, ...addrs] = await ethers.getSigners();

        let gridSize = 3
        tTriad = await TreasureTriad.deploy();
        await tTriad.initialize(gridSize);
        ttCardStats = await TreasureTriadCardStats.deploy();
        sRandom = await ShittyRandom.deploy();
    });


	it("Looks up cards (ox, cow, donkey) with correct stats", async function () {

		let player_legion = Player.assassin
		try {
			await tTriad.stakeTreasureCard(0, 0, "ox", player_legion);
		} catch(e) {
			console.log(e)
		}
		try {
			await tTriad.stakeTreasureCard(0, 1, "cow", player_legion);
		} catch(e) {
			console.log(e)
		}
		try {
			await tTriad.stakeTreasureCard(0, 2, "donkey", player_legion);
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

	it("Nature draws 3 cards without replacement", async function () {

        console.log("Before");
        await printGrid(tTriad)

        const decoder = new ethers.utils.AbiCoder();

        let naturesTx = await tTriad.naturePlacesInitialCards(3);
		let receipt2 = await naturesTx?.wait();
		let logs2 = receipt2?.events?.filter(x => x.event === "NaturesInitialCells") ?? []

		let naturesCells = decoder.decode(
			['uint8[2][]'],
			ethers.utils.hexDataSlice(logs2?.[0]?.data, 0)
		)

        let naturesCards = (await Promise.all(naturesCells?.[0].map(async (cell: number[]) => {
            // console.log("naturesCell", cell[0], cell[1])
            let n1 = await tTriad.getCardAtCell(cell[0], cell[1]);
            // console.log("naturesCell", n1)
            return n1
        }))).filter((card: TreasureCardStructOutput) => !!card.tcard)

		console.log("naturesCards", naturesCards)

        console.log("\nAfter");
        await printGrid(tTriad)


		expect(naturesCards.length).to.equal(3)
		// expect(cow.n.toNumber()).to.equal(4)
		// expect(donkey.n.toNumber()).to.equal(5)
		// expect(parsed[0].length).to.be.eq(numDraws)

	})


	// it("Stakes cards and flips cards", async function () {


	// 	console.log("\nBefore: ")
	// 	await printGrid(tTriad);


	// 	const tryStakeAndPrint = async (row: number, col: number, treasure: string, player: any) => {
	// 		try {
	// 			if (player === 'nature') {
	// 				await tTriad.stakeTreasureCardAsNature(row, col, treasure);
	// 			} else {
	// 				await tTriad.stakeTreasureCard(row, col, treasure, player);
	// 			}
	// 		} catch(e) {
	// 			console.log(e)
	// 		} finally {
	// 			await printGrid(tTriad);
	// 		}
	// 	}


	// 	let c00: TreasureCardStructOutput
	// 	let c01: TreasureCardStructOutput
	// 	let c02: TreasureCardStructOutput
	// 	let c10: TreasureCardStructOutput
	// 	let c11: TreasureCardStructOutput
	// 	let c12: TreasureCardStructOutput
	// 	let c20: TreasureCardStructOutput
	// 	let c21: TreasureCardStructOutput
	// 	let c22: TreasureCardStructOutput

	// 	let player_legion = Player.assassin
	// 	let	convertedCards

	// 	console.log("Staking dragon tail in: ", [0,1])
	// 	await tryStakeAndPrint(0, 1, "dragon tail", "nature");
	// 	c01 = await tTriad.getCardAtCell(0, 1)
	// 	expect(c01.tcard).to.equal("dragon tail")
	// 	expect(c01.player).to.equal(Player.nature) // nature: 0
	// 	convertedCards = await tTriad.getConvertedCards();
	// 	expect(convertedCards).to.equal(0);
	// 	console.log("convertedCards: ", convertedCards )
	// 	console.log("\n")


	// 	console.log("Staking honeycomb in: ", [0,0])
	// 	await tryStakeAndPrint(0, 0, "honeycomb", player_legion);
	// 	c01 = await tTriad.getCardAtCell(0, 1)
	// 	c00 = await tTriad.getCardAtCell(0, 0)
	// 	expect(c01.tcard).to.equal("dragon tail")
	// 	expect(c01.player).to.equal(player_legion)
	// 	expect(c00.tcard).to.equal("honeycomb")
	// 	expect(c00.player).to.equal(player_legion)
	// 	convertedCards = await tTriad.getConvertedCards();
	// 	expect(convertedCards).to.equal(1);
	// 	console.log("convertedCards: ", convertedCards )
	// 	console.log("\n")


	// 	console.log("Staking grin in: ", [1,0])
	// 	await tryStakeAndPrint(1, 0, "grin", Player.nature);
	// 	c00 = await tTriad.getCardAtCell(0, 0)
	// 	c10 = await tTriad.getCardAtCell(1, 0)
	// 	expect(c00.tcard).to.equal("honeycomb")
	// 	expect(c00.player).to.equal(player_legion)
	// 	expect(c10.tcard).to.equal("grin")
	// 	expect(c10.player).to.equal(Player.nature)
	// 	convertedCards = await tTriad.getConvertedCards();
	// 	expect(convertedCards).to.equal(1);
	// 	console.log("convertedCards: ", convertedCards )
	// 	console.log("\n")

	// 	console.log("Staking ox in: ", [1,2])
	// 	await tryStakeAndPrint(1, 2, "ox", player_legion);
	// 	console.log("Staking bottomless elixer in: ", [0,2])
	// 	await tryStakeAndPrint(0, 2, "bottomless elixer", "nature");
	// 	c01 = await tTriad.getCardAtCell(0, 1)
	// 	c02 = await tTriad.getCardAtCell(0, 2)
	// 	c12 = await tTriad.getCardAtCell(1, 2)
	// 	expect(c01.tcard).to.equal("dragon tail")
	// 	expect(c01.player).to.equal(Player.nature)
	// 	expect(c02.tcard).to.equal("bottomless elixer")
	// 	expect(c02.player).to.equal(Player.nature)
	// 	expect(c12.tcard).to.equal("ox")
	// 	expect(c12.player).to.equal(Player.nature)
	// 	convertedCards = await tTriad.getConvertedCards();
	// 	expect(convertedCards).to.equal(-1);
	// 	console.log("convertedCards: ", convertedCards )
	// 	console.log("\n")

	// 	console.log("Staking donkey in: ", [1,1])
	// 	await tryStakeAndPrint(1, 1, "donkey", player_legion);
	// 	c01 = await tTriad.getCardAtCell(0, 1)
	// 	c10 = await tTriad.getCardAtCell(1, 0)
	// 	c11 = await tTriad.getCardAtCell(1, 1)
	// 	c12 = await tTriad.getCardAtCell(1, 2)
	// 	expect(c01.tcard).to.equal("dragon tail")
	// 	expect(c01.player).to.equal(player_legion)
	// 	expect(c10.tcard).to.equal("grin")
	// 	expect(c10.player).to.equal(player_legion)
	// 	expect(c11.tcard).to.equal("donkey")
	// 	expect(c11.player).to.equal(player_legion)
	// 	expect(c12.tcard).to.equal("ox")
	// 	expect(c12.player).to.equal(player_legion)
	// 	convertedCards = await tTriad.getConvertedCards();
	// 	expect(convertedCards).to.equal(2);
	// 	console.log("convertedCards: ", convertedCards )
	// 	console.log("\n")

	// 	console.log("Staking small bird in: ", [2,2])
	// 	await tryStakeAndPrint(2, 2, "small bird", "nature");
	// 	c12 = await tTriad.getCardAtCell(1, 2)
	// 	c22 = await tTriad.getCardAtCell(2, 2)
	// 	expect(c12.tcard).to.equal("ox")
	// 	expect(c12.player).to.equal(Player.nature)
	// 	expect(c22.tcard).to.equal("small bird")
	// 	expect(c22.player).to.equal(Player.nature)
	// 	convertedCards = await tTriad.getConvertedCards();
	// 	expect(convertedCards).to.equal(1);
	// 	console.log("convertedCards: ", convertedCards )
	// 	console.log("\n")

	// 	console.log("Staking immovable stone in: ", [2,1])
	// 	await tryStakeAndPrint(2, 1, "immovable stone", player_legion);
	// 	c21 = await tTriad.getCardAtCell(2, 1)
	// 	c22 = await tTriad.getCardAtCell(2, 2)
	// 	expect(c21.tcard).to.equal("immovable stone")
	// 	expect(c21.player).to.equal(player_legion)
	// 	expect(c22.tcard).to.equal("small bird")
	// 	expect(c22.player).to.equal(player_legion)
	// 	convertedCards = await tTriad.getConvertedCards();
	// 	expect(convertedCards).to.equal(2);
	// 	console.log("convertedCards: ", convertedCards )
	// 	console.log("\n")


	// 	console.log("Staking red feather in: ", [2,0])
	// 	await tryStakeAndPrint(2, 0, "red feather", "nature");
	// 	c20 = await tTriad.getCardAtCell(2, 0)
	// 	c21 = await tTriad.getCardAtCell(2, 1)
	// 	expect(c20.tcard).to.equal("red feather")
	// 	expect(c20.player).to.equal(Player.nature)
	// 	expect(c21.tcard).to.equal("immovable stone")
	// 	expect(c21.player).to.equal(Player.nature)

	// 	convertedCards = await tTriad.getConvertedCards();
	// 	expect(convertedCards).to.equal(1);
	// 	console.log("convertedCards: ", convertedCards )
	// 	console.log("\n")
	// })


	// it("Shitty random samples 2 gridCells without replacement", async function () {

	// 	const decoder = new ethers.utils.AbiCoder();

	// 	// let arrOfIndicesTx2 = await sRandom.getRandomIndices();

	// 	// let receipt = await arrOfIndicesTx2.wait();
	// 	// let logs = receipt.events?.filter(x => x.event == "ArrayOfIndices") ?? []
	// 	// // console.log("logs: ", logs)
	// 	// let data = logs[0].data
	// 	// // console.log("data: ", data)

	// 	// let parsed = decoder.decode(
	// 	// 	['uint[]'],
	// 	// 	ethers.utils.hexDataSlice(data, 0)
	// 	// )
	// 	// console.log("parsed data: ", parsed)

	// 	let numDraws = 2;

	// 	let arrOfCellCoordsTx = await sRandom.sampleRandomGridCellCoords(numDraws);
	// 	let receipt2 = await arrOfCellCoordsTx.wait();
	// 	let logs2 = receipt2.events?.filter(x => x.event === "ArrayOfSampledCellCoords") ?? []
	// 	let parsed = decoder.decode(
	// 		['uint8[2][]'],
	// 		ethers.utils.hexDataSlice(logs2?.[0].data, 0)
	// 	)
	// 	console.log("parsed data: ", parsed)
	// 	expect(parsed[0].length).to.be.eq(numDraws)

	// })

})



function fmt(treasure: string, player: number) {
	let _t =  treasure.trim() != "" ? treasure : "------------------"
	let _player = player === 0
		? "Nature"
		: player !== 1
			? "Player"
			: undefined

	if (!_player) {
		return _t
	} else {
		return _t + " " + `(${_player})`
	}
}

const printGrid = async (tTriad: TreasureTriad) => {
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
		fmt(_c00.tcard, _c00.player),
		fmt(_c01.tcard, _c01.player),
		fmt(_c02.tcard, _c02.player)
	].join(",\t")
	const row1 = [
		fmt(_c10.tcard, _c10.player),
		fmt(_c11.tcard, _c11.player),
		fmt(_c12.tcard, _c12.player)
	].join(",\t")
	const row2 = [
		fmt(_c20.tcard, _c20.player),
		fmt(_c21.tcard, _c21.player),
		fmt(_c22.tcard, _c22.player)
	].join(",\t")
	console.log("[", row0, "]")
	console.log("[", row1, "]")
	console.log("[", row2, "]")
	console.log("\n")
}