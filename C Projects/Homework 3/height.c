//Zach Mithell 700726936

/*Write a program that requests your height in inches and your name, and then displays the information in the following form:

Dabney, you are 6.208 feet tall*/

#include <stdio.h>

int main() {
    float inches;
    char name[100];

    printf("Enter your height in inches: ");
    scanf("%f", &inches);

    printf("Enter your name: ");
    scanf("%s", name);

    float feet = inches / 12.0;

    printf("%s, you are %.3f feet tall\n", name, feet);

    return 0;
}


