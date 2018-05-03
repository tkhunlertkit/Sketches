`include "../FF/DFF.v"

module TFF(q, clk, reset);
  input clk, reset;
  output q;

  DFF d1(q, d, clk, reset);
  not n1(d, q);

endmodule
