#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

sem_t s1, s2;
void* pA(void* ){
    for(int i = 0; i < 10; i++){
        sem_wait(&s1);          
        printf("A\n");
        sem_post(&s2);            
    }
    pthread_exit(0);
}
void* pB(void* ){
    for(int i = 0; i < 10; i++){
        sem_wait(&s2);            
        printf("B\n");
        sem_post(&s1);            
    }
    pthread_exit(0);
}

int main() {
    pthread_t t1, t2;
    sem_init(&s1, 0, 1);  
    sem_init(&s2, 0, 0);  
    pthread_create(&t1, NULL, pA, NULL);
    pthread_create(&t2, NULL, pB, NULL);
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    sem_destroy(&s1);
    sem_destroy(&s2);

    return 0;
}
