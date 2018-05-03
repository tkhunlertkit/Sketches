#include "gtest/gtest.h"

class ExampleTestSuite : public ::testing::Test {
    virtual void SetUp() {

    }
    virtual void TearDown() {
      // Code here will be called immediately after each test
      // (right before the destructor).
    }
};

TEST(ExampleTestSuite, PositiveNos) { 
    EXPECT_EQ (2, 1 + 1);
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}