module DFF(q, d, clk, reset);
  input d, clk, reset;
  output q;
  reg q;

  always @ (negedge clk or posedge reset)
  if (reset) begin
    q <= 1'b0;
  end else begin
    q <= d;
  end

endmodule
