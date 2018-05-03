`include "../ALU/counter.v"

module counter_tb();

  reg EN, CLK, RST;
  wire [3:0] C_OUT;

  counter c1(.en(EN), .clk(CLK), .rst(RST), .cout(C_OUT));

  initial begin
    $dumpfile("test.vcd");
    $dumpvars(0,counter_tb);

    CLK = 1'b0;
    RST = 1'b0;
    EN  = 1'b0;

    #5   RST = 1'b1;
    #10  RST = 1'b0;
    #10  EN  = 1'b1;
    #100 EN  = 1'b0;

    #5 $finish;
  end

  always #2 CLK = !CLK;
endmodule
