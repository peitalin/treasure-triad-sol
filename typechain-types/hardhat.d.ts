/* Autogenerated file. Do not edit manually. */
/* tslint:disable */
/* eslint-disable */

import { ethers } from "ethers";
import {
  FactoryOptions,
  HardhatEthersHelpers as HardhatEthersHelpersBase,
} from "@nomiclabs/hardhat-ethers/types";

import * as Contracts from ".";

declare module "hardhat/types/runtime" {
  interface HardhatEthersHelpers extends HardhatEthersHelpersBase {
    getContractFactory(
      name: "Ownable",
      signerOrOptions?: ethers.Signer | FactoryOptions
    ): Promise<Contracts.Ownable__factory>;
    getContractFactory(
      name: "IERC20",
      signerOrOptions?: ethers.Signer | FactoryOptions
    ): Promise<Contracts.IERC20__factory>;
    getContractFactory(
      name: "LegionDecks",
      signerOrOptions?: ethers.Signer | FactoryOptions
    ): Promise<Contracts.LegionDecks__factory>;
    getContractFactory(
      name: "ShittyRandom",
      signerOrOptions?: ethers.Signer | FactoryOptions
    ): Promise<Contracts.ShittyRandom__factory>;
    getContractFactory(
      name: "TreasureTriad",
      signerOrOptions?: ethers.Signer | FactoryOptions
    ): Promise<Contracts.TreasureTriad__factory>;
    getContractFactory(
      name: "TreasureTriadCardStats",
      signerOrOptions?: ethers.Signer | FactoryOptions
    ): Promise<Contracts.TreasureTriadCardStats__factory>;
    getContractFactory(
      name: "WorldBoss2",
      signerOrOptions?: ethers.Signer | FactoryOptions
    ): Promise<Contracts.WorldBoss2__factory>;

    getContractAt(
      name: "Ownable",
      address: string,
      signer?: ethers.Signer
    ): Promise<Contracts.Ownable>;
    getContractAt(
      name: "IERC20",
      address: string,
      signer?: ethers.Signer
    ): Promise<Contracts.IERC20>;
    getContractAt(
      name: "LegionDecks",
      address: string,
      signer?: ethers.Signer
    ): Promise<Contracts.LegionDecks>;
    getContractAt(
      name: "ShittyRandom",
      address: string,
      signer?: ethers.Signer
    ): Promise<Contracts.ShittyRandom>;
    getContractAt(
      name: "TreasureTriad",
      address: string,
      signer?: ethers.Signer
    ): Promise<Contracts.TreasureTriad>;
    getContractAt(
      name: "TreasureTriadCardStats",
      address: string,
      signer?: ethers.Signer
    ): Promise<Contracts.TreasureTriadCardStats>;
    getContractAt(
      name: "WorldBoss2",
      address: string,
      signer?: ethers.Signer
    ): Promise<Contracts.WorldBoss2>;

    // default types
    getContractFactory(
      name: string,
      signerOrOptions?: ethers.Signer | FactoryOptions
    ): Promise<ethers.ContractFactory>;
    getContractFactory(
      abi: any[],
      bytecode: ethers.utils.BytesLike,
      signer?: ethers.Signer
    ): Promise<ethers.ContractFactory>;
    getContractAt(
      nameOrAbi: string | any[],
      address: string,
      signer?: ethers.Signer
    ): Promise<ethers.Contract>;
  }
}
