#include <iostream>

int main() {
    int num1, num2, suma;
    std::cout << "Introduce el primer numero: ";
    std::cin >> num1;
    std::cout << "Introduce el segundo numero: ";
    std::cin >> num2;
    suma = num1 + num2;
    std::cout << "La suma de " << num1 << " y " << num2 << " es: " << suma << std::endl;
    return 0;
}
