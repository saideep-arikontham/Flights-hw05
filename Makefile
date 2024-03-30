.PHONY: data, clean


data/flight_data:
	mkdir -p data
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/rdata/main/data/mydb.sqlite

q1: data/flight_data
	mkdir -p figs
	python -B src/q1.py

q2: data/flight_data
	mkdir -p figs
	python -B src/q2.py

q3: data/flight_data
	python -B src/q3.py

q4: data/flight_data
	python -B src/q4.py
