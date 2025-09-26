#include <stdio.h>
#include <limits.h>

int main(){
    int n;
    printf("Enter the size of the array:");
    scanf("%d",&n);
    int arr[n];
    for(int x=0;x<n;x++){
        scanf("%d",&arr[x]);
    }
    int larg=INT_MIN,slarg=INT_MIN;
    for(int x=0;x<n;x++){
        if(arr[x]>larg){
            slarg =larg;
            larg = arr[x];
        }else if (arr[x]>=slarg && arr[x]<larg){
            slarg = arr[x];
        }else{
            continue;
        }
    }
    printf("The largest value is %d and second largest is %d", larg, slarg);
    return 0;
}