#include <stdio.h>

int main(){
    printf("Enter a number: ");
    int num;
    scanf("%d", &num);
    print("Fibonacci series: ");
    for(int x=1;x<num;x++){
        int first = x;
        int second = x+1;
        int third = first +second;
        printf("%d", third);
    }
    return 0;
}