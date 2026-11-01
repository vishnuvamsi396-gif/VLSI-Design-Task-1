# VLSI Design Task 1

Starter submission for Sumerix Global's VLSI Design and Semiconductor Engineering Task 1. The project collects synthesizable Verilog modules, self-checking testbenches, a reproducible Icarus Verilog script, design notes, and submission evidence slots.

## Project status

RTL and testbench sources are prepared. The included suite has been run in WSL with Icarus Verilog; all six testbenches passed and produced logs and VCD files. The mini-project waveform was inspected in GTKWave and its screenshot is included; the student's environment setup report and any additional waveform views remain pending.

## Contents

- `rtl/` - gates, multiplexers, adders, and the mini-project circuit library
- `testbench/` - self-checking testbenches for every module family
- `scripts/run_all.sh` - compile and run all testbenches with Icarus Verilog
- `docs/` - assignment checklist, design notes, diagrams, and report source
- `simulation/` - location for genuine simulator logs and VCD files
- `waveforms/` - location for genuine GTKWave screenshots
- `linux_report/` - command practice report template
- `progress_log/` - dated work log template

## Requirements

- Ubuntu Linux or WSL
- Icarus Verilog (`iverilog` and `vvp`)
- GTKWave for visual waveform inspection
- Git

Check the tools with `iverilog -V`, `vvp -V`, `gtkwave --version`, and `git --version`.

## Run simulations

From the repository root in Ubuntu/WSL:

```bash
chmod +x scripts/run_all.sh
./scripts/run_all.sh
```

The script writes build files and logs under `simulation/build/`, VCD files under `simulation/vcd/`, and per-test logs under `simulation/results/`. The included results are the actual output of a successful run. A non-zero exit status indicates a compile or self-check failure.

Open a generated waveform, for example:

```bash
gtkwave simulation/vcd/tb_arithmetic_logic_library.vcd
```

The verified mini-project screenshot is `waveforms/arithmetic_logic_library.png`. Add any additional testbench screenshots to `waveforms/`; do not label an expected-output table as a simulation result.

## Assignment checklist

See [`docs/requirements_checklist.md`](docs/requirements_checklist.md). The generated report PDF is `docs/task1_project_report.pdf`; its reproducible source is `scripts/build_report_pdf.py`. Update the report with the pending GTKWave screenshots and personal environment evidence, then regenerate the PDF before final submission.

## Mini-project

The mini-project is the **Digital Arithmetic Logic Circuit Library Using Verilog HDL**. `rtl/arithmetic_logic_library.v` provides a reusable 4-bit combinational unit with AND, OR, XOR, and addition operations. Primitive gate, mux, half-adder, full-adder, ripple-carry-adder, and parameterized-adder modules are also included for independent study and verification.