# HexData package

To install package using pip

```bash
pip install pyhexdata
```

To install the package version x.x.x from wheel:

```bash
pip install pydei-x.x.x-py3-none-any.whl 
```

To import the Hexdata module in your code:
```python
from pyhexdata.HexData import HexData
```

To create virtual environment (venv):

```bash
# Create virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate.bat

# set pip configuration for server
# pip.ini in venv directory

# Install package requirements 
(venv) pip install -r requirements.txt
```

To generate the package distribution :

```bash
# Package distribution only
python setup.py bdist_wheel

# Package distribution and sphinx documentation
python setup.py bdist_wheel build_sphinx
```
