#include <stdio.h>
#include <unistd.h>

int main(){

    printf("\nEu Sou o processo %d.\n", getpid());
    printf("Eu,%d, sou o pai dele!\n ", getppid());
    sleep(30);
    return 0;
}