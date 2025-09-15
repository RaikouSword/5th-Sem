#include <stdio.h>

int main(){
    int base;
    int height;
    printf("Enter the base and height of the triangle: ");
    scanf("%d %d", &base, &height);
    float area = 0.5*base*height;
    printf("Area of the traingle: %f", area);
    return 0;
}