#!/usr/bin/env python3
"""Build the editable-source companion PDF for the Task 1 project report."""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "task1_project_report.pdf"
NAVY = colors.HexColor("#17365D")
BLUE = colors.HexColor("#2F75B5")
PALE = colors.HexColor("#EAF2F8")
GRAY = colors.HexColor("#5B6573")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=23, leading=28, textColor=NAVY, alignment=TA_CENTER, spaceAfter=8))
styles.add(ParagraphStyle(name="CoverSub", parent=styles["Normal"], fontSize=12, leading=17, textColor=GRAY, alignment=TA_CENTER, spaceAfter=6))
styles.add(ParagraphStyle(name="Section", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=NAVY, spaceBefore=7, spaceAfter=8))
styles.add(ParagraphStyle(name="SubSection", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=BLUE, spaceBefore=6, spaceAfter=5))
styles.add(ParagraphStyle(name="BodySmall", parent=styles["BodyText"], fontSize=9, leading=13, spaceAfter=5))
styles.add(ParagraphStyle(name="Cell", parent=styles["BodyText"], fontSize=8, leading=10))
styles.add(ParagraphStyle(name="CellHead", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=8, leading=10, textColor=colors.white))
styles.add(ParagraphStyle(name="Callout", parent=styles["BodyText"], fontSize=9, leading=13, textColor=NAVY, backColor=PALE, borderColor=BLUE, borderWidth=0.7, borderPadding=8, spaceBefore=5, spaceAfter=9))


def P(text, style="BodySmall"):
    return Paragraph(text, styles[style])


