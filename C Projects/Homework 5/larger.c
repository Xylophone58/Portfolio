//Zach Mitchell 700726936

#include <stdio.h>

void larger_of(double *x, double *y) {
    if (*x < *y) {
        *x = *y;
    } else {
        *y = *x;
    }
}

int main() {
    double x, y;

    printf("Enter the first double value: ");
    scanf("%lf", &x);

    printf("Enter the second double value: ");
    scanf("%lf", &y);

    larger_of(&x, &y);

    printf("The larger value is: %lf\n", x);

    return 0;
}