//Zach Mitchell 700726936

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* duplicate(const char *str) {
    // Allocate memory for the duplicated string
    char *duplicate_str = (char*)malloc(strlen(str) + 1);

    if (duplicate_str != NULL) {
        strcpy(duplicate_str, str); // Copy the contents of the original string
    }

    return duplicate_str;
}

int main() {
    const char *str1 = "This is a test";
    const char *str2 = "Hello from the duplicate!";

    // Duplicate the first string
    char *p1 = duplicate(str1);
    if (p1 != NULL) {
        printf("Duplicated string 1: %s\n", p1);
        free(p1);
    } else {
        printf("Memory allocation failed for string 1.\n");
    }

    // Duplicate the second string
    char *p2 = duplicate(str2);
    if (p2 != NULL) {
        printf("Duplicated string 2: %s\n", p2);
        free(p2);
    } else {
        printf("Memory allocation failed for string 2.\n");
    }

    return 0;
}
