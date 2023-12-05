//Zach Mitchell 700726936

#include <stdio.h>
#include <stdlib.h>

int main() {
    double num1, num2;
    char input[100];

    while (1) {
        printf("Enter the first floating-point number (or non-numeric input to exit): ");
        if (fgets(input, sizeof(input), stdin) == NULL || sscanf(input, "%lf", &num1) != 1) {
            printf("Exiting the program.\n");
            break;
        }

        printf("Enter the second floating-point number: ");
        if (fgets(input, sizeof(input), stdin) == NULL || sscanf(input, "%lf", &num2) != 1) {
            printf("Exiting the program.\n");
            break;
        }

        if (num2 == 0) {
            printf("Error: Division by zero. Please enter a non-zero second number.\n");
            continue;  
        }

        double result = (num1 - num2) / (num1 * num2);
        printf("Result: %.4lf\n", result);
    }

    return 0;
}
