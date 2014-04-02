#include <gtest/gtest.h>
#include "../Numbers/fib/fib.h"
#include "../Numbers/fib/fib.cpp"


TEST(FibTest, Fib0) {
  EXPECT_EQ(Fib::get_fib(0), 0);
}

TEST(FibTest, Fib1) {
  EXPECT_EQ(Fib::get_fib(1), 1);
}

TEST(FibTest, Fib2) {
  EXPECT_EQ(Fib::get_fib(2), 1);
}

TEST(FibTest, Fib3) {
  EXPECT_EQ(Fib::get_fib(3), 2);
}

TEST(FibTest, Fib4) {
  EXPECT_EQ(Fib::get_fib(4), 3);
}

TEST(FibTest, Fib5) {
  EXPECT_EQ(Fib::get_fib(5), 5);
}

TEST(FibTest, Fib6) {
  EXPECT_EQ(Fib::get_fib(6), 8);
}

TEST(FibTest, Fib20) {
  EXPECT_EQ(Fib::get_fib(20), 6765);
}
