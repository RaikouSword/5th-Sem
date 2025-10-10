#include <stdio.h>
#include <limits.h>

void smol_and_ssmol(int arr[],int n){
    int smol=INT_MAX,ssmol=INT_MAX;
    for(int x=0;x<n;x++){
        if(arr[x]<=smol){
            ssmol =smol;
            smol = arr[x];
        }else if (arr[x]<=ssmol && arr[x]>smol){
            ssmol = arr[x];
        }else{
            continue;
        }
    }
    printf("The smallest value is %d and second smallest is %d", smol, ssmol);
}

int main(){
    int n;
    printf("Enter the size of the array:");
    scanf("%d",&n);
    int arr[n];
    for(int x=0;x<n;x++){
        scanf("%d",&arr[x]);
    }
    smol_and_ssmol(arr,n);
    return 0;
}