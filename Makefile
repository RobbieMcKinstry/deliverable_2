all:

clear:
	clear

serve: clear
	python main.py

test: clear
	python -m unittest -v test_math
