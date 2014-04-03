// fizz.cpp

#include "fizz.h"

std::string Fizz::fizzOrBuzz(int i)
{
  if((i % 5 == 0) && (i % 3 ==0))
    return "FizzBuzz";
  if(i % 5 == 0)
    return "Buzz";
  if(i % 3 == 0)
    return "Fizz";
  char buffer[50];
  std::string return_str;
  return_str = sprintf(buffer, "%d", i);
  return buffer;
}