def table(rows, widths, header=True):
    rendered = [[P(str(cell), "CellHead" if header and r == 0 else "Cell") for cell in row] for r, row in enumerate(rows)]
    t = Table(rendered, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
    commands = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#B7C9D6")),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    if header:
        commands.append(("BACKGROUND", (0, 0), (-1, 0), NAVY))
        if len(rows) > 1:
            commands.append(("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PALE]))
    t.setStyle(TableStyle(commands))
    return t


def footer(canvas, doc):
    canvas.saveState()
    w, _ = A4
    canvas.setStrokeColor(colors.HexColor("#CBD5E1"))
    canvas.line(18 * mm, 15 * mm, w - 18 * mm, 15 * mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GRAY)
    canvas.drawString(18 * mm, 10 * mm, "VLSI Design Task 1 | Sumerix Global")
    canvas.drawRightString(w - 18 * mm, 10 * mm, f"Page {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(
    str(OUTPUT), pagesize=A4, rightMargin=18 * mm, leftMargin=18 * mm,
    topMargin=17 * mm, bottomMargin=21 * mm,
    title="VLSI Design Task 1 - Project Report",
    author="Vishnu Vamsi",
)
story = []

story += [Spacer(1, 15 * mm), P("VLSI DESIGN TASK 1", "CoverTitle"), P("Digital Arithmetic Logic Circuit Library Using Verilog HDL", "CoverSub"), Spacer(1, 4 * mm)]
story.append(table([
    ["Prepared for", "Industry-Oriented Internship Program on VLSI Design and Semiconductor Engineering"],
    ["Student", "Vishnu Vamsi"],
    ["Repository", "github.com/vishnuvamsi396-gif/VLSI-Design-Task-1"],
    ["Report date", "2026-11-01"],
], [34 * mm, 130 * mm], header=False))
story += [Spacer(1, 7 * mm), P("1. Objective", "Section"), P("Implement a small reusable combinational RTL library and demonstrate the Task 1 workflow: digital logic design, synthesizable Verilog, self-checking testbenches, Icarus Verilog simulation, waveform generation, and organized version-controlled documentation."), P("2. Scope", "Section"), P("The project includes basic logic gates, 2:1 and 4:1 multiplexers, half and full adders, a 4-bit ripple-carry adder, a parameterized unsigned adder, and a 4-bit arithmetic/logic mini-project unit. The assignment also introduces Linux-based development and the VLSI design flow; this introductory submission does not claim physical design, synthesis signoff, or chip fabrication."), P("3. Design inventory", "Section")]
story.append(table([
    ["Design", "Interface / purpose"],
    ["Basic gates", "AND, OR, XOR, NOT, NAND, NOR, XNOR; one-bit truth-table functions."],
    ["Multiplexers", "2:1 one-bit data selection; 4:1 one-bit selection from a 4-bit input bus."],
    ["Half adder", "Two one-bit inputs; sum and carry outputs."],
    ["Full adder", "Two one-bit inputs plus carry-in; sum and carry-out."],
    ["4-bit ripple adder", "Four cascaded full-adder stages with carry-in and carry-out."],
    ["Parameterized adder", "Unsigned WIDTH-bit addition with explicit carry-out."],
    ["Mini-project unit", "4-bit AND, OR, XOR, or addition selected by a 2-bit operation code."],
], [42 * mm, 122 * mm]))

story += [PageBreak(), P("4. Logic reference", "Section"), P("The following truth table is the reference for the single-bit gate implementation.")]
story.append(table([
    ["A", "B", "AND", "OR", "XOR", "NAND", "NOR", "XNOR"],
    ["0", "0", "0", "0", "0", "1", "1", "1"],
    ["0", "1", "0", "1", "1", "1", "0", "0"],
    ["1", "0", "0", "1", "1", "1", "0", "0"],
    ["1", "1", "1", "1", "0", "0", "0", "1"],
], [15 * mm] * 8))
story += [Spacer(1, 3 * mm), P("Boolean expressions", "SubSection"), P("Half adder: SUM = A XOR B; CARRY = A AND B.<br/>Full adder: SUM = A XOR B XOR Cin; Cout = AB + ACin + BCin.<br/>2:1 mux: Y = (~S AND D0) OR (S AND D1).", "BodySmall"), P("Karnaugh-map simplifications", "SubSection")]
story.append(table([
    ["Function", "Minterms", "Minimal SOP"],
    ["AND", "m3", "A.B"],
    ["OR", "m1, m2, m3", "A + B"],
    ["XOR", "m1, m2", "(~A.B) + (A.~B)"],
], [32 * mm, 42 * mm, 90 * mm]))
story += [Spacer(1, 5 * mm), P("Mini-project operation map", "SubSection")]
story.append(table([
    ["operation", "Result", "Carry-out"],
    ["00", "a AND b", "0"], ["01", "a OR b", "0"], ["10", "a XOR b", "0"], ["11", "unsigned a + b", "Addition carry"],
], [32 * mm, 73 * mm, 59 * mm]))
story += [P("5. VLSI context", "Section"), P("A typical digital IC flow proceeds from specification and architecture through RTL, functional verification, synthesis, implementation (floorplanning, placement, clock-tree synthesis, routing), signoff, and fabrication. ASICs are custom-fabricated for a target product; FPGAs provide reconfigurable programmable logic and are commonly used for prototyping and adaptable products. This repository focuses on introductory RTL and functional simulation."), P("RTL and simulation workflow", "SubSection"), P("Specification -> RTL modules -> self-checking testbenches -> iverilog compile -> vvp simulation -> pass/fail log and VCD -> GTKWave inspection -> screenshot evidence.")]

story += [PageBreak(), P("6. Verification plan and observed results", "Section"), P("The testbenches use self-checking comparisons and terminate with a fatal error on a mismatch. The suite was run in WSL with Icarus Verilog on 2026-11-01.")]
story.append(table([
    ["Testbench", "Coverage", "Result"],
    ["tb_basic_gates", "All 4 two-input combinations", "PASS"],
    ["tb_muxes", "8 2:1 input/select cases; 4 4:1 selections", "PASS"],
    ["tb_adders", "All half-adder and full-adder inputs", "PASS"],
    ["tb_ripple_carry_adder_4bit", "All 512 operand/carry-in combinations", "PASS"],
    ["tb_parameterized_adder", "1,024 deterministic 8-bit cases", "PASS"],
    ["tb_arithmetic_logic_library", "All 4 operations across 16 x 16 operands", "PASS"],
], [50 * mm, 83 * mm, 31 * mm]))
story += [Spacer(1, 4 * mm), P("The corresponding simulator logs are in `simulation/results/`; VCD traces are in `simulation/vcd/`. The run script is `scripts/run_all.sh` and returns a failure status if compilation or an assertion fails."), P("7. Waveform review and environment evidence", "Section"), P("PENDING: open the VCD files in GTKWave, inspect input/output transitions and carry propagation, and save genuine screenshots in `waveforms/`. VCD generation proves the simulator produced trace data; it does not prove that a person has visually inspected the traces."), P("PENDING: record the actual Ubuntu/WSL distribution and tool versions, and add the student's Linux command practice observations to `linux_report/command_practice.md`. This report does not claim a completed setup exercise."), P("8. Conclusion", "Section"), P("The RTL source and self-checking verification suite are prepared and the recorded simulator run passed all six testbenches. Waveform inspection, student environment evidence, and the final personal learning log remain to be completed before treating the submission checklist as fully complete."), P("Repository checklist", "SubSection")]
story.append(table([
    ["Deliverable", "Status"],
    ["RTL and testbench source", "Prepared; all six testbenches passed"],
    ["Simulation logs and VCD traces", "Included from the recorded WSL run"],
    ["Logic/K-map/design notes and workflow diagrams", "Included in docs/"],
    ["GTKWave screenshot evidence", "Pending actual visual inspection"],
    ["Linux environment practice evidence", "Pending student completion"],
], [80 * mm, 84 * mm]))

doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUTPUT)