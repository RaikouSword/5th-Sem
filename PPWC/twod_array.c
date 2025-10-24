#include <stdio.h>

int main(){
    int x =100;
    int *p;
    p = &x;
    // &x-->address of x
    // x-->value of x
    // p-->address of x 
    // *p--> value of x 
    int **q = &p;
    //q-->address of p
    //*q-->&x
    //**q-->value of x
    int r,c;
    int arr[r][c] = {{1,2,3},{4,5,6}};

    return 0;
}