#include <stdio.h>
#include <math.h>

int main(){
    int x;
    printf("Enter a number: ");
    scanf("%d", &x);

    float powers = pow(x,1.0) + pow(x,2.0) + pow(x,3.0);
    printf("Sum of first 3 powers: %f\n",powers);
    return 0;
}