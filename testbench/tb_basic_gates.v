`timescale 1ns/1ps
module tb_basic_gates;
    reg a, b;
    wire and_y, or_y, xor_y, not_y, nand_y, nor_y, xnor_y;
    integer i;
    reg [6:0] expected;

    and_gate u0(a,b,and_y); or_gate u1(a,b,or_y); xor_gate u2(a,b,xor_y);
    not_gate u3(a,not_y); nand_gate u4(a,b,nand_y); nor_gate u5(a,b,nor_y); xnor_gate u6(a,b,xnor_y);

    initial begin
        $dumpfile("simulation/vcd/tb_basic_gates.vcd"); $dumpvars(0,tb_basic_gates);
        for (i=0; i<4; i=i+1) begin
            {a,b}=i[1:0]; #1;
            expected = {~(a^b), ~(a|b), ~(a&b), ~a, a^b, a|b, a&b};
            if ({xnor_y,nor_y,nand_y,not_y,xor_y,or_y,and_y} !== expected)
                $fatal(1,"gate mismatch a=%b b=%b",a,b);
        end
        $display("PASS tb_basic_gates (4 input combinations)"); $finish;
    end
endmodule
