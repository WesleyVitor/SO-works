#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(){

    printf("Vou chamar o programa cat para ler o arquivo /etc/issue:\n");

    // Criar um processo 
    // Dá um wait no processo pai
    // Retornar ao processo api quando o filho terminar
    system("/bin/cat /etc/issue");

    sleep(5);
    printf("Essa mensagem foi mostrada!\n");


    return 0;
}