#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        function = fct(*args)
        return(function)
    except Exception as err:
        sys.stderr.write('Exception: {}\n'.format(err))
        result = None
        return (result)
