FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

#Copy project files to container
COPY . /app/

#change work directory
WORKDIR /app

#install dependencies
RUN pip install -r requirements.txt

# if you want to add custom commands you can add here 
# RUN <your command>
# eg: RUN python -m venv venv


ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

# application port. 
EXPOSE 5000