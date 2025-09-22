#include <stdio.h>

int main(){
    printf("Enter a number: ");
    int num;
    scanf("%d", &num);
    int first =0, second = 1, third;
    if(num==1){
        printf("0");
    }else if(num==2){
        printf("0 1");
    }else{
        printf("0 1 ");
        num-=2;
        while(num>0){
            third = first+second;
            printf("%d ", third);
            first = second;
            second = third;
            num--;
        }
    }
    printf("\n");
    return 0;
}