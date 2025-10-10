#include <stdio.h>

void reverse(int arr[],int n){
    int low=0,high=n-1;
    while(low<=high){
        int temp = arr[high];
        arr[high] = arr[low];
        arr[low] = temp;
        high--;
        low++;
    }
}

int main(){ 
    int n;
    printf("Enter the size of the array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the numbers: ");
    for(int x=0;x<n;x++){
        scanf("%d",&arr[x]);
    }
    printf("\nArray is:");
    for(int x=0;x<n;x++){
        printf("%d ",arr[x]);
    }
    reverse(arr,n);
    printf("\nArray is:");
    for(int x=0;x<n;x++){
        printf("%d ",arr[x]);
    }
    return 0;
}