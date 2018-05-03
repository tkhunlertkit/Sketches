FILES = ./FF/TFF.v

#Actual Programs
run: prog
	./prog > output.txt

prog: $(FILES)
	iverilog -o prog $(FILES)

clean: output.txt prog
	rm output.txt prog
