FROM python:3.11-slim

ENV TZ=Asia/Shanghai

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "tieba_sign.py"]
