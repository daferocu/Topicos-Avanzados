FROM python:3.10
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8989
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8989"]