FROM python:3.11.8-alpine3.19

WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache gcc musl-dev g++ libffi-dev openssl-dev make  libstdc++ && \
    pip3 install --no-cache-dir -r requirements.txt && \
    apk del gcc musl-dev g++ libffi-dev openssl-dev make

COPY . .

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]