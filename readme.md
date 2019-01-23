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
