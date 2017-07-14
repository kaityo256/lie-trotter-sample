PNG=n_1.png h_1.png n_2.png h_2.png
all:$(PNG)

.SUFFIXES: .png .dat

n_1.dat: lie-trotter.py
	python lie-trotter.py

h_1.dat: n_1.dat
h_2.dat: n_2.dat
n_2.dat: n_1.dat

n_1.png: n_1.dat
h_1.png: h_1.dat

n_2.png: n_2.dat
h_2.png: h_2.dat


.dat.png:
	gnuplot $*.plt


clean:
		rm -f n_1.dat n_2.dat
		rm -f h1_1.dat h2_1.dat h4_1.dat
		rm -f h1_2.dat h2_2.dat h4_2.dat
		rm -f $(PNG)
