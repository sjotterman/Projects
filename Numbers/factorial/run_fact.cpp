#include <iostream>
#include "fact.h"


int main()
{
std::cout << "Enter an integer. " << std::endl << "> ";
int num;
std::cin >> num;
std::cout << "Fact of " << num << " is: " << Fact::get_fact(num) << std::endl;

}
