#include <stdio.h>
#include <limits.h>

void larg_small_diff(int arr[],int n){
    int small=INT_MAX,large=INT_MIN;
    for(int x=0;x<n;x++){
        if(arr[x]>=large){
            large = arr[x];
        }if(arr[x]<=small){
            small = arr[x];
        }
    }
    printf("The largest value is %d and smallest is %d", large, small);
    printf("\nDifference is: %d",large-small);
}

int main(){
    int n;
    printf("Enter the size of the array:");
    scanf("%d",&n);
    int arr[n];
    for(int x=0;x<n;x++){
        scanf("%d",&arr[x]);
    }
    larg_small_diff(arr,n);
    return 0;
}