# 1 Base image 
FROM python:3.12-slim

# 2  now select working directory 
WORKDIR /app 

# 3 install system dependencies 
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


# 4 copy req
COPY requirements.txt .

# 5 Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6 copy appplication code
COPY . .

#  7 expose fastapi post
EXPOSE 8000

#  8 run application 
CMD ["uvicorn" , "main:app" , "--host" , "0.0.0.0" , "--port" , "8000"]

