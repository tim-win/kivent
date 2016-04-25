import os
import sys
from setuptools import setup, find_packages

os.environ['KIVY_DOC_INCLUDE'] = '1'
import kivy

if sys.platform == 'win32':
    compile_args = ['-std=gnu99', '-ffast-math']
    libraries = ['opengl32', 'glu32','glew32']
else:
    compile_args = ['-std=c99', '-ffast-math', "-w"]
    libraries = []

setup(
    name='KivEnt.Velocity',
    description='''A game engine for the Kivy Framework.
        https://github.com/Kovak/KivEnt for more info.''',
    author='Jacob Kovac',
    author_email='kovac1066@gmail.com',
    packages=find_packages(),
    package_data={
        '': ['*.pxd', '*.so']
    },
    setup_requires=['cython', 'setuptools.autocythonize'],
    auto_cythonize={
        "compile_args": compile_args,
        "libraries": libraries,
        "includes": kivy.get_includes()
    }
)
