`timescale 1ns/1ps
module tb_parameterized_adder;
    reg [7:0] a,b; reg cin; wire [7:0] sum; wire cout;
    integer i; reg [8:0] expected;
    parameterized_adder #(.WIDTH(8)) dut(a,b,cin,sum,cout);
    initial begin
        $dumpfile("simulation/vcd/tb_parameterized_adder.vcd"); $dumpvars(0,tb_parameterized_adder);
        for(i=0;i<1024;i=i+1) begin
            a=(i*37)%256; b=(i*91)%256; cin=i[0]; #1;
            expected={1'b0,a}+{1'b0,b}+cin;
            if({cout,sum} !== expected) $fatal(1,"parameterized adder mismatch");
        end
        $display("PASS tb_parameterized_adder (1024 deterministic 8-bit cases)"); $finish;
    end
endmodule
