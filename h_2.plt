set term png 16
set out "h_2.png"
set log xy
set format y "10^{%L}"
set xla "h"
set yla "Error"
set key at 0.06,1e-3
p "h1_2.dat" t "n=1"\
, "h2_2.dat" t "n=2"\
, "h4_2.dat" t "n=4"\
, x**3*1e-4 lc rgb "black" lw 2 t "h**3"
