import matplotlib.pyplot as plt

from config import run_config, rm_files
run_config()


def media_dos_tempos_medios(file:str)->float:
    soma=0
    with open(file, "r") as file:
        for readline in file: 
            line_strip = readline.strip()
            soma += float(line_strip)

    result = soma/10
    return result

def variancia_dos_tempos_medios(file:str, media:float)->float:
    soma=0
    count=0
    with open(file, "r") as file:
        for readline in file: 
            count+=1
            line_strip = readline.strip()
            soma = soma + (float(line_strip) - media) ** 2

    result = soma/count
    return result
"""
Média do Round Robin
"""

media_rr_50_p = media_dos_tempos_medios("escalonador_rr/TME50.txt")
media_rr_50_cpu_bound = media_dos_tempos_medios("escalonador_rr/TMECPUBound50.txt")
media_rr_50_IO_bound = media_dos_tempos_medios("escalonador_rr/TMEIOBound50.txt")

media_rr_100_p = media_dos_tempos_medios("escalonador_rr/TME100.txt")
media_rr_100_cpu_bound = media_dos_tempos_medios("escalonador_rr/TMECPUBound100.txt")
media_rr_100_IO_bound = media_dos_tempos_medios("escalonador_rr/TMEIOBound100.txt")

media_rr_150_p = media_dos_tempos_medios("escalonador_rr/TME150.txt")
media_rr_150_cpu_bound = media_dos_tempos_medios("escalonador_rr/TMECPUBound150.txt")
media_rr_150_IO_bound = media_dos_tempos_medios("escalonador_rr/TMEIOBound150.txt")

media_rr_200_p = media_dos_tempos_medios("escalonador_rr/TME200.txt")
media_rr_200_cpu_bound = media_dos_tempos_medios("escalonador_rr/TMECPUBound200.txt")
media_rr_200_IO_bound = media_dos_tempos_medios("escalonador_rr/TMEIOBound200.txt")

media_rr_250_p = media_dos_tempos_medios("escalonador_rr/TME250.txt")
media_rr_250_cpu_bound = media_dos_tempos_medios("escalonador_rr/TMECPUBound250.txt")
media_rr_250_IO_bound = media_dos_tempos_medios("escalonador_rr/TMEIOBound250.txt")


arrayRR = [media_rr_50_p, media_rr_100_p, media_rr_150_p, media_rr_200_p, media_rr_250_p]
arrayRRCPUBound = [media_rr_50_cpu_bound, media_rr_100_cpu_bound, media_rr_150_cpu_bound, media_rr_200_cpu_bound, media_rr_250_cpu_bound]
arrayRRIOBound = [media_rr_50_IO_bound, media_rr_100_IO_bound, media_rr_150_IO_bound, media_rr_200_IO_bound, media_rr_250_IO_bound]

"""
Variância do Round Robin
"""
variancia_rr_50_p=variancia_dos_tempos_medios("escalonador_rr/TME50.txt", media_rr_50_p)
variancia_rr_100_p=variancia_dos_tempos_medios("escalonador_rr/TME100.txt", media_rr_100_p)
variancia_rr_150_p=variancia_dos_tempos_medios("escalonador_rr/TME150.txt", media_rr_150_p)
variancia_rr_200_p=variancia_dos_tempos_medios("escalonador_rr/TME200.txt", media_rr_200_p)
variancia_rr_250_p=variancia_dos_tempos_medios("escalonador_rr/TME250.txt", media_rr_250_p)


"""
Média do de Prioridades
"""
media_prio_50_p = media_dos_tempos_medios("escalonador_prio/TME50.txt")
media_prio_50_cpu_bound = media_dos_tempos_medios("escalonador_prio/TMECPUBound50.txt")
media_prio_50_IO_bound = media_dos_tempos_medios("escalonador_prio/TMEIOBound50.txt")

media_prio_100_p = media_dos_tempos_medios("escalonador_prio/TME100.txt")
media_prio_100_cpu_bound = media_dos_tempos_medios("escalonador_prio/TMECPUBound100.txt")
media_prio_100_IO_bound = media_dos_tempos_medios("escalonador_prio/TMEIOBound100.txt")

media_prio_150_p = media_dos_tempos_medios("escalonador_prio/TME150.txt")
media_prio_150_cpu_bound = media_dos_tempos_medios("escalonador_prio/TMECPUBound150.txt")
media_prio_150_IO_bound = media_dos_tempos_medios("escalonador_prio/TMEIOBound150.txt")

media_prio_200_p = media_dos_tempos_medios("escalonador_prio/TME200.txt")
media_prio_200_cpu_bound = media_dos_tempos_medios("escalonador_prio/TMECPUBound200.txt")
media_prio_200_IO_bound = media_dos_tempos_medios("escalonador_prio/TMEIOBound200.txt")

media_prio_250_p = media_dos_tempos_medios("escalonador_prio/TME250.txt")
media_prio_250_cpu_bound = media_dos_tempos_medios("escalonador_prio/TMECPUBound250.txt")
media_prio_250_IO_bound = media_dos_tempos_medios("escalonador_prio/TMEIOBound250.txt")

