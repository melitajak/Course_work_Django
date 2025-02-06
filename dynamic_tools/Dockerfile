 
FROM python:3.9-slim

 
ENV DEBIAN_FRONTEND=noninteractive

 
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    procps \
    ca-certificates \
    && apt-get clean

 
RUN useradd -m -s /bin/bash brewuser && \
    mkdir -p /home/brewuser/homebrew /home/brewuser/miniconda && \
    chown -R brewuser:brewuser /home/brewuser

 
USER brewuser
WORKDIR /home/brewuser

 
RUN git clone https://github.com/Homebrew/brew homebrew && \
    echo 'eval "$(/home/brewuser/homebrew/bin/brew shellenv)"' >> ~/.bashrc && \
    /home/brewuser/homebrew/bin/brew shellenv && \
    /home/brewuser/homebrew/bin/brew update && \
    /home/brewuser/homebrew/bin/brew install gcc

 
ENV PATH="/home/brewuser/homebrew/bin:$PATH"

 
RUN curl -o miniconda.sh -sSL https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash miniconda.sh -b -u -p /home/brewuser/miniconda && \
    rm miniconda.sh && \
    echo 'export PATH="/home/brewuser/miniconda/bin:$PATH"' >> ~/.bashrc && \
    /home/brewuser/miniconda/bin/conda init bash && \
    /home/brewuser/miniconda/bin/conda config --set always_yes yes --set changeps1 no && \
    /home/brewuser/miniconda/bin/conda update -q conda

 
ENV PATH="/home/brewuser/miniconda/bin:$PATH"

 
USER root

 
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

 
COPY . /app/
WORKDIR /app

 
EXPOSE 8000

 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
