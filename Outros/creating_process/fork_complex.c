#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include<sys/wait.h>

int value = 10;
int main(){

    int pid;
    pid = fork();

    if(pid==0){
        value +=15;
        printf("Value no filho:%d\n", value);
        return 0;
    }else{
        value +=5;
        printf("Value no pai:%d\n", value);
    }
    // O contexto é compartilhado, mas depois cada processo é independente
    return 0;
}