#include <stdio.h>

void diff(int v1[], int n, int v2[], int m) {
    for (int i = 0; i < n; i++) {
        int flag = 1;
        for (int j = 0; j < m; j++) {
            if (v1[i] == v2[j]) {
                flag = 0;
                break;
            }
        }
        if (flag) {
            printf("%d ", v1[i]);
        }
    }
    printf("\n");
}

int main() {
    int n;
    scanf("%d", &n);
    int v1[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &v1[i]);
    }

    int m;
    scanf("%d", &m);
    int v2[m];
    for (int i = 0; i < m; i++) {
        scanf("%d", &v2[i]);
    }

    diff(v1, n, v2, m);
    diff(v2, m, v1, n);

    return 0;
}
