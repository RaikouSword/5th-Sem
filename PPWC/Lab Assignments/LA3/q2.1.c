#include <stdio.h>

void separate_oddEven(int arr[],int n ){
    int p1=0;
    for(int i=0;i<n;i++){
        if(arr[i]%2==0){
            p1=i;
            break;
        }
    }
    for(int j=p1;j<n;j++){
        if(arr[j]%2==1){
            int temp = arr[p1];
            arr[p1] = arr[j];
            arr[j] = temp;
            p1++;
        }
    }
}

int main(){
    int n;
    scanf("%d",&n);
    int v[n];
    for(int i=0;i<n;i++){
        scanf("%d",&v[i]);
    }
    separate_oddEven(v,n);
    for(int i=0;i<n;i++){
        printf("%d ",v[i]);
    }
    return 0;
}