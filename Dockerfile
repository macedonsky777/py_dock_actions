FROM ghcr.io/macedonsky777/py_dock_actions:main

RUN pip3 install coverage

COPY tests /workdir

ENTRYPOINT ["python3", "tests.py"]
