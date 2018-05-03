module test;

    parameter WIDTH = 10;
    
    reg reset = 0;
    
    
    initial begin
        $dumpfile("test.vcd");
        $dumpvars(0,test);
        
        #17 reset = 1;
        #11 reset = 0;
        #29 reset = 1;
        #5  reset = 0;
        #2000 $finish;
    end
    
    reg clk = 0;
    always #1 clk = ~clk;
    
    wire [WIDTH-1:0] value;
    counter #(WIDTH) c1(value, clk, reset);
    
    initial begin
        $monitor("At time %t, value = %h (%0d)", $time, value, value);
    end
    
endmodule