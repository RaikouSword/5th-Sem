#include <stdio.h>

int main(){
    int n, pos;
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
    printf("\nEnter the pos(1-based): ");
    scanf("%d",&pos);

    if(pos<1 || pos >n){
        printf("Invalid Input!!");
    }else{
        for(int x=pos-1;x<n-1;n++){
            arr[x]= arr[x+1];
        }
        n--;
        printf("Array after deletion: ");
        for(int x=0;x<n;x++){
            printf("%d ",arr[x]);
        }
        printf("\n");
    }
    return 0;
}