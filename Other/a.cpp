#include <iostream>

int main()
{
    std::string a;
    std::cout << "Your name: ";
    std::getline(std::cin, a);
    std::cout << "Hello " << a << "\n";
    return 0;
}