# VLSI Design Task 1 - Project Report

**Student:** Vishnu Vamsi  
**Program:** Industry-Oriented Internship Program on VLSI Design and Semiconductor Engineering  
**Project:** Digital Arithmetic Logic Circuit Library Using Verilog HDL  
**Repository:** https://github.com/vishnuvamsi396-gif/VLSI-Design-Task-1

The generated PDF snapshot is `docs/task1_project_report.pdf`. Rebuild it with `python3 scripts/build_report_pdf.py` after updating this editable report and adding the remaining evidence.

## 1. Objective

Build a small reusable combinational RTL library and practice the Task 1 workflow: digital logic design, Verilog coding, self-checking testbench development, simulation, waveform inspection, and version-controlled documentation.

## 2. Designs

The RTL folder contains AND, OR, XOR, NOT, NAND, NOR, and XNOR gates; 2:1 and 4:1 multiplexers; half and full adders; a four-stage 4-bit ripple-carry adder; an unsigned parameterized adder; and a 4-bit mini-project unit selecting AND, OR, XOR, or addition.

For the assignment's ASIC/FPGA comparison activity, the notes compare reconfigurability, up-front cost, typical applications, and design-cycle trade-offs. Gate symbols are drawn in `docs/diagrams/basic_logic_gates.svg`; the mini-project RTL and simulation workflows are described in `docs/diagrams/`.

## 3. Verification plan

The testbenches exhaustively cover all 2-input gate combinations, the mux select/data cases, all half/full-adder inputs, all 512 input combinations of the 4-bit ripple adder, 1,024 deterministic 8-bit parameterized-adder cases, and every mini-project operation across all 4-bit operand pairs. Testbenches include assertions and generate VCD traces when run with Icarus Verilog.

## 4. Simulation results

The included suite was run in WSL using `bash scripts/run_all.sh`. All six testbenches compiled and passed their self-checks: gate combinations, mux selections, half/full-adder combinations, all 512 4-bit ripple-adder cases, 1,024 deterministic 8-bit parameterized-adder cases, and 1,024 operation/operand cases for the mini-project. Per-test simulator output is saved in `simulation/results/`, and VCD traces are in `simulation/vcd/`. The run date was 2026-11-01. GTKWave visual inspection remains pending.

## 5. Waveform observations

The mini-project waveform was inspected in GTKWave over 964-968 ns. With `a=F` and `b=1`, the operation select steps through AND (`00`), OR (`01`), XOR (`10`), and addition (`11`). During addition, the observed result is `0` and `carry_out` is `1`, as expected for 4-bit unsigned overflow. Its genuine screenshot is `waveforms/arithmetic_logic_library.png`. Additional genuine captures from earlier runs cover AND, OR, XOR, half adder, full adder, and 2:1 mux in the same folder.

## 6. Environment and Linux practice

**Pending local verification.** Record actual Ubuntu/WSL version and `iverilog -V`, `vvp -V`, `gtkwave --version`, and `git --version` output in `linux_report/command_practice.md`.

## 7. Conclusion

This source repository is organized for the required Task 1 deliverables. Completion of simulation, waveform review, local environment evidence, and final PDF export remains dependent on running the project in the student's development environment.