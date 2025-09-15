#include <stdio.h>

int main(){
    int p,r,t;
    printf("Enter Rate of interest , Principal, Time(in years): ");
    scanf("%d %d %d", &p, &r, &t);
    float SI = (p*r*t)/100;
    printf("Simple Interest: %f", SI);
    return 0;
}