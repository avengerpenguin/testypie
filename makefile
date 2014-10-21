VENV=venv
PIP=${VENV}/bin/pip


clean:
	rm -rf ${VENV}


venv:
	virtualenv --python python3 ${VENV}
	${PIP} install -r requirements.txt


run: venv
	${VENV}/bin/python testypie.py
