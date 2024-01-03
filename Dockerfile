FROM python:3.11.0
WORKDIR /app
EXPOSE 80
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
