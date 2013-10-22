#/usr/bin/sh

case "$(python --version 2>&1)" in
    *" 3."*)
        pip install nose3
        nosetests3 -w Numbers
        ;;
    *)
        nosetests -w Numbers
        ;;
esac

