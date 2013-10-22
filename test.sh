#/usr/bin/sh

case "$(python --version 2>&1)" in
    *" 3."*)
        nosetests3 -w Numbers
        ;;
    *)
        pip install nosetests3
        nosetests -w Numbers
        ;;
esac

