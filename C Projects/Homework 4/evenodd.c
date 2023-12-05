//Zach Mitchell 700726936

#include <stdio.h>

int main() {
    int num, even = 0, odd = 0;
    int even_sum = 0, odd_sum = 0;

    printf("Enter integers (0 to terminate):\n");

    while (1) {
        printf("Enter an integer: ");
        scanf("%d", &num);

        if (num == 0) {
            break;  
        }

        if (num % 2 == 0) {
            even++;
            even_sum += num;
        } else {
            odd++;
            odd_sum += num;
        }
    }

    if (even > 0) {
        double even_average = (double)even_sum / even;
        printf("Total even integers: %d\n", even);
        printf("Average value of even integers: %.2lf\n", even_average);
    } else {
        printf("No even integers were entered.\n");
    }

    if (odd > 0) {
        double odd_average = (double)odd_sum / odd;
        printf("Total odd integers: %d\n", odd);
        printf("Average value of odd integers: %.2lf\n", odd_average);
    } else {
        printf("No odd integers were entered.\n");
    }

    return 0;
}