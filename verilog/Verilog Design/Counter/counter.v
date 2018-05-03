module counter(out, clk, rst);

parameter WIDTH = 8;

input clk, rst;
output [WIDTH-1:0] out;

reg [WIDTH-1:0] out;

always@(posedge clk, posedge rst)
begin
	if(rst)
		out <= 0;
	else
		out <= out+1;
end

endmodule

