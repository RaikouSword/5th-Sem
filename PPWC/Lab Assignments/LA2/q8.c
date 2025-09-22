#include <stdio.h>

int gcd(int a, int b){
    if(b==0) return a;
    return gcd(b,a%b);
}

int main(){
    int a,b;
    printf("Enter two numbers: ");
    scanf("%d%d", &a, &b);
    int ans = gcd(a, b);
    printf("GCD is: %d\n",ans);
    printf("LCM is: %d", (a*b)/ans);
    return 0;
}