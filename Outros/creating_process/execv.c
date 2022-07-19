#include <stdio.h>
#include <unistd.h>

int main(){
    char *cmd[] = {"cat", "/etc/passwd", (char *)0};

    printf("Vou chamar o programa cat para ler o arquivo /etc/passwd:\n");

    // Cria um novo processo e mata o processo pai
    execv("/bin/cat", cmd);

    printf("Mensagem não aparecerá");

    return 0;
}