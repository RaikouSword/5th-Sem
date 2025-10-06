#include <stdio.h>

int main(){
    int n;
    scanf("%d",&n);
    int v[n];
    for(int i=0;i<n;i++){
        scanf("%d",&v[i]);
    }

    int p1=0;
    for(int i=0;i<n;i++){
        if(v[i]%2==0){
            p1=i;
            break;
        }
    }
    for(int j=p1;j<n;j++){
        if(v[j]%2==1){
            int temp = v[p1];
            v[p1] = v[j];
            v[j] = temp;
            p1++;
        }
    }

    for(int i=0;i<n;i++){
        printf("%d ",v[i]);
    }
    return 0;
}