FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
#   software-properties-common \
  python3 \
  python3-pip

WORKDIR /ubuntu-dir

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY main.py ./

# ENV APP_PORT=8081

# EXPOSE 8081

CMD ["python3", "./main.py"]
# CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]




# docker run -d ubuntu_v1