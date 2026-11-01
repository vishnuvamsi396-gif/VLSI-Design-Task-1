# Task 1 submission checklist

Source: *Industry-Oriented Internship Program on VLSI Design and Semiconductor Engineering, Project Task-1*, 22-page assignment PDF.

| Assignment requirement | Repository location | Status |
|---|---|---|
| Verilog source files: logic gates, 2:1 and 4:1 muxes, half adder, full adder | `rtl/` | Prepared |
| 4-bit ripple carry adder built from full adders | `rtl/adders.v` | Prepared |
| Parameterized N-bit adder exercise | `rtl/adders.v` | Prepared |
| Mini-project: Digital Arithmetic Logic Circuit Library | `rtl/arithmetic_logic_library.v` | Prepared |
| Testbench for every module family | `testbench/` | Prepared; all passed in WSL |
| Simulation outputs | `simulation/results/` | Included: six successful run logs |
| GTKWave screenshots | `waveforms/*.png` | Seven genuine captures included: mini-project, AND/OR/XOR, half/full adders, and 2:1 mux |
| Logic gate diagrams | `docs/diagrams/basic_logic_gates.svg` | Included; previewed in the [diagrams gallery](diagrams/README.md) |
| Truth tables | `docs/design_notes.md` | Included for basic gates and NOT |
| Karnaugh-map solutions | `docs/design_notes.md` | Included for AND, OR, and XOR |
| RTL block diagram | `docs/diagrams/rtl_block_diagram.md`, `docs/diagrams/rtl_block_diagram.svg` | SVG embedded in Markdown and gallery for GitHub preview |
| Simulation workflow diagram | `docs/diagrams/simulation_workflow.md`, `docs/diagrams/simulation_workflow.svg` | SVG embedded in Markdown and gallery for GitHub preview |
| Project folder structure and README | `README.md` | Prepared; links to the diagrams gallery |
| GitHub repository | `https://github.com/vishnuvamsi396-gif/VLSI-Design-Task-1` | Public repository; listed project deliverables are organized on `main` |
| Project documentation PDF | `docs/task1_project_report.pdf`; editable source in `docs/report.md` | Included with waveform and reported environment evidence |
| Linux command practice report | `linux_report/command_practice.md` | Ubuntu/tool versions and observed command exercises recorded |
| Daily progress log | `progress_log/progress.md` | Actual dated project and student terminal-work entries recorded; add future work as completed |
| Ubuntu/WSL, Icarus, GTKWave, Git, and VS Code environment | `linux_report/command_practice.md` | Verified from student-reported terminal output; VS Code 1.138.0 (x64) |
| LinkedIn post link | Submitted separately in the internship form | Separate required form field; publish the post and enter its URL there |

## Expected outcomes and repository evidence

| Expected outcome | Supporting evidence |
|---|---|
| Fully configured VLSI development environment | Ubuntu/WSL and Icarus Verilog, VVP, GTKWave, Git, and VS Code versions recorded in `linux_report/command_practice.md`; successful simulations are recorded under `simulation/results/`. |
| Practical understanding of digital electronics and Boolean logic | Design notes include truth tables and Karnaugh-map simplifications; gate, adder, mux, and arithmetic/logic RTL implementations are in `rtl/`. The student should be ready to explain these designs during review. |
| Working Verilog modules for basic combinational circuits | Synthesizable modules are organized in `rtl/`. |
| Functional testbenches and verified simulation results | Self-checking testbenches are in `testbench/`; the six successful run logs are in `simulation/results/`, with VCDs in `simulation/vcd/`. |
| Organized project documentation and version-controlled source code | This public GitHub repository contains the README, checklist, project report PDF, design notes, diagrams, Linux report, progress log, RTL, testbenches, and simulation evidence. |
| Reusable RTL components for future processor and controller designs | The gate, mux, adder, and arithmetic/logic modules are reusable combinational building blocks in `rtl/`; no processor or controller is claimed as part of this task. |

## Evaluation areas (100 marks)

| Area | Marks |
|---|---:|
| Linux environment setup | 10 |
| Digital logic design | 20 |
| Verilog HDL coding | 25 |
| Testbench development | 15 |
| Simulation and waveform verification | 15 |
| Mini-project implementation | 10 |
| Documentation and GitHub | 5 |
| **Total** | **100** |

Only mark command exercises complete when their actual output is recorded. Publish the LinkedIn post and provide its URL in the separate internship form field; the GitHub repository link does not replace it.
