module main();

  reg clk;

  initial begin
    clk = 1'b0;
  end
  always
    #5 clk = ~clk;

  initial begin
    #200 $finish;
  end

  initial
    $monitor($time, " clk = %d", clk);

endmodule
