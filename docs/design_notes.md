# Design notes

## Semiconductor and VLSI fundamentals

An ASIC is a custom integrated circuit designed for a specific product or workload. It can offer strong performance, power, and area after fabrication, but carries non-recurring design and manufacturing cost and cannot be reconfigured after fabrication. An FPGA is a reconfigurable device made from programmable logic, routing, and I/O resources. It is useful for prototyping and lower-volume products, with faster iteration and lower up-front cost, usually at a higher per-unit area or power than a comparable ASIC. Examples include ASIC SoCs in phones and custom accelerators; FPGA boards in prototyping, instrumentation, and adaptable networking equipment.

Typical digital IC flow: specification -> architecture -> RTL -> functional verification -> synthesis -> implementation (floorplan, placement, clock-tree synthesis, routing) -> signoff -> fabrication. This repository covers introductory RTL and simulation, not physical design or signoff.

## Boolean functions and truth tables

| A | B | AND | OR | XOR | NAND | NOR | XNOR |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |

| A | NOT A |
|---:|---:|
| 0 | 1 |
| 1 | 0 |

## Multiplexers

For a 2:1 mux, `Y = (~S & D0) | (S & D1)`. For a 4:1 mux, `S1S0=00,01,10,11` selects `D0,D1,D2,D3` respectively.

## Adders

- Half adder: `SUM = A XOR B`; `CARRY = A AND B`.
- Full adder: `SUM = A XOR B XOR Cin`; `Cout = AB + ACin + BCin`.
- Four-bit ripple adder: four full-adder stages; each carry feeds the next higher bit.
- Parameterized adder: unsigned `WIDTH`-bit addition with an explicit carry-out.

## Karnaugh-map examples (SOP)

For two variables with Gray-code columns `B=0,1` and rows `A=0,1`:

**AND** has minterm `m3` only, so `F=A.B`.

| A \\ B | 0 | 1 |
|---|---:|---:|
| 0 | 0 | 0 |
| 1 | 0 | 1 |

**OR** has minterms `m1,m2,m3`; grouping the bottom row gives `A`, and grouping the right column gives `B`, so `F=A+B`.

| A \\ B | 0 | 1 |
|---|---:|---:|
| 0 | 0 | 1 |
| 1 | 1 | 1 |

**XOR** has minterms `m1,m2`; they are not adjacent as a pair without including a zero, so the minimal SOP is `F=(~A.B)+(A.~B)`.

| A \\ B | 0 | 1 |
|---|---:|---:|
| 0 | 0 | 1 |
| 1 | 1 | 0 |

## Mini-project operation map

| `operation` | Function | `carry_out` |
|---|---|---|
| `00` | `a AND b` | 0 |
| `01` | `a OR b` | 0 |
| `10` | `a XOR b` | 0 |
| `11` | unsigned `a + b` | addition carry |
