#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void * processoLevel1(){

    int i;
    for(i=1; i< 1000;i++){
        printf("\t Thread 1 - %d\n", i);
    }

}

void * processoLevel2(){

    int i;
    for(i=1000; i< 2000;i++){
        printf("\t\t Thread 2 - %d\n", i);
    }
}

void * processoLevel3(){

    int i;
    for(i=2000; i< 3000;i++){
        printf("\t\t Thread 3 - %d\n", i);
    }
}

int main(){

    pthread_t thread1, thread2, thread3;
    pthread_create(&thread1, NULL, processoLevel1, NULL);
    pthread_create(&thread2, NULL   , processoLevel2, NULL);
    pthread_create(&thread3, NULL, processoLevel3, NULL);
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    pthread_join(thread3, NULL);
    printf("FIM\n");
}

