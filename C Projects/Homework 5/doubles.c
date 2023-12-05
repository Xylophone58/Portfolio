//Zach Mitchell 700726936

#include <stdio.h>

void double_sort(double *a, double *b, double *c) {
    double temp;
    
    if (*a > *b) {
        temp = *a;
        *a = *b;
        *b = temp;
    }
    
    if (*a > *c) {
        temp = *a;
        *a = *c;
        *c = temp;
    }
    
    if (*b > *c) {
        temp = *b;
        *b = *c;
        *c = temp;
    }
}

int main() {
    double num1, num2, num3;
    
    printf("Enter the first double value: ");
    scanf("%lf", &num1);
    
    printf("Enter the second double value: ");
    scanf("%lf", &num2);
    
    printf("Enter the third double value: ");
    scanf("%lf", &num3);
    
    double_sort(&num1, &num2, &num3);
    
    printf("Sorted values: %.2lf, %.2lf, %.2lf\n", num1, num2, num3);
    
    return 0;
}