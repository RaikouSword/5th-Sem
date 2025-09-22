#include <stdio.h>
#include <math.h>

int main(){
    int a, b,c;
    printf("Enter coefficient(a,b,c) of quadratic eq: ");
    scanf("%d%d%d",&a,&b,&c);
    double root1 = (-b + (sqrt(b*b-4*a*c)))/2*a;
    double root2 = (-b - (sqrt(b*b-4*a*c)))/2*a;
    printf("%d and %d are roots of the quad eq",(int)(root1),(int)(root2));
    return 0;
}