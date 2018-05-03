TB = Ripple_Carry_Counter_tb counter_tb

#Actual Programs
run: $(TB)

Ripple_Carry_Counter_tb:
	iverilog -o Ripple_Carry_Counter_tb Ripple_Carry_Counter_test.v
	vvp Ripple_Carry_Counter_tb

counter_tb: counter_tb.v
	iverilog -o counter_tb counter_tb.v
	vvp counter_tb

clean:
	rm $(TB) *.vcd
