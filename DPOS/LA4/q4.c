#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <math.h>

void fibo(int *ptr,int n){
    int a=0,b=1;
    *ptr =a;
    ptr++;
    *ptr =b;
    ptr++;
    n-=2;
    while(n--){
        int c = a+b;
        *ptr = c;
        ptr++;
        a =b;
        b=c;
    }
}
int isPrime(int num){
    if(num<=1) return 0;
    int res =1;
    for(int x=2;x*x<=num;x++){
        if(num%x==0) return 0;
    }
    return 1;
}

int main(){
    int n;
    printf("Enter length: ");
    scanf("%d",&n);
    int arr[n];
    if(vfork()==0){
        fibo(arr,n);
        _exit(0);
    }else{
        // wait(NULL);
        for(int x=0;x<n;x++){
            printf("%d ",arr[x]);
        }
        printf("\n");
        for(int x=0;x<n;x++){
            if(isPrime(arr[x])==1){
                printf("Ele:%d and Pos:%d\n",arr[x],x);
            }
        }
    }

    return 0;
}