run: prog
	vvp prog

prog: counter.v test.v
	iverilog -o prog test.v counter.v

clean:
	rm prog *~ *.vcd