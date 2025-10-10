#include <stdio.h>

void remove_duplicates_from_array(int arr[],int n){
    int count=1,low=0,high=low+1;
    while(high<n){
        if(arr[low]!=arr[high]){
            low++;
            int temp = arr[high];
            arr[high] = arr[low];
            arr[low] = temp;
            count++;
        }
        high++;
    }
    n=count;
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
    remove_duplicates_from_array(arr,n);
    printf("\nArray is:");
    for(int x=0;x<n;x++){
        printf("%d ",arr[x]);
    }
    return 0;
}