#include <stdio.h>
#define PI 3.141593

int main(){
    int rad;
    printf("Enter the radius of the circle: ");
    scanf("%d", &rad);
    float area = PI * rad * rad;
    float circumference = 2*PI*rad;
    printf("Area of circle: %f\nCircumference of circle: %f", area, circumference);
    return 0;
}