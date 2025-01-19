FROM python:3.9

# Define the user [will create it later]
ARG USER=app
ARG USER_GROUP=app

# Define user related ENVs
ENV HOME=/home/$USER
ENV APP_HOME=$HOME/web
ENV PATH "$PATH:$HOME/.local/bin"
ARG LOG_PATH=$HOME/web/logs

# Create directory for the app user & create the app user
RUN mkdir -p $APP_HOME; \
    mkdir -p $LOG_PATH; \
    groupadd $USER_GROUP; \
    useradd -g $USER_GROUP $USER;

# Change workdir to app dir
WORKDIR $APP_HOME
# Copy requirements files
COPY requirements.txt $APP_HOME

# Install python dependecies
RUN pip install --upgrade pip; \
    pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED 1

# Copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R $USER:$USER_GROUP $APP_HOME

# Switch user
USER $USER
ENTRYPOINT ["bash","./docker-entrypoint.sh"]