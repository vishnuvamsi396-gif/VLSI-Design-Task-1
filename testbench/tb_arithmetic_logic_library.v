`timescale 1ns/1ps
module tb_arithmetic_logic_library;
    reg [3:0] a,b; reg [1:0] operation; wire [3:0] result; wire carry_out;
    integer i,j; reg [4:0] expected;
    arithmetic_logic_library dut(a,b,operation,result,carry_out);
    initial begin
        $dumpfile("simulation/vcd/tb_arithmetic_logic_library.vcd"); $dumpvars(0,tb_arithmetic_logic_library);
        for(i=0;i<16;i=i+1) for(j=0;j<16;j=j+1) begin
            a=i; b=j;
            operation=2'b00; #1; if(result !== (a&b) || carry_out !== 1'b0) $fatal(1,"AND operation mismatch");
            operation=2'b01; #1; if(result !== (a|b) || carry_out !== 1'b0) $fatal(1,"OR operation mismatch");
            operation=2'b10; #1; if(result !== (a^b) || carry_out !== 1'b0) $fatal(1,"XOR operation mismatch");
            operation=2'b11; #1; expected={1'b0,a}+{1'b0,b}; if({carry_out,result} !== expected) $fatal(1,"ADD operation mismatch");
        end
        $display("PASS tb_arithmetic_logic_library (1024 operation/input cases)"); $finish;
    end
endmodule
