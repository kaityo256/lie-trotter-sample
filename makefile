all: n.png h.png

n.dat: lie-trotter.py
	python lie-trotter.py

h.dat: n.dat

n.png: n.dat
	gnuplot n.plt

h.png: h.dat
	gnuplot h.plt

clean:
		rm -f h.dat n.dat n.png h.png
