/* Autogenerated file. Do not edit manually. */
/* tslint:disable */
/* eslint-disable */
import {
  BaseContract,
  BigNumber,
  BigNumberish,
  BytesLike,
  CallOverrides,
  ContractTransaction,
  Overrides,
  PopulatedTransaction,
  Signer,
  utils,
} from "ethers";
import { FunctionFragment, Result, EventFragment } from "@ethersproject/abi";
import { Listener, Provider } from "@ethersproject/providers";
import { TypedEventFilter, TypedEvent, TypedListener, OnEvent } from "./common";

export type CardStatsStruct = {
  n: BigNumberish;
  e: BigNumberish;
  s: BigNumberish;
  w: BigNumberish;
  card_affinity: BigNumberish;
  tokenId: BigNumberish;
  card_name: string;
};

export type CardStatsStructOutput = [
  BigNumber,
  BigNumber,
  BigNumber,
  BigNumber,
  number,
  BigNumber,
  string
] & {
  n: BigNumber;
  e: BigNumber;
  s: BigNumber;
  w: BigNumber;
  card_affinity: number;
  tokenId: BigNumber;
  card_name: string;
};

export interface TreasureTriadCardStatsInterface extends utils.Interface {
  contractName: "TreasureTriadCardStats";
  functions: {
    "addCard(string,uint256,uint256,uint256,uint256,uint8,uint256)": FunctionFragment;
    "getAffinities()": FunctionFragment;
    "getBaseCardStatsByName(string)": FunctionFragment;
    "getBaseCardStatsByTokenId(uint256)": FunctionFragment;
    "getCardNames()": FunctionFragment;
    "getCardTokenIds()": FunctionFragment;
    "getLegionAffinities(uint8)": FunctionFragment;
    "removeCard(string)": FunctionFragment;
    "setLegionAffinities(uint8,uint8[])": FunctionFragment;
  };

  encodeFunctionData(
    functionFragment: "addCard",
    values: [
      string,
      BigNumberish,
      BigNumberish,
      BigNumberish,
      BigNumberish,
      BigNumberish,
      BigNumberish
    ]
  ): string;
  encodeFunctionData(
    functionFragment: "getAffinities",
    values?: undefined
  ): string;
  encodeFunctionData(
    functionFragment: "getBaseCardStatsByName",
    values: [string]
  ): string;
  encodeFunctionData(
    functionFragment: "getBaseCardStatsByTokenId",
    values: [BigNumberish]
  ): string;
  encodeFunctionData(
    functionFragment: "getCardNames",
    values?: undefined
  ): string;
  encodeFunctionData(
    functionFragment: "getCardTokenIds",
    values?: undefined
  ): string;
  encodeFunctionData(
    functionFragment: "getLegionAffinities",
    values: [BigNumberish]
  ): string;
  encodeFunctionData(functionFragment: "removeCard", values: [string]): string;
  encodeFunctionData(
    functionFragment: "setLegionAffinities",
    values: [BigNumberish, BigNumberish[]]
  ): string;

  decodeFunctionResult(functionFragment: "addCard", data: BytesLike): Result;
  decodeFunctionResult(
    functionFragment: "getAffinities",
    data: BytesLike
  ): Result;
  decodeFunctionResult(
    functionFragment: "getBaseCardStatsByName",
    data: BytesLike
  ): Result;
  decodeFunctionResult(
    functionFragment: "getBaseCardStatsByTokenId",
    data: BytesLike
  ): Result;
  decodeFunctionResult(
    functionFragment: "getCardNames",
    data: BytesLike
  ): Result;
  decodeFunctionResult(
    functionFragment: "getCardTokenIds",
    data: BytesLike
  ): Result;
  decodeFunctionResult(
    functionFragment: "getLegionAffinities",
    data: BytesLike
  ): Result;
  decodeFunctionResult(functionFragment: "removeCard", data: BytesLike): Result;
  decodeFunctionResult(
    functionFragment: "setLegionAffinities",
    data: BytesLike
  ): Result;

  events: {
    "AddedNewCard(tuple)": EventFragment;
    "SetLegionAffinity(uint8,uint8[])": EventFragment;
  };

  getEvent(nameOrSignatureOrTopic: "AddedNewCard"): EventFragment;
  getEvent(nameOrSignatureOrTopic: "SetLegionAffinity"): EventFragment;
}

