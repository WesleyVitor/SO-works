#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include "escalonador.fifo.h"

int n;

/**
 * Insere processo no final da fila passada
 */
BCP *anexa_fila (BCP *processo, BCP *fila)
{
        BCP *aux;
        BCP *ant;
        processo -> prox = NULL;
        if (fila == NULL)
        {
                fila = processo;
                return fila;
        }
        

        for (aux = fila; aux->prox != NULL; aux = aux->prox);
        aux->prox = processo;
        return fila;
}

/**
 * Inicializa os campos de um processo
 *
 * Principais pontos a analisar:
 *
 * - Define a faixa dele (se � CPU ou I/O Bound); e
 * - Define o tempo que o processo precisar� para finalizar sua tarefa
 *   (tempo_restante).
 */
void cria_processo (BCP *processo)
{       
        static int id = 0; 
        processo->pid = id; /* pid do processo */
        processo->faixa = 2.0 * (double) random() / (double) RAND_MAX; /* faixa do processo */
        if (processo->faixa < 1)
                sprintf(processo->tipo, "I/O Bound");
        else
                sprintf(processo->tipo, "CPU Bound");
        processo->num_fila1 = 0; 
        processo->num_fila2 = 0;
        processo->num_bloqueado = 0;
        processo->tempo_restante = (100 * (double) random() / (double) RAND_MAX);
        processo->tempo_espera = 0;
        processo->inicio.tv_sec = processo->inicio.tv_usec = 0;
        processo->fim.tv_sec = processo->fim.tv_usec = 0;
        processo->prox = NULL;  
         
        id++; /* Incrementa o PID para ser atribuido ao proximo processo */
        return;
}

/**
 * Mata um processo, apagando ele da mem�ria
 */
void destroi_processo (BCP *processo)
{
        free (processo);
        return;
}

/**
 * Imprime na tela as estat�sticas de um processo.
 *
 * � usado tanto quando um processo � finalizado, quanto no final de toda a
 * simula��o, exibindo um sum�rio, onde � exibido o tempo m�dio de espera.
 */
void estatisticas (BCP *processo, int imprime_sumario)
{
        static int numero_processos = 0;
        static int num_cpu=0;
        static int num_io=0;
        static double tempo_total=0;
        static double tempo_cpu=0;
        static double tempo_io=0;
        if(!imprime_sumario)
        {
                printf ("\nID do processo: %d\n", processo->pid);
                printf ("Tipo de processo: %s (faixa = %.3f)\n", processo->tipo, processo->faixa);
                printf ("Passagens pela fila 1:                  %d\n", processo->num_fila1);
                printf ("Passagens pela fila 2:                  %d\n", processo->num_fila2);
                printf ("Numero de vezes que foi bloqueado:      %d\n", processo->num_bloqueado);
                printf ("Tempo de espera:                    %f s\n", processo->tempo_espera);
                printf ("______________________________________________\n");
                numero_processos++;
                if (processo->faixa < 1)
                {
                        tempo_io += processo->tempo_espera;
                        num_io++;
                }
                else
                {
                        tempo_cpu += processo->tempo_espera;
                        num_cpu++;
                }
                tempo_total += processo->tempo_espera;
                return;
        }
        else
        {
                printf ("\nSumario: \n\n");
                printf ("Total de processos: %d\n",numero_processos);
                printf ("Total de processos CPU Bound: %d\n",num_cpu);
                printf ("Total de processos I/O Bound: %d\n\n",num_io);
                printf ("Tempo medio de espera: %f s\n",(double)tempo_total/numero_processos);
                if(num_cpu)
                        printf ("Tempo medio de espera de processos CPU Bound: %f s\n",(double)tempo_cpu/num_cpu);
                if(num_io)
                        printf ("Tempo medio de espera de processos I/O Bound: %f s\n",(double)tempo_io/num_io);
                printf ("\n");
                return;
        }
}

/**
 * Simula a ocorr�ncia de uma interrup��o para um processo que est� bloqueado.
 *
 * Essencial para que o processo saia do estado bloqueado e volte � fila de
 * aptos.
 */
int interrupcao (BCP *bloqueados)
{
        int randomico;
        if (bloqueados == NULL)
                return 0;
        randomico = (int) (9.0 * (double) random() / (double) RAND_MAX);
        if (randomico >= 5)
                return 1;
        else
                return 0;
}

