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
    return 0;
}