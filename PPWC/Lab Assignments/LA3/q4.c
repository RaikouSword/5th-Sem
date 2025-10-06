#include<stdio.h>

int main(){
    int n;
    scanf("%d",&n);
    int v1[n];
    for(int i=0;i<n;i++){
        scanf("%d",&v1[i]);
    }
    int m;
    scanf("%d",&m);
    int v2[m];
    for(int i=0;i<m;i++){
        scanf("%d",&v2[i]);
    }
    
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(v1[i]==v2[j])
            printf("%d ",v1[i]);
        }
    }
    return 0;
}