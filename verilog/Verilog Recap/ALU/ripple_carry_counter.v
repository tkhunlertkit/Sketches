`include "../FF/TFF.v"
module ripple_carry_counter(q, clk, reset);

  output [3:0] q;
  input clk, reset;

  TFF t0(q[0], clk, reset);
  TFF t1(q[1], q[0], reset);
  TFF t2(q[2], q[1], reset);
  TFF t3(q[3], q[2], reset);

endmodule
