# 
FROM python:3.9

RUN mkdir /code
# 
WORKDIR /code

# 
COPY requirements.txt /code

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
COPY ./ /code/

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
