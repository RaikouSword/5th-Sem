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
    if(org==rev){
        printf("%d is a palindrome number", org);
    }else{
        printf("%d isn't a palindrome", org);
    }

    return 0;
}