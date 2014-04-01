#include <gtest/gtest.h>
#include "fib.h"
#include "fib.cpp"

TEST(MathTest, TwoPlusTwoEqualsFour) {
  EXPECT_EQ(4, 2 + 2);
}

TEST(FibTest, Fib1) {
  EXPECT_EQ(Fib::get_fib(1), 1);
}

int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
