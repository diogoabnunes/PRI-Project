.PHONY: all venv run clean

VENV := venv_pri
SRC ?= ./src/


all: venv

run: processed_data venv 
	cd src && ls | grep -e ^.*.py$ | xargs -I _ ../$(VENV)/bin/python3 _

venv: $(VENV)/bin/activate

processed_data:
	mkdir $@

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

clean:
	rm -rf $(VENV)
	rm -rfi processed_data/