arrayPRIO = [media_prio_50_p, media_prio_100_p, media_prio_150_p, media_prio_200_p, media_prio_250_p]
arrayPRIOCPUBound = [media_prio_50_cpu_bound, media_prio_100_cpu_bound, media_prio_150_cpu_bound, media_prio_200_cpu_bound, media_prio_250_cpu_bound]
arrayPRIOIOBound = [media_prio_50_IO_bound, media_prio_100_IO_bound, media_prio_150_IO_bound, media_prio_200_IO_bound, media_prio_250_IO_bound]

"""
Variância do Prioridades
"""
variancia_prio_50_p=variancia_dos_tempos_medios("escalonador_prio/TME50.txt", media_prio_50_p)
variancia_prio_100_p=variancia_dos_tempos_medios("escalonador_prio/TME100.txt", media_prio_100_p)
variancia_prio_150_p=variancia_dos_tempos_medios("escalonador_prio/TME150.txt", media_prio_150_p)
variancia_prio_200_p=variancia_dos_tempos_medios("escalonador_prio/TME200.txt", media_prio_200_p)
variancia_prio_250_p=variancia_dos_tempos_medios("escalonador_prio/TME250.txt", media_prio_250_p)

"""
Média do FIFO
"""
media_fifo_50_p = media_dos_tempos_medios("escalonador_fifo/TME50.txt")
media_fifo_50_cpu_bound = media_dos_tempos_medios("escalonador_fifo/TMECPUBound50.txt")
media_fifo_50_IO_bound = media_dos_tempos_medios("escalonador_fifo/TMEIOBound50.txt")

media_fifo_100_p = media_dos_tempos_medios("escalonador_fifo/TME100.txt")
media_fifo_100_cpu_bound = media_dos_tempos_medios("escalonador_fifo/TMECPUBound100.txt")
media_fifo_100_IO_bound = media_dos_tempos_medios("escalonador_fifo/TMEIOBound100.txt")

media_fifo_150_p = media_dos_tempos_medios("escalonador_fifo/TME150.txt")
media_fifo_150_cpu_bound = media_dos_tempos_medios("escalonador_fifo/TMECPUBound150.txt")
media_fifo_150_IO_bound = media_dos_tempos_medios("escalonador_fifo/TMEIOBound150.txt")

media_fifo_200_p = media_dos_tempos_medios("escalonador_fifo/TME200.txt")
media_fifo_200_cpu_bound = media_dos_tempos_medios("escalonador_fifo/TMECPUBound200.txt")
media_fifo_200_IO_bound = media_dos_tempos_medios("escalonador_fifo/TMEIOBound200.txt")

media_fifo_250_p = media_dos_tempos_medios("escalonador_fifo/TME250.txt")
media_fifo_250_cpu_bound = media_dos_tempos_medios("escalonador_fifo/TMECPUBound250.txt")
media_fifo_250_IO_bound = media_dos_tempos_medios("escalonador_fifo/TMEIOBound250.txt")

arrayFIFO = [media_fifo_50_p, media_fifo_100_p, media_fifo_150_p, media_fifo_200_p, media_fifo_250_p]
arrayFIFOCPUBound = [media_fifo_50_cpu_bound, media_fifo_100_cpu_bound, media_fifo_150_cpu_bound, media_fifo_200_cpu_bound, media_fifo_250_cpu_bound]
arrayFIFOIOBound = [media_fifo_50_IO_bound, media_fifo_100_IO_bound, media_fifo_150_IO_bound, media_fifo_200_IO_bound, media_fifo_250_IO_bound]

"""
Variância do FIFO
"""

variancia_fifo_50_p=variancia_dos_tempos_medios("escalonador_fifo/TME50.txt", media_fifo_50_p)
variancia_fifo_100_p=variancia_dos_tempos_medios("escalonador_fifo/TME100.txt", media_fifo_100_p)
variancia_fifo_150_p=variancia_dos_tempos_medios("escalonador_fifo/TME150.txt", media_fifo_150_p)
variancia_fifo_200_p=variancia_dos_tempos_medios("escalonador_fifo/TME200.txt", media_fifo_200_p)
variancia_fifo_250_p=variancia_dos_tempos_medios("escalonador_fifo/TME250.txt", media_fifo_250_p)


"""
Média do SJF
"""
media_sjf_50_p = media_dos_tempos_medios("escalonador_sjf/TME50.txt")
media_sjf_50_cpu_bound = media_dos_tempos_medios("escalonador_sjf/TMECPUBound50.txt")
media_sjf_50_IO_bound = media_dos_tempos_medios("escalonador_sjf/TMEIOBound50.txt")

media_sjf_100_p = media_dos_tempos_medios("escalonador_sjf/TME100.txt")
media_sjf_100_cpu_bound = media_dos_tempos_medios("escalonador_sjf/TMECPUBound100.txt")
media_sjf_100_IO_bound = media_dos_tempos_medios("escalonador_sjf/TMEIOBound100.txt")

