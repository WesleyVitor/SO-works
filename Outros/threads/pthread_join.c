#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void * minha_thread(void* arg){
    printf("\t\ Iniciando a thread.\n", arg);
    printf("\t\ Recebi o argumento %p do processo pesado\n",arg);
    sleep(10);
}

int main(){
    int retcode;
    pthread_t thread_a, thread_b;
    void * retval;
    printf("Criando a primeira thread.\n");
    retcode = pthread_create(&thread_a, NULL, &minha_thread, "a");
    if(retcode != 0){
        printf("A thread não foi criada. Erro %d\n", retcode);
    }
    sleep(1);
    printf("Criando a segimda thread.\n");
    retcode = pthread_create(&thread_b, NULL, &minha_thread, "b");
    if(retcode != 0){
        printf("A thread não foi criada. Erro %d\n", retcode);
    }
    sleep(1);
    printf("Esperando pelo término da primeira thread.\n");
    retcode = pthread_join(thread_a, &retval);
    printf("A primeira thread terminou.\n");
    printf("Esperando a segunda thread terminad.\n");
    retcode = pthread_join(thread_b, &retval);
    printf("Ambas as threads terminaram.\n");
    return 0;
    
}