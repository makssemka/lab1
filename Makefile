.PHONY: all venv

# Set the main shell for executing tasks.
SHELL := /bin/bash

SOURCES := $(shell find . -name '*.py' -not -path '*./.venv/*' -not -path '*./.git/*' -print)

PROGRAM := lab1.py

all: lint

venv: .venv/bin/activate
.venv/bin/activate: requirements.txt
	@python3 -m venv ./.venv

	# Install the required python packages inside a new virtual environment.
	@.venv/bin/python -m pip install -r requirements.txt

	@touch .venv/bin/activate

black: venv
	@.venv/bin/black --target-version=py38 --line-length=100 -- $(SOURCES)

lint: venv
	-.venv/bin/pylint -- $(SOURCES)
	-.venv/bin/flake8 -- $(SOURCES)
	
run: lint
	python3 $(PROGRAM)
