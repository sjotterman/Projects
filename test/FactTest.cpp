
#include <gtest/gtest.h>
#include "../Numbers/factorial/fact.h"
#include "../Numbers/factorial/fact.cpp"


TEST(FactTest, Fact0) {
  EXPECT_EQ(Fact::get_fact(0), 1);
}

TEST(FactTest, Fact1) {
  EXPECT_EQ(Fact::get_fact(1), 1);
}

TEST(FactTest, Fact2) {
  EXPECT_EQ(Fact::get_fact(2), 2);
}

TEST(FactTest, Fact7) {
  EXPECT_EQ(Fact::get_fact(7), 5040);
}

TEST(FactTest, Fact12) {
  EXPECT_EQ(Fact::get_fact(12), 479001600);
}