media_sjf_150_p = media_dos_tempos_medios("escalonador_sjf/TME150.txt")
media_sjf_150_cpu_bound = media_dos_tempos_medios("escalonador_sjf/TMECPUBound150.txt")
media_sjf_150_IO_bound = media_dos_tempos_medios("escalonador_sjf/TMEIOBound150.txt")

media_sjf_200_p = media_dos_tempos_medios("escalonador_sjf/TME200.txt")
media_sjf_200_cpu_bound = media_dos_tempos_medios("escalonador_sjf/TMECPUBound200.txt")
media_sjf_200_IO_bound = media_dos_tempos_medios("escalonador_sjf/TMEIOBound200.txt")

media_sjf_250_p = media_dos_tempos_medios("escalonador_sjf/TME250.txt")
media_sjf_250_cpu_bound = media_dos_tempos_medios("escalonador_sjf/TMECPUBound250.txt")
media_sjf_250_IO_bound = media_dos_tempos_medios("escalonador_sjf/TMEIOBound250.txt")

arraySJF = [media_sjf_50_p, media_sjf_100_p, media_sjf_150_p, media_sjf_200_p, media_sjf_250_p]
arraySJFCPUBound = [media_sjf_50_cpu_bound, media_sjf_100_cpu_bound, media_sjf_150_cpu_bound, media_sjf_200_cpu_bound, media_sjf_250_cpu_bound]
arraySJFIOBound = [media_sjf_50_IO_bound, media_sjf_100_IO_bound, media_sjf_150_IO_bound, media_sjf_200_IO_bound, media_sjf_250_IO_bound]

"""
Variância do SJF
"""
variancia_sjf_50_p=variancia_dos_tempos_medios("escalonador_sjf/TME50.txt", media_sjf_50_p)
variancia_sjf_100_p=variancia_dos_tempos_medios("escalonador_sjf/TME100.txt", media_sjf_100_p)
variancia_sjf_150_p=variancia_dos_tempos_medios("escalonador_sjf/TME150.txt", media_sjf_150_p)
variancia_sjf_200_p=variancia_dos_tempos_medios("escalonador_sjf/TME200.txt", media_sjf_200_p)
variancia_sjf_250_p=variancia_dos_tempos_medios("escalonador_sjf/TME250.txt", media_sjf_250_p)

"""
    Apagando o arquivo de resultado e escalonador
"""
rm_files()


"""
    Plot do gráfico TEMPO MÉDIO TOTAL
"""
# Using Numpy to create an array X
X = [50, 100, 150, 200, 250]

# Assign variables to the y axis part of the curve
a = arrayFIFO
b = arrayPRIO
c = arrayRR
d = arraySJF


# Plotting both the curves simultaneously
plt.plot(X, a, color='r', label='FIFO')
plt.plot(X, b, color='g', label='PRIO')
plt.plot(X, c, color='b', label='RR')
plt.plot(X, d, color='y', label='SJF')

# Naming the x-axis, y-axis and the whole graph
plt.xlabel("Número de processos")
plt.ylabel("Tempo médio")
plt.title("Gráfico de tempo médio dos escalonadores")

# Adding legend, which helps us recognize the curve according to it's color
plt.legend()

# To load the display window
#plt.show()
plt.savefig('TME.png')
plt.close()

"""
    Plot do gráfico TEMPO MÉDIO CPU Bound
"""
# Using Numpy to create an array X
X = [50, 100, 150, 200, 250]

# Assign variables to the y axis part of the curve
a = arrayFIFOCPUBound
b = arrayPRIOCPUBound
c = arrayRRCPUBound
d = arraySJFCPUBound


# Plotting both the curves simultaneously
plt.plot(X, a, color='r', label='FIFO')
plt.plot(X, b, color='g', label='PRIO')
plt.plot(X, c, color='b', label='RR')
plt.plot(X, d, color='y', label='SJF')

# Naming the x-axis, y-axis and the whole graph
plt.xlabel("Número de processos")
plt.ylabel("Tempo médio")
plt.title("Gráfico de tempo médio CPU BOUND dos escalonadores")

# Adding legend, which helps us recognize the curve according to it's color
plt.legend()

# To load the display window
#plt.show()
plt.savefig('TMECPUBound.png')
plt.close()
"""
    Plot do gráfico TEMPO MÉDIO IO Bound
"""
# Using Numpy to create an array X
X = [50, 100, 150, 200, 250]

# Assign variables to the y axis part of the curve
a = arrayFIFOIOBound
b = arrayPRIOIOBound
c = arrayRRIOBound
d = arraySJFIOBound


# Plotting both the curves simultaneously
plt.plot(X, a, color='r', label='FIFO')
plt.plot(X, b, color='g', label='PRIO')
plt.plot(X, c, color='b', label='RR')
plt.plot(X, d, color='y', label='SJF')

# Naming the x-axis, y-axis and the whole graph
plt.xlabel("Número de processos")
plt.ylabel("Tempo médio")
plt.title("Gráfico de tempo médio IO BOUND dos escalonadores")

# Adding legend, which helps us recognize the curve according to it's color
plt.legend()

# To load the display window
#plt.show()
plt.savefig('TMEIOBound.png')



