# HexData package

To install package using pip

```bash
pip install ragnarok-pyhexdata
```

To install the package version x.x.x from wheel:

```bash
pip install pyhexdata-x.x.x-py3-none-any.whl 
```

To import the Hexdata module in your code:
```python
from pyhexdata.HexData import HexData
```

To create virtual environment on windows:

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

On linux:

```bash
# Create virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# set pip configuration for server
# pip.ini in venv directory

# Install package requirements 
(venv) pip install -r requirements.txt
# Install package development 
(venv) pip install -r development.txt
```

To generate the package distribution :

```bash
# Package distribution only
(venv) python -m build
```

To execute test:

```bash
(venv) pytest
```
To see coverage in html execute the following command :

```bash
(venv)  coverage html
```

by default coverage html report are in ```htmlcov``` folder.