export type AddedNewCardEvent = TypedEvent<
  [CardStatsStructOutput],
  { arg0: CardStatsStructOutput }
>;

export type AddedNewCardEventFilter = TypedEventFilter<AddedNewCardEvent>;

export type SetLegionAffinityEvent = TypedEvent<
  [number, number[]],
  { arg0: number; arg1: number[] }
>;

export type SetLegionAffinityEventFilter =
  TypedEventFilter<SetLegionAffinityEvent>;

export interface TreasureTriadCardStats extends BaseContract {
  contractName: "TreasureTriadCardStats";
  connect(signerOrProvider: Signer | Provider | string): this;
  attach(addressOrName: string): this;
  deployed(): Promise<this>;

  interface: TreasureTriadCardStatsInterface;

  queryFilter<TEvent extends TypedEvent>(
    event: TypedEventFilter<TEvent>,
    fromBlockOrBlockhash?: string | number | undefined,
    toBlock?: string | number | undefined
  ): Promise<Array<TEvent>>;

  listeners<TEvent extends TypedEvent>(
    eventFilter?: TypedEventFilter<TEvent>
  ): Array<TypedListener<TEvent>>;
  listeners(eventName?: string): Array<Listener>;
  removeAllListeners<TEvent extends TypedEvent>(
    eventFilter: TypedEventFilter<TEvent>
  ): this;
  removeAllListeners(eventName?: string): this;
  off: OnEvent<this>;
  on: OnEvent<this>;
  once: OnEvent<this>;
  removeListener: OnEvent<this>;

  functions: {
    addCard(
      _name: string,
      _n: BigNumberish,
      _e: BigNumberish,
      _s: BigNumberish,
      _w: BigNumberish,
      _aff: BigNumberish,
      _tokenId: BigNumberish,
      overrides?: Overrides & { from?: string | Promise<string> }
    ): Promise<ContractTransaction>;

    getAffinities(overrides?: CallOverrides): Promise<[number[]]>;

    getBaseCardStatsByName(
      _card_name: string,
      overrides?: CallOverrides
    ): Promise<[CardStatsStructOutput]>;

    getBaseCardStatsByTokenId(
      _tokenId: BigNumberish,
      overrides?: CallOverrides
    ): Promise<[CardStatsStructOutput]>;

    getCardNames(overrides?: CallOverrides): Promise<[string[]]>;

    getCardTokenIds(overrides?: CallOverrides): Promise<[BigNumber[]]>;

    getLegionAffinities(
      _legion_class: BigNumberish,
      overrides?: CallOverrides
    ): Promise<[number[]]>;

    removeCard(
      _name: string,
      overrides?: Overrides & { from?: string | Promise<string> }
    ): Promise<ContractTransaction>;

    setLegionAffinities(
      _legion_class: BigNumberish,
      _affinities: BigNumberish[],
      overrides?: Overrides & { from?: string | Promise<string> }
    ): Promise<ContractTransaction>;
  };

  addCard(
    _name: string,
    _n: BigNumberish,
    _e: BigNumberish,
    _s: BigNumberish,
    _w: BigNumberish,
    _aff: BigNumberish,
    _tokenId: BigNumberish,
    overrides?: Overrides & { from?: string | Promise<string> }
  ): Promise<ContractTransaction>;

  getAffinities(overrides?: CallOverrides): Promise<number[]>;

  getBaseCardStatsByName(
    _card_name: string,
    overrides?: CallOverrides
  ): Promise<CardStatsStructOutput>;

  getBaseCardStatsByTokenId(
    _tokenId: BigNumberish,
    overrides?: CallOverrides
  ): Promise<CardStatsStructOutput>;

  getCardNames(overrides?: CallOverrides): Promise<string[]>;

  getCardTokenIds(overrides?: CallOverrides): Promise<BigNumber[]>;

  getLegionAffinities(
    _legion_class: BigNumberish,
    overrides?: CallOverrides
  ): Promise<number[]>;

  removeCard(
    _name: string,
    overrides?: Overrides & { from?: string | Promise<string> }
  ): Promise<ContractTransaction>;

  setLegionAffinities(
    _legion_class: BigNumberish,
    _affinities: BigNumberish[],
    overrides?: Overrides & { from?: string | Promise<string> }
  ): Promise<ContractTransaction>;

