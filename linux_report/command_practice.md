# Linux command practice report

## Environment

- Distribution and version: Ubuntu 26.04.1 LTS (release 26.04, codename resolute)
- Environment: Ubuntu terminal at `~/VLSI-Design-Task-1`
- Icarus Verilog version: 12.0 (stable)
- VVP version: 12.0 (stable)
- GTKWave version: 3.3.126
- Git version: 2.53.0

These version checks were run by the student on 2026-11-01. `lsb_release -a` printed `No LSB modules are available.` followed by the Ubuntu release information; the release information was still reported correctly.

## Commands actually checked

| Command | Observed result | Date |
|---|---|---|
| `lsb_release -a` | Ubuntu 26.04.1 LTS, release 26.04, codename resolute | 2026-11-01 |
| `iverilog -V` | Icarus Verilog 12.0 (stable) | 2026-11-01 |
| `vvp -V` | Icarus Verilog runtime 12.0 (stable) | 2026-11-01 |
| `gtkwave --version` | GTKWave Analyzer v3.3.126 | 2026-11-01 |
| `git --version` | git version 2.53.0 | 2026-11-01 |

## Commands practiced

Run and record the actual result/date for each command. The examples below are a plan, not evidence that they have been run.

| Command | Example purpose | Actual result/date |
|---|---|---|
| `ls -la` | Listed the project root, including hidden `.git` and `.gitignore` entries and project folders | 2026-11-01 |
| `ls -lh waveforms/` | Confirmed the README and seven PNG waveform screenshots were present | 2026-11-01 |
| `pwd` | Printed `/home/vishn/VLSI-Design-Task-1` | 2026-11-01 |
| `cd ..` | Changed from the project folder to its parent; `pwd` showed `/home/vishn` | 2026-11-01 |
| `mkdir -p ~/vlsi-task1-practice` | Created `/home/vishn/vlsi-task1-practice`; a later listing typo used `vlsi-task1-practic` and returned “No such file or directory” | 2026-11-01 |
| `cp README.md ~/vlsi-task1-practice/README-copy.md` | Copied the repository README to the scratch folder; `ls -l` showed `README-copy.md` (3,090 bytes) | 2026-11-01 |
| `mv ~/vlsi-task1-practice/README-copy.md ~/vlsi-task1-practice/README-renamed.md` | Renamed the scratch copy; `ls -l` showed `README-renamed.md` (3,090 bytes) | 2026-11-01 |
| `rm` | Remove a disposable file | Pending |
| `cat linux_report/command_practice.md` | Displayed the Linux command practice report in the terminal | 2026-11-01 |
| `nano` | Edit a text file | Pending |
| `chmod` | Set script execute permission | Pending |

## Git commands practiced

| Command | Observed result | Date |
|---|---|---|
| `git remote -v` | `origin` fetch and push URLs point to this public GitHub repository | 2026-11-01 |
| `git status` | Confirmed `main` tracked `origin/main`; after restoring timestamp-only VCD date changes, the working tree was clean | 2026-11-01 |
| `git diff --stat` and `git diff -- simulation/vcd/tb_basic_gates.vcd` | Found the six VCD changes were generated-date-only | 2026-11-01 |
| `git restore simulation/vcd/` | Restored only generated VCD files; subsequent status was clean | 2026-11-01 |
| `git pull origin main` | Fast-forwarded local `main` and downloaded the seven waveform screenshots and report updates | 2026-11-01 |

## VLSI environment setup

Record installation/configuration steps actually completed and attach terminal evidence if required by the instructor. Never include credentials or personal tokens in this report.

