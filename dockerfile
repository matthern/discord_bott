FROM python:3.8
RUN mkdir /app
COPY bot.py /app
COPY main.py /app
COPY responses.py /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y ffmpeg
CMD ["python", "main.py"]
