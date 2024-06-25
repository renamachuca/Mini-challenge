#include <iostream>
#include <string>
#include <algorithm>

bool esPalindromo(const std::string& cadena) {
    std::string cadenaLimpia;
    for (char c : cadena) {
        if (std::isalnum(c)) {
            cadenaLimpia += std::tolower(c);
        }
    }
    std::string reverso = cadenaLimpia;
    std::reverse(reverso.begin(), reverso.end());
    return cadenaLimpia == reverso;
}

int main() {
    std::string cadena;
    std::cout << "Ingrese una cadena: ";
    std::getline(std::cin, cadena);
    if (esPalindromo(cadena)) {
        std::cout << "La cadena es un palindromo." << std::endl;
    } else {
        std::cout << "La cadena no es un palindromo." << std::endl;
    }

    return 0;
}
