#include <cpptest-suite.h>

class ExampleTestSuite : public Test::Suite {
	public:
		ExampleTestSuite()
	    {
	        TEST_ADD(ExampleTestSuite::first_test)
	        TEST_ADD(ExampleTestSuite::second_test)
	    }

	private:
		void first_test();
	    void second_test();
};