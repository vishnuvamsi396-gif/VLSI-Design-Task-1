# VLSI Design Task 1

Organized project submission for Sumerix Global's VLSI Design and Semiconductor Engineering Task 1. The repository collects synthesizable Verilog modules, self-checking testbenches, a reproducible Icarus Verilog script, design notes, simulation evidence, and project reports.

## Project status

RTL and testbench sources are prepared. The included suite was run in WSL with Icarus Verilog; all six testbenches passed and produced logs and VCD files. Seven genuine GTKWave screenshots are included for the mini-project, AND/OR/XOR gates, half/full adders, and 2:1 mux. Ubuntu and tool versions, including VS Code 1.138.0 and the verified Verilog extension, plus observed Linux/Git command practice, are recorded in the reports.

## Contents

- `rtl/` - gates, multiplexers, adders, and the mini-project circuit library
- `testbench/` - self-checking testbenches for every module family
- `scripts/run_all.sh` - compile and run all testbenches with Icarus Verilog
- `docs/` - assignment checklist, design notes, diagrams, and report source
- [Diagrams gallery](docs/diagrams/README.md) - GitHub-previewable RTL, ripple-carry adder, logic-gate, and simulation workflow drawings
- `simulation/` - location for genuine simulator logs and VCD files
- `waveforms/` - location for genuine GTKWave screenshots
- `linux_report/` - environment and command practice evidence
- `progress_log/` - dated work log

## Requirements

- Ubuntu Linux or WSL
- Icarus Verilog (`iverilog` and `vvp`)
- GTKWave for visual waveform inspection
- Visual Studio Code with a Verilog HDL extension
- Git

This workspace recommends the Verilog HDL/SystemVerilog extension from the VS Code Marketplace in [`.vscode/extensions.json`](.vscode/extensions.json). The student confirmed `mshr-h.veriloghdl` installed in the WSL VS Code extension host. When opening the repository in another VS Code environment, accept the workspace extension recommendation and verify the installation there.

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

GTKWave screenshots are in `waveforms/`. The project includes the mini-project overflow case plus screenshots for the AND/OR/XOR gates, half/full adders, and 2:1 mux. Add other testbench screenshots if you inspect those waveforms; do not label an expected-output table as a simulation result.

## Assignment checklist

See [`docs/requirements_checklist.md`](docs/requirements_checklist.md). The generated report PDF is `docs/task1_project_report.pdf`; its reproducible source is `scripts/build_report_pdf.py`. The PDF includes the seven GTKWave screenshots and the reported Ubuntu/tool versions. The Linux practice report marks commands complete only when their terminal results were observed.

## Mini-project

The mini-project is the **Digital Arithmetic Logic Circuit Library Using Verilog HDL**. `rtl/arithmetic_logic_library.v` provides a reusable 4-bit combinational unit with AND, OR, XOR, and addition operations. Primitive gate, mux, half-adder, full-adder, ripple-carry-adder, and parameterized-adder modules are also included for independent study and verification.
