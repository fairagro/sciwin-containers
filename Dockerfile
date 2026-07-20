FROM python:3.13-slim

LABEL net.fairagro.sciwin.lang="python"
LABEL net.fairagro.sciwin.version="3.13"
LABEL net.fairagro.sciwin.requirements='[\
        "pandas==3.0.4", \
        "numpy==2.5.0", \
        "matplotlib==3.10.6", \
        "kaleido==0.2.1",\
        "plotly==6.9.0",\
        "requests==2.32.5"\
    ]'
LABEL net.fairagro.use-case="datascience"

RUN pip install --no-cache-dir \
    pandas==3.0.4 \
    numpy==2.5.0 \
    matplotlib==3.10.6 \
    kaleido==0.2.1 \
    plotly==6.9.0 \
    requests==2.32.5 \