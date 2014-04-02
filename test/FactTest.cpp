
#include <gtest/gtest.h>
#include "../Numbers/factorial/fact.h"
#include "../Numbers/factorial/fact.cpp"


TEST(FactTest, Fact0) {
  EXPECT_EQ(Fact::get_fact(0), 1);
}

