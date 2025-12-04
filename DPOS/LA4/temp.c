#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <math.h>

// Fibonacci function
void fibo(int *ptr, int n) {
    int a = 0, b = 1;
    *ptr = a;
    ptr++;
    *ptr = b;
    ptr++;
    n -= 2;
    while (n--) {
        int c = a + b;
        *ptr = c;
        ptr++;
        a = b;
        b = c;
    }
}

// Prime number check
int isPrime(int num) {
    if (num <= 1) return 0; // 0 and 1 are not prime
    for (int x = 2; x <= sqrt(num); x++) { // Only check up to sqrt(num)
        if (num % x == 0) return 0; // Not prime if divisible by any number
    }
    return 1; // Prime if no divisors found
}

int main() {
    int n;
    printf("Enter length of Fibonacci sequence: ");
    scanf("%d", &n);

    int arr[n];
    
    if (vfork() == 0) { // Child process
        fibo(arr, n);
        _exit(0); // Exit child process after Fibonacci computation
    } else { // Parent process
        wait(NULL); // Wait for the child process to finish
        printf("Fibonacci sequence: ");
        for (int x = 0; x < n; x++) {
            printf("%d ", arr[x]);
        }
        printf("\n");

        printf("Prime numbers in the sequence:\n");
        for (int x = 0; x < n; x++) {
            if (isPrime(arr[x])) {
                printf("Element: %d at Index: %d\n", arr[x], x);
            }
        }
    }

    return 0;
}
