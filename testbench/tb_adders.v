`timescale 1ns/1ps
module tb_adders;
    reg a,b,cin; wire hs,hc,fs,fc;
    integer i; reg [1:0] total;
    half_adder ha(a,b,hs,hc); full_adder fa(a,b,cin,fs,fc);
    initial begin
        $dumpfile("simulation/vcd/tb_adders.vcd"); $dumpvars(0,tb_adders);
        for(i=0;i<8;i=i+1) begin
            {a,b,cin}=i[2:0]; #1;
            total={1'b0,a}+{1'b0,b};
            if({hc,hs} !== total) $fatal(1,"half adder mismatch");
            total={1'b0,a}+{1'b0,b}+cin;
            if({fc,fs} !== total) $fatal(1,"full adder mismatch");
        end
        $display("PASS tb_adders (all half/full-adder input combinations)"); $finish;
    end
endmodule
