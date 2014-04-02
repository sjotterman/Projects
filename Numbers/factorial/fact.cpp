// fact.cpp
#include "fact.h"

int Fact::get_fact(int n)
{
  if (n < 2){ return 1;}
  int total = n;
  for(int i = n; i > 2; --i)
  {
    total *= i - 1;
  }
  return total;
}