/**
 * Calcula o tempo em que o processo estava aguardando para ser processado. 
 *
 * Efetua a subtra��o do tempo final pelo tempo inicial da contagem de espera.
 */
BCP *inicializa_tempo (BCP *processo)
{
        if((processo->inicio.tv_sec != 0) && (processo->inicio.tv_usec != 0))
        {
                gettimeofday (&(processo->fim), NULL);
                processo->tempo_espera += (double)(processo->fim.tv_sec + processo->fim.tv_usec*1.e-6) -
                                          (processo->inicio.tv_sec + processo->inicio.tv_usec*1.e-6);
        }
        return processo;
}

/**
 * Gera um tempo aleat�rio para simular o tempo em que um processo passar� na CPU.
 *
 * Essencial para simular os eventos que o processo poder� ter durante sua
 * execu��o, como para saber se ele continuar� em execu��o ou se necessitar�
 * bloquear por uma entrada e sa�da (E/S).
 *
 * Ponto a analisar:
 *  - Processos CPU Bound t�m uma maior probabilidade de continuar executando,
 *  pois gerar� um tempo de processador maior que QUANTUM;
 *  - Processos I/O Bound t�m uma maior probabilidade de gerar um tempo
 *  aleat�rio menor que o QUANTUM, o que o levaria a mais eventos de E/S.
 *
 * Esta probabilidade � dada pela utiliza��o da "faixa" de cada processo
 * (I/O ou CPU Bound) na gera��o do tempo.
 */
double gera_tempo (BCP *processo)
{
        double tempo_processador;
        tempo_processador = PI + (PI/2) + QUANTUM * processo->faixa * (double)random()/(double)RAND_MAX;
        
        /*
         * A inclusao das constantes no valor calculado acima pode ser
         * entendido como que constantes empiricas para otimizacao do
         * fator de uso de processador a cada vez que o processo e
         * escalonado.
         */
        
        return tempo_processador;
}

/**
 * Modifica��o 1: Inicia a contagem do tempo de espera mesmo quando o processo
 * entra na fila1.
 *
 * Essencial para os algoritmos que possuem apenas uma fila (FIFO, SJF, RR).
 */
BCP * conta_espera(BCP *fila1)
{
    BCP * p = NULL;
    for (p = fila1; p != NULL; p = p->prox)
        gettimeofday (&(p->inicio), NULL);

    return fila1;
}

/**
 * Fun��o que efetua o algoritmo de escalonamento dos processos.
 *
 * Principal ponto de modifica��o para a cria��o dos demais algoritmos
 * solicitados.
 */
