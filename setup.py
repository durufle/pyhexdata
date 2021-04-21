from setuptools import setup
from setuptools import find_packages
from os import path
from sphinx.setup_command import BuildDoc

name = 'pyhexdata'
version = '0.2.0'

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(name=name,
      version=version,
      cmdclass={'build_sphinx': BuildDoc},
      command_options={
          'build_sphinx': {
              'project': ('setup.py', name),
              'version': ('setup.py', version),
              'source_dir': ('setup.py', 'docs/source')
          }
      },
      
      description='Hex data conversion',
      long_description=long_description,
      long_description_content_type='text/markdown',
      
      classifiers=[
        'License :: OSI Approved ::  Massachusetts Institute of Technology (MIT)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utils class',
        'Intended Audience :: Developers',
      ],
      
      keywords='HexData',
      
      url='https://git.ul-ts.com/ims-se/hardware-team/pybench/pyhexdata',
      author='Stephane Potti',
      author_email='Stephane.Potti@ul.com',
      python_requires='>=3.6',
      license='MIT',
      packages=find_packages(),
      install_requires=['numpy'],
      zip_safe=False)
