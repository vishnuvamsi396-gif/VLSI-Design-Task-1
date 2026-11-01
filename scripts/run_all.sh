#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD="$ROOT/simulation/build"
VCD="$ROOT/simulation/vcd"
RESULTS="$ROOT/simulation/results"
mkdir -p "$BUILD" "$VCD" "$RESULTS"
cd "$ROOT"

if ! command -v iverilog >/dev/null || ! command -v vvp >/dev/null; then
    echo "ERROR: install Icarus Verilog (iverilog and vvp) first." >&2
    exit 127
fi

run_tb() {
    local name="$1"; shift
    echo "== $name =="
    iverilog -g2012 -Wall -s "$name" -o "$BUILD/$name.out" "$@"
    vvp "$BUILD/$name.out" | tee "$RESULTS/$name.log"
}

run_tb tb_basic_gates rtl/basic_gates.v testbench/tb_basic_gates.v
run_tb tb_muxes rtl/muxes.v testbench/tb_muxes.v
run_tb tb_adders rtl/adders.v testbench/tb_adders.v
run_tb tb_ripple_carry_adder_4bit rtl/adders.v testbench/tb_ripple_carry_adder_4bit.v
run_tb tb_parameterized_adder rtl/adders.v testbench/tb_parameterized_adder.v
run_tb tb_arithmetic_logic_library rtl/arithmetic_logic_library.v testbench/tb_arithmetic_logic_library.v

echo "All testbenches passed. See simulation/results/ for logs and simulation/vcd/ for waveforms."