void escalona (BCP *fila1, BCP *bloqueados)
{
        /**
         * Ponteiro que vai apontar para o processo que estar� em execu��o.
         *
         * � importante observar que este ponteiro simula o processo que est�
         * no estado "executando", onde s� pode haver um processo por vez.
         */
        BCP *processo = NULL;

        // Vari�veis de controle para os la�os
        int executa = 1, i;

        // Armazenar� o valor gerado para simular o tempo que o processo
        // passar� processando.
        double tempo_processador;

        // Modifica��o 2: Inicia a contagem do tempo de espera j� quando os
        // processos est�o na fila1
        fila1 = conta_espera(fila1);

        // Executar� o programa enquanto ainda houver processos necessitando
        // ser processador, quando seu tempo_restante for maior que 0
        while (executa)
        {
                // Processa os processos da fila1.
                //
                // Pontos a analisar:
                //
                // 1 - Executar� enquanto houver processos nesta fila;
                // 2 - Sempre executar� os processos da fila1 antes da fila2, dando prioridade � fila1.
                while (fila1 != NULL)
                {
                        // Busca se h� algum processo na fila de bloqueados,
                        // e se houve a interrup��o necess�ria para tornar o
                        // processo apto novamente.
                        //
                        // Ponto a analisar:
                        // 1 - Este teste � feito a cada vez que o la�o
                        // inicia, mas o processo que estava bloqueado �
                        // inserido no final da fila de aptos (fila1);
                        // 2 - A interrup��o � simulada por meio da gera��o de
                        // um valor aleat�rio.
                        if ((bloqueados != NULL))
                        {
                                // Pega o primeiro processo da fila de
                                // bloqueados
                                processo = bloqueados;
                                // Anda a fila de bloqueados
                                bloqueados = processo->prox;
                                // Inicia a contagem do tempo de espera em que
                                // o processo entre na fila, at� que seja processado.
                                gettimeofday(&(processo -> inicio), NULL);
                                // Incrementa a quantidade de vezes que o
                                // processo entrou na fila1
                                processo->num_fila1++;
                                // Insere o processo no final da fila1
                                fila1 = anexa_fila (processo, fila1);
                        }

                        /** Inicio da simula��o de execu��o do processo **/
                        
                        // Pega primeiro processo da fila1, simula colocar o
                        // processo no estado executando
                        processo = fila1;
                        
                        // Retira o processo da fila1, anda a fila
                        fila1 = processo -> prox;
                        
                        // Contabiliza o tempo esperado pelo processo, desde
                        // que entrou na fila at� agora, quando inicia seu
                        // estado de execu��o.
                        processo=inicializa_tempo(processo);
                        
                        
                        // Simula quanto tempo o processo ir� passar
                        // executando no processador.
                        //
                        // Este valor definir� o que ocorrer� com o processo.
                        // tempo_processador = gera_tempo(processo);

                         estatisticas(processo, SEMSUMARIO);
                         destroi_processo(processo);

                }

                // Verifica as condi��es para finaliza��o do escalonador
                //
                // Se n�o houver nenhum processo nas filas 1 e 2
                if ((fila1 == NULL))
                {
                        // E se tamb�m n�o houver nenhum processo na fila de
                        // bloqueados,
                        if (bloqueados == NULL)
                                // Todos os processos foram finalizados,
                                // devendo o escalonador ser finalizado
                                // tamb�m, setando esta vari�vel para
                                // finalizar a execu��o do la�o maior.
                                executa = 0;
                        // Caso ainda haja processos bloqueados, retir�-los
                        // para a fila de aptos (fila1).
                        else
                        {
                                processo = bloqueados;
                                bloqueados = processo->prox;
                                gettimeofday(&(processo -> inicio), NULL);
                                processo->num_fila1++;
                                fila1 = anexa_fila (processo, fila1);   
                        }
                }
        }

        return;
}

/**
 * Fun��o principal do programa.
 *
 * Realiza a chamada para a execu��o das demais fun��es.
 */
int main(int argc, char **argv)
{
        // Vari�vel de controle, para o for
        int i;
        // Estruturas que armazenar�o o inicio e fim da simula��o
        struct timeval comeco, fim;

        // Estrutura para manipular um processo
        BCP *processo;

        // Ponteiro para o in�nio da fila 1
        BCP *fila1 = NULL;
        
        // Ponteiro para o in�nio da fila 2
        BCP *fila2 = NULL;
        
        // Ponteiro para o in�nio da fila de bloqueados
        BCP *bloqueados = NULL;
                
        // S� permite o programa executar se seu uso for correto
        if (argc != 2)
        {
                printf("\nUso: ./escalonador [numero de processos]\n");
                printf("Uso recomendado: ./escalonador [numero de processos] | less\n\n");
                exit (1);
        }
        
        // Obtem o n�mero de processos informados na linha de comando
        n = atoi(argv[1]);      /* Numero de processos que serao executados */

        if(n<=0)
        {
                printf("\nPor favor entre com um valor coerente...\n\n");
                exit(1);
        }
        
        srand (time(NULL));     /* Gera uma nova semente de numeros aleatorios */
        
        /**
         * La�o para criar os n processos solicitados:
         */
        for (i = 0; i < n; i++)
        {
                // 1 - Cria o processo, alocando mem�ria para sua estrutura
                processo = (BCP *) malloc (sizeof (BCP));
                // 2 - Preenche os dados iniciais do processo
                cria_processo (processo);
                // 3 - Insere o processo no final da fila1
                fila1 = anexa_fila (processo, fila1);
                
                // 4 - Incrementa a quantidade de vezes que o processo entrou na fila1, neste caso 1 vez.
                processo->num_fila1++;
        }
        
        /* Contagem do tempo de simulacao */
        gettimeofday(&comeco, NULL);
        
        /* Inicializacao da simulacao */;
        escalona (fila1, bloqueados);

        /* Fim da contagem */
        gettimeofday(&fim, NULL);

        // Imprime na tela um sum�rio de toda a simula��o realizada
        estatisticas(NULL, COMSUMARIO);

        printf("Tempo total de simulacao: %f s\n\n",(double)(fim.tv_sec + fim.tv_usec*1.e-6) -
        (comeco.tv_sec + comeco.tv_usec*1.e-6));
                
        return 0;
}
