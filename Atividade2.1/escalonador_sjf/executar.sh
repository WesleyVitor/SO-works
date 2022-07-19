#bin/bash
# for i in 1 2 3 4 5 6 7 8 9 10; do
# 	./escalonador 50 | grep "Tempo medio de espera:" | cut -d " " -f 5 >> resultado1.txt
# 	./escalonador 100 | grep "Tempo medio de espera:" | cut -d " " -f 5 >> resultado2.txt
# 	./escalonador 150 | grep "Tempo medio de espera:" | cut -d " " -f 5 >> resultado3.txt
# 	./escalonador 200 | grep "Tempo medio de espera:" | cut -d " " -f 5 >> resultado4.txt
# 	./escalonador 250 | grep "Tempo medio de espera:" | cut -d " " -f 5 >> resultado5.txt
for i in 1 2 3 4 5 6 7 8 9 10; do
	./escalonador 50 | grep "Tempo medio de espera" | grep -Eo "[0-9]{6}" > TMEGeral50.txt
	head -1 TMEGeral50.txt | tail -1 >> TME50.txt
	head -2 TMEGeral50.txt | tail -1 >> TMECPUBound50.txt
	head -3 TMEGeral50.txt | tail -1 >> TMEIOBound50.txt
	./escalonador 100 | grep "Tempo medio de espera" | grep -Eo "[0-9]{6}" > TMEGeral100.txt
	head -1 TMEGeral100.txt | tail -1 >> TME100.txt
	head -2 TMEGeral100.txt | tail -1 >> TMECPUBound100.txt
	head -3 TMEGeral100.txt | tail -1 >> TMEIOBound100.txt
	./escalonador 150 | grep "Tempo medio de espera" | grep -Eo "[0-9]{6}" > TMEGeral150.txt
	head -1 TMEGeral150.txt | tail -1 >> TME150.txt
	head -2 TMEGeral150.txt | tail -1 >> TMECPUBound150.txt
	head -3 TMEGeral150.txt | tail -1 >> TMEIOBound150.txt
	./escalonador 200 | grep "Tempo medio de espera" | grep -Eo "[0-9]{6}" > TMEGeral200.txt
	head -1 TMEGeral200.txt | tail -1 >> TME200.txt
	head -2 TMEGeral200.txt | tail -1 >> TMECPUBound200.txt
	head -3 TMEGeral200.txt | tail -1 >> TMEIOBound200.txt
	./escalonador 250 | grep "Tempo medio de espera" | grep -Eo "[0-9]{6}" > TMEGeral250.txt
	head -1 TMEGeral250.txt | tail -1 >> TME250.txt
	head -2 TMEGeral250.txt | tail -1 >> TMECPUBound250.txt
	head -3 TMEGeral250.txt | tail -1 >> TMEIOBound250.txt

done
