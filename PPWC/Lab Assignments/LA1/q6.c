#include <stdio.h>

int main(){
    //Fahrenheit to Celsius
    double temp_f;
    printf("Enter Temperature in Fahrenheit: ");
    scanf("%lf", &temp_f);
    double res_c =  5.0*(temp_f-32)/9;
    printf("Converted Temperature in Celsius: %lf", res_c);

    //Celsius to Fahrenheit
    double temp_c;
    printf("\nEnter Temperature in Celsius: ");
    scanf("%lf", &temp_c);
    double res_f =  (9.0*temp_c+160)/5.0;
    printf("Converted Temperature in Fahrenheit: %lf", res_f);

    return 0;
}

