Overview
========

Data conversion

Requirements
============
You will need `Python 3+ <https://www.python.org>`_ This package has been tested using python 3.6.
ls

Installation
============

This package is available under devpi server. So you can install it using pip tools as follow:

.. code-block:: bash

    pip install pyavtech

.. note::

    Refer to initialize pip application note in order to point on internal devpi server.

else you have the ability to install it using wheel distribution package:

.. code-block:: bash

    pip install pyavtech-x.y.z-py3-none-any.whl

.. note::

    Replace x.y.z by the package version number.



Package development
===================

The code of the package is developed under :file:`pyhexdata` directory.

Convention
----------

If you are developing new features inside the package, please follow `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_

Note that package will be used by other people, so stability matters.

* Follow `PEP20 <https://www.python.org/dev/peps/pep-0020/>`_

.. code-block:: rest

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

All necessary packages need to develop are identifed in the requirements.txt file.

After cloning, create a virtual environement, activate it and install necessary package:

.. code-block:: bash

    $ git clone ssh://git@git.ul-ts.com:5022/ims-se/hardware-team/pybench/pyavtech.git
    $ cd pyavtech
    $ python -m python3 -m venv venv
    $ .\venv\Script\activate.bat
    (venv) $ pip install -r requirements.txt

To generate python package in wheel format locally:

.. code-block:: bash

    $ python setup.py bdist_wheel


Documentation and package update
--------------------------------

To generate the documentation, use the following command under docs sub-folder:

.. code-block:: bash

    $ make html
    $ make latex

.. warning::

    To generate latex format, the TeX Live utility must be installed first.


Under root directory you can generate the wheel package and the documentation using the following command:

.. code-block:: bash

    $ python setup.py build_sphinx

finally you can build wheel package and documentation and the upload to the devpi server using:

.. code-block:: bash

    $ devpi upload --format=bdist_wheel --with-docsAll necessary packages need to develop are identifed in the requirements.txt file.

After cloning, create a virtual environement, activate it and install necessary package:

.. code-block:: bash

    $ git clone ssh://git@git.ul-ts.com:5022/ims-se/hardware-team/pybench/pyavtech.git
    $ cd pyavtech
    $ python -m python3 -m venv venv
    $ .\venv\Script\activate.bat
    (venv) $ pip install -r requirements.txt

To generate python package in wheel format locally:

.. code-block:: bash

    $ python setup.py bdist_wheel


Documentation and package update
--------------------------------

To generate the documentation, use the following command under docs sub-folder:

.. code-block:: bash

    $ make html
    $ make latex

.. warning::

    To generate latex format, the TeX Live utility must be installed first.


Under root directory you can generate the wheel package and the documentation using the following command:

.. code-block:: bash

    $ python setup.py build_sphinx

finally you can build wheel package and documentation and the upload to the devpi server using:

.. code-block:: bash

    $ devpi upload --format=bdist_wheel --with-docs


.. warning::

    This operation is automatically done using continuous integration at tag creation. Manual operation can be done
    for testing purpose only, but in any case package versioning must be done previously and follow the semantic rules.


.. warning::

    This operation is automatically done using continuous integration at tag creation. Manual operation can be done
    for testing purpose only, but in any case package versioning must be done previously and follow the semantic rules.


References
==========
* `Markdown <https://daringfireball.net/projects/markdown/syntax/>`_
* `Sphinx <https://www.sphinx-doc.org/en/master/>`_


