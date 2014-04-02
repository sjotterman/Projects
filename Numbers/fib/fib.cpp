//fib.cc
#include "fib.h"

int Fib::get_fib(int n)
{
  if(n == 0){ return 0;}
  if(n < 3){ return 1; }
  return get_fib(n -1) + get_fib(n -2);
}
