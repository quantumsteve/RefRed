#-*- coding: utf-8 -*-
'''
  Templeates used for ASCII file creation.
'''

config_file='reduction'
NO_INTERPOLATION=True

gp_template=u"""#!/usr/bin/gnuplot
# Gnuplot script automatically generated by QuickNXS.
# Can be used to create plots of exported datasets.
# 
set term png enhanced size %(pix_x)i,%(pix_y)i font "DejaVuSans,24" lw 2
set output "%(output)spng"
set encoding iso_8859_1

set grid ytics mytics xtics
set xlabel "%(xlabel)s"
set format y "10^{%%L}"
set ylabel "%(ylabel)s" offset -1
set title "%(title)s"

set log y
set xrange [0:*]
set yrange [*:2]
unset bars

plot %(plot_lines)s
"""

gp_template_3D=u"""#!/usr/bin/gnuplot
# Gnuplot script automatically generated by QuickNXS.
# Can be used to create plots of exported datasets.
# 
set term png enhanced size %(pix_x)i,%(pix_y)i font "DejaVuSans,24" lw 2
set output "%(output)spng"
set encoding iso_8859_1

set xlabel "%(xlabel)s"
set ylabel "%(ylabel)s"
set cblabel "%(zlabel)s" offset 1
set format cb "10^{%%L}"

set xrange [%(xrange)s]
set yrange [%(yrange)s]
set cbrange [%(zmin)s:%(zmax)s]

set log cb
set pm3d map interpolate 5,5
set palette defined (0 "blue", 1 "green", 2 "yellow", 3 "red", 4 "purple", 5 "black")
set size ratio %(ratio)f

Imin(x)=x>0?x:%(zmin)s

set multiplot layout %(rows)i,%(cols)i title "%(title)s"
%(plot_lines)s
unset multiplot
"""

gp_line=u'"%(file_name)s" u 1:2:3 w errorlines t "(%(channel)s)" lw 1.5 pt 7 ps 0.25'
#GP_LINE=u'"%(file_name)s" u 1:2:4:3 w xyerrorbars t "(%(channel)s)" lw 1.5 lc %(index)i pt 7 ps 0.5, "%(file_name)s" u 1:2 smooth csplines t "" lw 1.5 lc %(index)i'
gp_line_3D=u'splot "%(file_name)s" u %(x)i:%(y)i:(Imin($%(z)i)) w pm3d t ""'
#GP_LINE_3D=u'splot "%(file_name)s" u %(x)i:%(y)i:%(z)i w pm3d t ""'
GP_SEP=u',\\\n     '
GP_SEP_3D=u'\nset title "%s"\n'

# set of characters to replace, as they can't be iso_8859_1 encoded but are
# avalable with gnuplot enhanced commands
GP_REPLACE_CHARS=(
                  (u'α', u'{/Symbol a}'),
                  (u'δ', u'{/Symbol d}'),
                  )

gp_font_paths=[u'/usr/share/fonts/dejavu/', u'/usr/share/fonts/truetype/ttf-dejavu/']

FILE_HEADER=u'''# Datafile created by QuickNXS %(version)s
# Date: %(date)s
# Type: %(datatype)s
# Input file indices: %(indices)s
# Extracted states: %(channels)s
#
# Parameters used for extraction of direct beam:
# I0           P0  PN    x0       xw           y0       yw           bg0      bgw          Direct Pixel TTH          Number       DB Index  FAN  File
%(norm_lines)s
#
# Parameters used for extraction of reflectivity:
# I0           P0  PN    x0       xw           y0       yw           bg0      bgw          Direct Pixel TTH          Number       DB Index  FAN  File
%(params_lines)s
#
# Column Units:
# %(column_units)s
# Column Names:
# %(column_names)s
'''
FILE_HEADER_PARAMS=u'%(scale)-12g %(P0)-3i %(PN)-5i %(x_pos)-8g %(x_width)-12g %(y_pos)-8g %(y_width)-12g %(bg_pos)-8g %(bg_width)-12g %(dpix)-12g %(tth)-12g %(file_number)-12s %(norm_index)-9s %(extract_fan)-4i %(file_name)-12s '

DICTIZE_CHANNELS={
                 'x': 'unpolarized',
                 '+': 'up',
                 '-': 'down',
                 '++': 'upup',
                 '--': 'downdown',
                 '+-': 'updown',
                 '-+': 'downup',
                 }
