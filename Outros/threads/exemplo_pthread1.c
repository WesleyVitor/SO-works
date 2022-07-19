#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void * funcao_thread(void* arg){
    printf("Nova thread Criada com o PID %d.\n", getpid());
    sleep(20);
    return NULL;
}

int main(){
    pthread_t thread;
    printf("Processo pesado PID %d.\n", getpid());
    pthread_create(&thread, NULL, &funcao_thread, NULL);
    printf("Indentificador do Thread %ld.\n", thread);
    sleep(20);
    return 0;
}