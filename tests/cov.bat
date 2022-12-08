coverage erase
coverage run --branch --parallel-mode test.py
coverage combine
coverage report -m ../pyhexdata/HexData.py
coverage html
