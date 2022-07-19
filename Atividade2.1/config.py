import os
def run_config():
    

    """
    Rodando os algoritmos de escalonamentos
    """
    os.system("cd escalonador_prio && gcc -o escalonador escalonador.prio.c")
    os.system("cd escalonador_fifo && gcc -o escalonador escalonador.fifo.c")
    os.system("cd escalonador_rr && gcc -o escalonador escalonador.rr.c")
    os.system("cd escalonador_sjf && gcc -o escalonador escalonador.sjf.c")


    """
    Pegando a média dos tempos de espera para cada algoritmo
    """
    os.system("cd escalonador_prio && ./executar.sh")
    os.system("cd escalonador_fifo && ./executar.sh")
    os.system("cd escalonador_rr && ./executar.sh")
    os.system("cd escalonador_sjf && ./executar.sh")

def rm_files():
    """
    Apagando o arquivo de resultado e escalonador
    """
    os.system("cd escalonador_prio && rm TME50.txt && rm escalonador")
    os.system("cd escalonador_prio && rm TMECPUBound50.txt")
    os.system("cd escalonador_prio && rm TMEIOBound50.txt")

    os.system("cd escalonador_prio && rm TME100.txt")
    os.system("cd escalonador_prio && rm TMECPUBound100.txt")
    os.system("cd escalonador_prio && rm TMEIOBound100.txt")

    os.system("cd escalonador_prio && rm TME150.txt")
    os.system("cd escalonador_prio && rm TMECPUBound150.txt")
    os.system("cd escalonador_prio && rm TMEIOBound150.txt")

    os.system("cd escalonador_prio && rm TME200.txt")
    os.system("cd escalonador_prio && rm TMECPUBound200.txt")
    os.system("cd escalonador_prio && rm TMEIOBound200.txt")

    os.system("cd escalonador_prio && rm TME250.txt")
    os.system("cd escalonador_prio && rm TMECPUBound250.txt")
    os.system("cd escalonador_prio && rm TMEIOBound250.txt")

    os.system("cd escalonador_prio && rm TMEGeral50.txt")
    os.system("cd escalonador_prio && rm TMEGeral100.txt")
    os.system("cd escalonador_prio && rm TMEGeral150.txt")
    os.system("cd escalonador_prio && rm TMEGeral200.txt")
    os.system("cd escalonador_prio && rm TMEGeral250.txt")

    os.system("cd escalonador_fifo && rm TME50.txt && rm escalonador")
    os.system("cd escalonador_fifo && rm TMECPUBound50.txt")
    os.system("cd escalonador_fifo && rm TMEIOBound50.txt")

    os.system("cd escalonador_fifo && rm TME100.txt")
    os.system("cd escalonador_fifo && rm TMECPUBound100.txt")
    os.system("cd escalonador_fifo && rm TMEIOBound100.txt")

    os.system("cd escalonador_fifo && rm TME150.txt")
    os.system("cd escalonador_fifo && rm TMECPUBound150.txt")
    os.system("cd escalonador_fifo && rm TMEIOBound150.txt")

    os.system("cd escalonador_fifo && rm TME200.txt")
    os.system("cd escalonador_fifo && rm TMECPUBound200.txt")
    os.system("cd escalonador_fifo && rm TMEIOBound200.txt")

    os.system("cd escalonador_fifo && rm TME250.txt")
    os.system("cd escalonador_fifo && rm TMECPUBound250.txt")
    os.system("cd escalonador_fifo && rm TMEIOBound250.txt")

    os.system("cd escalonador_fifo && rm TMEGeral50.txt")
    os.system("cd escalonador_fifo && rm TMEGeral100.txt")
    os.system("cd escalonador_fifo && rm TMEGeral150.txt")
    os.system("cd escalonador_fifo && rm TMEGeral200.txt")
    os.system("cd escalonador_fifo && rm TMEGeral250.txt")


    os.system("cd escalonador_rr && rm TME50.txt && rm escalonador")
    os.system("cd escalonador_rr && rm TMECPUBound50.txt")
    os.system("cd escalonador_rr && rm TMEIOBound50.txt")

    os.system("cd escalonador_rr && rm TME100.txt")
    os.system("cd escalonador_rr && rm TMECPUBound100.txt")
    os.system("cd escalonador_rr && rm TMEIOBound100.txt")

    os.system("cd escalonador_rr && rm TME150.txt")
    os.system("cd escalonador_rr && rm TMECPUBound150.txt")
    os.system("cd escalonador_rr && rm TMEIOBound150.txt")

    os.system("cd escalonador_rr && rm TME200.txt")
    os.system("cd escalonador_rr && rm TMECPUBound200.txt")
    os.system("cd escalonador_rr && rm TMEIOBound200.txt")

    os.system("cd escalonador_rr && rm TME250.txt")
    os.system("cd escalonador_rr && rm TMECPUBound250.txt")
    os.system("cd escalonador_rr && rm TMEIOBound250.txt")

    os.system("cd escalonador_rr && rm TMEGeral50.txt")
    os.system("cd escalonador_rr && rm TMEGeral100.txt")
    os.system("cd escalonador_rr && rm TMEGeral150.txt")
    os.system("cd escalonador_rr && rm TMEGeral200.txt")
    os.system("cd escalonador_rr && rm TMEGeral250.txt")


    os.system("cd escalonador_sjf && rm TME50.txt && rm escalonador")
    os.system("cd escalonador_sjf && rm TMECPUBound50.txt")
    os.system("cd escalonador_sjf && rm TMEIOBound50.txt")

    os.system("cd escalonador_sjf && rm TME100.txt")
    os.system("cd escalonador_sjf && rm TMECPUBound100.txt")
    os.system("cd escalonador_sjf && rm TMEIOBound100.txt")

    os.system("cd escalonador_sjf && rm TME150.txt")
    os.system("cd escalonador_sjf && rm TMECPUBound150.txt")
    os.system("cd escalonador_sjf && rm TMEIOBound150.txt")

    os.system("cd escalonador_sjf && rm TME200.txt")
    os.system("cd escalonador_sjf && rm TMECPUBound200.txt")
    os.system("cd escalonador_sjf && rm TMEIOBound200.txt")

    os.system("cd escalonador_sjf && rm TME250.txt")
    os.system("cd escalonador_sjf && rm TMECPUBound250.txt")
    os.system("cd escalonador_sjf && rm TMEIOBound250.txt")
    
    os.system("cd escalonador_sjf && rm TMEGeral50.txt")
    os.system("cd escalonador_sjf && rm TMEGeral100.txt")
    os.system("cd escalonador_sjf && rm TMEGeral150.txt")
    os.system("cd escalonador_sjf && rm TMEGeral200.txt")
    os.system("cd escalonador_sjf && rm TMEGeral250.txt")
