#include <stdio.h>

int main(){
    printf("Enter a number: ");
    int num;
    scanf("%d",&num);
    int sum = (num*(num+1))/2;
    printf("Total sum is: %d ", sum);

    return 0;
}