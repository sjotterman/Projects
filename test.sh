#/usr/bin/sh

nosetests -w Numbers

ret=`python -c 'import sys; print("%i" % (sys.hexversion<0x03000000))'`
if [ $ret -eq 0 ]; then
   nosetests3 -w Numbers
else 
    nosetests -w Numbers
fi
