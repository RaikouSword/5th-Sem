#include<stdio.h>

void insert_ele_in_sorted_array(int v[],int n,int x){
    int pos= n-1;
    for (int i=0;i<n;i++){
        if(x<=v[i]){
            pos = i;
            break;
        }
    }

    if(pos==n-1){
        n++;
        v[n-1]=x;
    }else{
        for(int i=n-1;i>=pos;i--){
        v[i+1] = v[i];
        }
        v[pos]=x;
        n++;
    }
}

int main(){
    int n;
    scanf("%d",&n);
    int v[n];
    for(int i=0;i<n;i++){
        scanf("%d",&v[i]);
    }

    int x;
    scanf("%d",&x);
    insert_ele_in_sorted_array(v,n,x);
    for(int i=0;i<n;i++){
        printf("%d ",v[i]);
    }
    
    return 0;
}