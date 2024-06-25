#include <iostream>
#include <vector>
#include <algorithm> 

void imprimirArray(const std::vector<int>& arr) {
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
}

void ordenarArray(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i) {
        int min_idx = i;
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        std::swap(arr[i], arr[min_idx]);
    }
}

int main() {
    std::vector<int> arr = {625, 3584, 200, 369, 5864 };

    std::cout << "Array original: ";
    imprimirArray(arr);
    ordenarArray(arr);

    std::cout << "Array ordenado: ";
    imprimirArray(arr);

    return 0;
}
