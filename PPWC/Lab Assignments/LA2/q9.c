#include <stdio.h>

int main(){
    printf("Enter a number: ");
    int num, rem, rev=0;
    scanf("%d", &num);
    int org = num;
    while (num != 0) {
        rem = num % 10;          
        rev = rev * 10 + rem;  
        num /= 10;                      
    }
    printf("Reversed num is: %d ", rev);

    return 0;
}