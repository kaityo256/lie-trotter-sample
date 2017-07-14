set term png 16
set out "h_1.png"
set log xy
set format y "10^{%L}"
set xla "h"
set yla "Error"
set key at 0.08,4e-2
p "h1_1.dat" t "n=1"\
, "h2_1.dat" t "n=2"\
, "h4_1.dat" t "n=4"\
, x**2*7e-3 lc rgb "black" lw 2 t "h**2"
