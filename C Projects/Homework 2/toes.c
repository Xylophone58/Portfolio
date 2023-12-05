//Zach Mitchell
//700726936

//write a program that creates an interger variable called 'toes'. have the program set toes to 10.
//also have the program calculate what twice toes is and what toes squared is.
//the program should output 3 values

#include <stdio.h>

int main(void){
    int toes = 10;
    int toesx2 = toes * 2;
    int toesSquared = toes * toes;

    printf("The number of toes is %d.\n", toes);
    printf("The number of toes times 2 is %d.\n", toesx2);
    printf("The number of toes squared is %d.\n", toesSquared);

    return 0;
}