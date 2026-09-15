# Run these inside the activated environment: mamba activate wrr-proj
.PHONY: all data build test test-all lint fmt clean

all: data build test

data:        ## prepare/download input data (you implement this)
	python -m wrr.scripts.prepare_data

build:       ## run the analysis pipeline; writes results/ and figures/
	python -m wrr.scripts.run_analysis

test:        ## fast tests only (no geodata needed)
	pytest -m "not heavy"

test-all:    ## all tests, including those needing the geospatial stack
	pytest

lint:        ## check code style without changing files
	ruff check . && ruff format --check .

fmt:         ## auto-format code and fix simple issues
	ruff format . && ruff check --fix .

clean:       ## remove generated outputs
	rm -rf results/* figures/* || true
