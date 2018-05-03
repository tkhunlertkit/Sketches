`include "../ALU/ripple_carry_counter.v"

module test;
  reg clk;
  reg reset;
  wire[3:0] q;

  ripple_carry_counter r1(q, clk, reset);

  initial
    clk = 1'b0;
  always
    #5 clk = ~clk;

  initial begin
    $dumpfile("test.vcd");
    $dumpvars(0,test);
    reset = 1'b1;
    #15 reset = 1'b0;
    #180 reset = 1'b1;
    #10 reset = 1'b0;
    #20 $finish;
  end

  initial
    $monitor($time, " Output q = %d", q);

endmodule
