#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        function = fct(*args)
        return(function)
    except Exception as err:
        sys.stderr.write('Exception: {}\n'.format(err))
        result = None
        return (result)
