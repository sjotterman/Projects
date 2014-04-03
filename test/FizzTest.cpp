#include <gtest/gtest.h>
#include "../Text/fizzbuzz/fizz.h"
#include "../Text/fizzbuzz/fizz.cpp"


/**************************************** 
 * Note, to convert int to string, you will need to use sprintf or some other
 * similar function.
 ****************************************/
 
 TEST(FizzTest, Fizz0) {
  EXPECT_EQ(Fizz::fizzOrBuzz(0), "FizzBuzz"); }

TEST(FizzTest, Fizz1to15) {
  EXPECT_EQ(Fizz::fizzOrBuzz(1), "1");
  EXPECT_EQ(Fizz::fizzOrBuzz(2), "2");
  EXPECT_EQ(Fizz::fizzOrBuzz(3), "Fizz");
  EXPECT_EQ(Fizz::fizzOrBuzz(4), "4");
  EXPECT_EQ(Fizz::fizzOrBuzz(5), "Buzz");
  EXPECT_EQ(Fizz::fizzOrBuzz(6), "Fizz");
  EXPECT_EQ(Fizz::fizzOrBuzz(7), "7");
  EXPECT_EQ(Fizz::fizzOrBuzz(8), "8");
  EXPECT_EQ(Fizz::fizzOrBuzz(9), "Fizz");
  EXPECT_EQ(Fizz::fizzOrBuzz(10), "Buzz");
  EXPECT_EQ(Fizz::fizzOrBuzz(11), "11");
  EXPECT_EQ(Fizz::fizzOrBuzz(12), "Fizz");
  EXPECT_EQ(Fizz::fizzOrBuzz(13), "13");
  EXPECT_EQ(Fizz::fizzOrBuzz(14), "14");
  EXPECT_EQ(Fizz::fizzOrBuzz(15), "FizzBuzz");
}
