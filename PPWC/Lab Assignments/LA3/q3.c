#include<stdio.h>

void merge(int v1[],int v2[],int n,int m){
    int v3[n+m];
    int p1=0,p2=0,p3=0;
    while(p1<n && p2<m){
        if(v1[p1]<=v2[p2])
            v3[p3++]=v1[p1++];
        else
            v3[p3++]=v2[p2++];    
    }

    while(p1<n)v3[p3++]=v1[p1++];
    while(p2<n)v3[p3++]=v2[p2++]; ;

    for(int i=0;i<n+m;i++){
        printf("%d ",v3[i]);
    }
}

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
    merge(v1,v2,n,m);
    return 0;
}