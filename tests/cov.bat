coverage erase
coverage run --branch --parallel-mode test.py
coverage combine
coverage report -m ../HexData.py
coverage html
