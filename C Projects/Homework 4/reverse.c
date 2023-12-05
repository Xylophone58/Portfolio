//Zach Mitchell 700726936

#include <stdio.h>

int main() {
    int numbers[8];

    // Read eight integers into the array
    printf("Enter eight integers, one at a time:\n");
    for (int i = 0; i < 8; i++) {
        printf("Enter integer %d: ", i + 1);
        scanf("%d", &numbers[i]);
    }

    // Print the integers in reverse order
    printf("Integers in reverse order:\n");
    for (int i = 7; i >= 0; i--) {
        printf("%d\n", numbers[i]);
    }

    return 0;
}