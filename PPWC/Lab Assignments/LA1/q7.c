#include <stdio.h>

int main(){
    int a = 10;
    float b = 10.55555;
    double c= 19.49;
    char d = "D";
    short e = 6;

    printf("%lu\n", sizeof(a));
    printf("%zu\n", sizeof(b));
    printf("%zu\n", sizeof(c));
    printf("%zu\n", sizeof(d));
    printf("%zu\n", sizeof(e));

    return 0;
}