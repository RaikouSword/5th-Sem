#include <stdio.h>
#include <unistd.h>

int main(){
    pid_t childpid;
    fork()+fork();
    printf("My PID: %ld, Parent PID: %ld\n", (long)getpid(),(long)getpid());
    getchar();
    return 0;
}