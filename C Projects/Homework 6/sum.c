//Zach Mitchell 700726936

#include <stdio.h>

void sum_arrays(int arr1[], int arr2[], int arr3[], int size) {
    for (int i = 0; i < size; i++) {
        arr3[i] = arr1[i] + arr2[i];
    }
}

int main() {
    int arr1[] = {4, -10, 15, 296, 42};
    int arr2[] = {15, 27, 89, -204, 76};
    int size = sizeof(arr1) / sizeof(arr1[0]);

    int arr3[size]; // Create an array to store the sum

    sum_arrays(arr1, arr2, arr3, size);

    // Print the results from the third array
    printf("Result array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr3[i]);
    }
    printf("\n");

    return 0;
}