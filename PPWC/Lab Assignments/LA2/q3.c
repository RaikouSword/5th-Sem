#include <stdio.h>
#include <math.h>

int main(){
    printf("Enter a number: ");
    int num;
    scanf("%d", &num);
    int count=0;
    for(int x=2;x<num;x++){
        if(num%x==0){
            count++;
            break;
        }
    }
    if(count!=0){
        printf("%d isn't prime number", num);
    }else{
        printf("%d is a prime number", num);
    }
    
    return 0;
}