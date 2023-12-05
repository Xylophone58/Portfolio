//Zach Mitchell 700726936

#include <stdio.h>

// Define the SUMSQ macro
#define SUMSQ(x, y) ((x)*(x) + (y)*(y))

int main() {
    int result1 = SUMSQ(4, 6);
    printf("SUMSQ(4, 6) = %d\n", result1); // Expected result: 52

    int result2 = SUMSQ(5 + 2, 1 + 8);
    printf("SUMSQ(5+2, 1+8) = %d\n", result2); // Expected result: 130

    return 0;
}