FROM python:alpine
WORKDIR /program
COPY . /program
RUN pip install nltk
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt
CMD [ "python", "pythonScript.py"]