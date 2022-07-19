#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

long conta = 0;
int flag[] = {0,0};
int turn = 2;

void * t2(){
    long i;
    for(i=0; i < 1000000; i++){
        flag[0] = 1;
        turn = 3;
        while(flag[1] && turn==3);
        conta = conta + 5;
        flag[0] = 0;
    }

    printf("Encerrei t1\n");
}

void * t3(){
    long i;
    for(i=0; i < 1000000; i++){
        flag[1]=1;
        turn=2;
        while(flag[0] && turn==2);
        conta = conta + 2;
        flag[1]=0;
    }

    printf("Encerrei t2\n");
}


int main(){
    pthread_t tid2, tid3;
    pthread_create(&tid2, NULL, &t2, NULL);
    pthread_create(&tid3, NULL, &t3, NULL);

    pthread_join(tid2, NULL);
    pthread_join(tid3, NULL);

    printf("O valor da variável conta é: %ld\n", conta);
    return 0;
}