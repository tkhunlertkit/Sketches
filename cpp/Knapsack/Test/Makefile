CXX = g++
CXXFLAGS = -g -L/usr/local/Cellar/gtest -lgtest -lgtest_main -lpthread
INCS = -I./ -I../../src -I/usr/local/include/gtest
OBJS = ExampleTestSuite.o

testAll: $(OBJS)
	$(CXX) $(CXXFLAGS) $(INCS) -o testAll  ExampleTestSuite.cpp $(OBJS)

.cpp.o:
	$(CXX) $(CXXFLAGS) -c $< -o $@ $(INCS)

clean:
	rm testAll *.o testAll.xml