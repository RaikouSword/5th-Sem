#include <stdio.h>

int main(){
    printf("Enter a number: ");
    int num;
    scanf("%d", &num);
    int res =1;
    while(num>0){
        res*=num;
        num--;
    }
    printf("%d", res);

    return 0;
}