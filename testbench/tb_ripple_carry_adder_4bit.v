`timescale 1ns/1ps
module tb_ripple_carry_adder_4bit;
    reg [3:0] a,b; reg cin; wire [3:0] sum; wire cout;
    integer i; reg [4:0] expected;
    ripple_carry_adder_4bit dut(a,b,cin,sum,cout);
    initial begin
        $dumpfile("simulation/vcd/tb_ripple_carry_adder_4bit.vcd"); $dumpvars(0,tb_ripple_carry_adder_4bit);
        for(i=0;i<512;i=i+1) begin
            {a,b,cin}=i; #1; expected={1'b0,a}+{1'b0,b}+cin;
            if({cout,sum} !== expected) $fatal(1,"4-bit adder mismatch a=%h b=%h cin=%b",a,b,cin);
        end
        $display("PASS tb_ripple_carry_adder_4bit (512 combinations)"); $finish;
    end
endmodule
