`timescale 1ns/1ps
module tb_muxes;
    reg d0,d1,sel; wire y2;
    reg [3:0] d; reg [1:0] sel4; wire y4;
    integer i;
    mux2_1 u2(d0,d1,sel,y2); mux4_1 u4(d,sel4,y4);
    initial begin
        $dumpfile("simulation/vcd/tb_muxes.vcd"); $dumpvars(0,tb_muxes);
        for(i=0;i<8;i=i+1) begin
            {d0,d1,sel}=i[2:0]; #1;
            if(y2 !== (sel ? d1 : d0)) $fatal(1,"2:1 mux mismatch");
        end
        d=4'b1010;
        for(i=0;i<4;i=i+1) begin
            sel4=i[1:0]; #1;
            if(y4 !== d[sel4]) $fatal(1,"4:1 mux mismatch sel=%b",sel4);
        end
        $display("PASS tb_muxes (8 2:1 cases, 4 4:1 selections)"); $finish;
    end
endmodule
