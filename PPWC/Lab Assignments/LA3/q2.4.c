#include <stdio.h>

void delete_ele_from_array(int arr[], int *n, int pos) {
    for(int i = pos - 1; i < *n - 1; i++) {
        arr[i] = arr[i + 1];
    }
    (*n)--;
}

int main() {
    int n, pos;

    printf("Enter the size of the array: ");
    scanf("%d", &n);

    int arr[n];
    printf("Enter the numbers: ");
    for(int x = 0; x < n; x++) {
        scanf("%d", &arr[x]);
    }

    printf("\nArray is: ");
    for(int x = 0; x < n; x++) {
        printf("%d ", arr[x]);
    }

    printf("\nEnter the pos (1-based): ");
    scanf("%d", &pos);

    if(pos < 1 || pos > n) {
        printf("Invalid Input!!\n");
    } else {
        delete_ele_from_array(arr, &n, pos);

        printf("Array after deletion: ");
        for(int x = 0; x < n; x++) {
            printf("%d ", arr[x]);
        }
        printf("\n");
    }

    return 0;
}
