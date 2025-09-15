#include <stdio.h>

int main(){
    int m1,m2,m3,m4,m5;
    printf("Enter the marks for 5 subjects: ");
    scanf("%d %d %d %d %d", &m1,&m2, &m3, &m4, &m5);
    double avg = (m1+m2+m3+m4+m5)/5.0;
    printf("Percentage of marks: %lf", avg);
    return 0;
}