//Zach Mitchell 700726936

#include <stdio.h>

int times_called() {
    static int count = 0;
    
    return ++count;
}

int main() {
    int i;

    for (i = 1; i <= 10; i++) {
        int call_count = times_called();
        printf("Function has been called %d times.\n", call_count);
    }

    return 0;
}