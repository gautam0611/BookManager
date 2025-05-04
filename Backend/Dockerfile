FROM python:3.11-slim 

WORKDIR /backend

# Set PYTHONPATH to include the working directory
ENV PYTHONPATH=/backend

# copy requirements.txt into the container 
COPY requirements.txt .

# install the dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the code into the container 
COPY . .

EXPOSE 8000 

CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000"]