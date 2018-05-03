module counter(en, clk, rst, cout);

  input en, clk, rst;
  output [3:0] cout;

  reg [3:0] cout;

  always @ (posedge clk) begin
    if (rst) begin
      cout <= 4'b0;
    end else if (en) begin
      cout <= cout + 1;
    end
  end

endmodule
