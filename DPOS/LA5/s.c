#include <stdio.h>
#include <semaphore.h>

int main(){
    sem_t s;
    int v;
    sem_init(&s,0,4);
    sem_wait(&s);
    sem_wait(&s);
    sem_wait(&s);
    sem_post(&s);
    sem_getvalue(&s,&v);
    printf("Value of S: %d",v);
    sem_destroy(&s);
}