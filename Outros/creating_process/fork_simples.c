#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include<sys/wait.h>
int main(){

    int id;

    id = fork();
    if(id==0){
        printf("Eu sou o processo filho %d\n", getpid());
        sleep(30);
        printf("Já Esperei vou embora...\n");

    }else{
        printf("Eu sou o processo pai %d e tenho o filho %d\n",getpid(), id);
        wait(NULL);
        printf("Meu Filho terminou!\n");
    }

    return 0 ;
}