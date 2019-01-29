# Simple Python Profiler
Simple download the `dist/py_profiler-0.0.0-py3-none-any.whl` file and run the pip install command to install it.

`pip install py_profiler-0.0.0-py3-none-any.whl`

To use the library simply import the py decorator :
`from profiler import profiler`

So wherever you need need to profile the function just add the profile decorator before the function:

    
    from profiler import profiler
    @profiler
    def my_func():
        # do something

As result to the script data related to the script will be generated

bhi to de
     6 function calls in 0.000 seconds
     Ordered by: standard name

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 test.py:4(main)
        4    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         6 function calls in 0.000 seconds

    Ordered by: cumulative time

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 test.py:4(main)
        4    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}