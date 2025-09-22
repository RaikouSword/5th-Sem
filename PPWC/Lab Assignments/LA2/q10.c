#include <stdio.h>

int main(){
    int num, count=0, div;
    printf("Enter a number: ");
    scanf("%d", &num);
    int org = num;
    while(num!=0){
        div = num%2;
        if(div==1){
            count++;
            if(count==2){
                break;
            }
        }
        num/=2;
    }
    if(count<2){
        printf("%d is a power of 2", org);
    }else{
        printf("%d is not a power of 2",org);
    }

    return 0;
}