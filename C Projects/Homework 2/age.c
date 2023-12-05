//Zach Mitchell
//700726936

//Write a program that converts your age in years to days and displays both values

#include <stdio.h>
int main(void){
    int age;
    int ageDays;

    printf("Enter your current age: ");
    scanf("%d", &age);

    ageDays = age * 365;

    printf("Your age in years is: %d.\n", age);
    printf("Your age in days is at least: %d.\n", ageDays);

    return 0;
}