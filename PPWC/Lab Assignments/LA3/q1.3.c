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
    int small=INT_MAX,large=INT_MIN;
    for(int x=0;x<n;x++){
        if(arr[x]>=large){
            large = arr[x];
        }if(arr[x]<=small){
            small = arr[x];
        }
    }
    printf("The largest value is %d and smallest is %d", large, small);
    printf("Difference is: %d",large-small);
    return 0;
}