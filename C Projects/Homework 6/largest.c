//Zach Mitchell 700726936

#include <stdio.h>

int array_largest(int arr[], int size) {
    int largest = arr[0]; // Assume the first element is the largest

    for (int i = 1; i < size; i++) {
        if (arr[i] > largest) {
            largest = arr[i];
        }
    }

    return largest;
}

int main() {
    int arr1[] = {14, -27, 19, 56, 104};
    int size1 = sizeof(arr1) / sizeof(arr1[0]);

    int arr2[] = {78, 12, 1015, 738, -14, 12, 49};
    int size2 = sizeof(arr2) / sizeof(arr2[0]);

    int largest1 = array_largest(arr1, size1);
    int largest2 = array_largest(arr2, size2);

    // Print the results to the console
    printf("Largest value in array1: %d\n", largest1);
    printf("Largest value in array2: %d\n", largest2);

    return 0;
}