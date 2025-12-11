//create a athread to increment a global variable and display its value
#include<pthread.h>
#include<stdio.h>
#include <semaphore.h>

int g,h;
sem_t s;
void * tfun(void *){
    sem_wait(&s);
    g = 0;
    while(g<10){
        g++;
        printf("Thread Prints g=A\n");
    }
    // for(int i = 1 ; i <= g ; i++){
    //     printf("%d\n",i);
    // }
    sem_post(&s);
    pthread_exit(0);
}
void * tfun1(void *){
    sem_wait(&s);
    h = 0;
    while(h<10){
        h++;
        printf("Thread Prints g=B\n");
    }
    // for(int i = 1 ; i <= g ; i++){
    //     printf("%d\n",i);
    // }
    sem_post(&s);
    pthread_exit(0);
}

int main(){
    pthread_t tid1;
    pthread_t tid2;
    sem_init(&s,0,1);
    pthread_create(&tid1,NULL,tfun,NULL);
    pthread_join(tid1,NULL);
  
    pthread_create(&tid2,NULL,tfun1,NULL);
    pthread_join(tid2,NULL);
    sem_destroy(&s);
    return 0;
}