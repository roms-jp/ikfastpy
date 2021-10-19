from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    name='ikfastpy',
    version='0.0.1',
    package_dir={'ikfastpy': ''},
    packages=['ikfastpy'],
    ext_modules=[
        Extension(
            "ikfastpy",
            ["ikfastpy.pyx", "ikfast_wrapper.cpp"],
            language="c++",
            libraries=['lapack']
            )],
    cmdclass = {'build_ext': build_ext}
    )
# setup(ext_modules=[Extension("ikfastpy", 
#                            ["ikfastpy.pyx", 
#                             "ikfast_wrapper.cpp"], language="c++", libraries=['lapack'])],
#      cmdclass = {'build_ext': build_ext})
