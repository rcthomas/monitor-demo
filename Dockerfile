FROM continuumio/miniconda3:latest

RUN \
    conda install --yes nomkl scipy

# This could be done with PYTHONPATH etc
# May want to watch out for pre-existing sitecustomizes
# Also, how to *install* them using Python install tools is like, not a thing?

ADD sitecustomize.py /opt/conda/lib/python3.8/site-packages

WORKDIR /srv
ADD app* /srv/.
ADD run.sh /srv/.

CMD ["/bin/bash", "run.sh"]