  callStatic: {
    addCard(
      _name: string,
      _n: BigNumberish,
      _e: BigNumberish,
      _s: BigNumberish,
      _w: BigNumberish,
      _aff: BigNumberish,
      _tokenId: BigNumberish,
      overrides?: CallOverrides
    ): Promise<CardStatsStructOutput>;

    getAffinities(overrides?: CallOverrides): Promise<number[]>;

    getBaseCardStatsByName(
      _card_name: string,
      overrides?: CallOverrides
    ): Promise<CardStatsStructOutput>;

    getBaseCardStatsByTokenId(
      _tokenId: BigNumberish,
      overrides?: CallOverrides
    ): Promise<CardStatsStructOutput>;

    getCardNames(overrides?: CallOverrides): Promise<string[]>;

    getCardTokenIds(overrides?: CallOverrides): Promise<BigNumber[]>;

    getLegionAffinities(
      _legion_class: BigNumberish,
      overrides?: CallOverrides
    ): Promise<number[]>;

    removeCard(_name: string, overrides?: CallOverrides): Promise<void>;

    setLegionAffinities(
      _legion_class: BigNumberish,
      _affinities: BigNumberish[],
      overrides?: CallOverrides
    ): Promise<void>;
  };

  filters: {
    "AddedNewCard(tuple)"(arg0?: null): AddedNewCardEventFilter;
    AddedNewCard(arg0?: null): AddedNewCardEventFilter;

    "SetLegionAffinity(uint8,uint8[])"(
      arg0?: null,
      arg1?: null
    ): SetLegionAffinityEventFilter;
    SetLegionAffinity(arg0?: null, arg1?: null): SetLegionAffinityEventFilter;
  };

  estimateGas: {
    addCard(
      _name: string,
      _n: BigNumberish,
      _e: BigNumberish,
      _s: BigNumberish,
      _w: BigNumberish,
      _aff: BigNumberish,
      _tokenId: BigNumberish,
      overrides?: Overrides & { from?: string | Promise<string> }
    ): Promise<BigNumber>;

    getAffinities(overrides?: CallOverrides): Promise<BigNumber>;

    getBaseCardStatsByName(
      _card_name: string,
      overrides?: CallOverrides
    ): Promise<BigNumber>;

    getBaseCardStatsByTokenId(
      _tokenId: BigNumberish,
      overrides?: CallOverrides
    ): Promise<BigNumber>;

    getCardNames(overrides?: CallOverrides): Promise<BigNumber>;

    getCardTokenIds(overrides?: CallOverrides): Promise<BigNumber>;

    getLegionAffinities(
      _legion_class: BigNumberish,
      overrides?: CallOverrides
    ): Promise<BigNumber>;

    removeCard(
      _name: string,
      overrides?: Overrides & { from?: string | Promise<string> }
    ): Promise<BigNumber>;

    setLegionAffinities(
      _legion_class: BigNumberish,
      _affinities: BigNumberish[],
      overrides?: Overrides & { from?: string | Promise<string> }
    ): Promise<BigNumber>;
  };

  populateTransaction: {
    addCard(
      _name: string,
      _n: BigNumberish,
      _e: BigNumberish,
      _s: BigNumberish,
      _w: BigNumberish,
      _aff: BigNumberish,
      _tokenId: BigNumberish,
      overrides?: Overrides & { from?: string | Promise<string> }
    ): Promise<PopulatedTransaction>;

    getAffinities(overrides?: CallOverrides): Promise<PopulatedTransaction>;

    getBaseCardStatsByName(
      _card_name: string,
      overrides?: CallOverrides
    ): Promise<PopulatedTransaction>;

    getBaseCardStatsByTokenId(
      _tokenId: BigNumberish,
      overrides?: CallOverrides
    ): Promise<PopulatedTransaction>;

    getCardNames(overrides?: CallOverrides): Promise<PopulatedTransaction>;

    getCardTokenIds(overrides?: CallOverrides): Promise<PopulatedTransaction>;

    getLegionAffinities(
      _legion_class: BigNumberish,
      overrides?: CallOverrides
    ): Promise<PopulatedTransaction>;

    removeCard(
      _name: string,
      overrides?: Overrides & { from?: string | Promise<string> }
    ): Promise<PopulatedTransaction>;

    setLegionAffinities(
      _legion_class: BigNumberish,
      _affinities: BigNumberish[],
      overrides?: Overrides & { from?: string | Promise<string> }
    ): Promise<PopulatedTransaction>;
  };
}