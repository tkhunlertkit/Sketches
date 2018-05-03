ALL_TESTS = test_Ripple_Carry_Counter

# TestBenches
run_all_tests: $(ALL_TESTS)

test_Ripple_Carry_Counter:
	iverilog -o ./tmp/Ripple_Carry_Counter_tb Ripple_Carry_Counter_test.v
	./tmp/Ripple_Carry_Counter_tb
