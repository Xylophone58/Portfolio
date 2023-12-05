//Zach Mitchell 700726936

#include <stdio.h>

int main() {
    #ifdef FIRST
        printf("I print if FIRST is defined\n");
    #endif

    #ifdef SECOND
        printf("I print if SECOND is defined\n");
    #endif

    #if defined(FIRST) && defined(SECOND)
        printf("I print if FIRST and SECOND are defined\n");
    #endif

    return 0;
}