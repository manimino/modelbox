FROM python3
COPY . /
RUN pip install -r requirements.txt
ENTRYPOINT /entrypoint.sh