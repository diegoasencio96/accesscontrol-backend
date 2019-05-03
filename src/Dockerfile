#FROM python:3.7.2
FROM python:3.6.7
ENV PYTHONUNBUFFERED 1
# Set the file maintainer (your name - the file's author)
LABEL maintainer="diegoasencio96@gmail.com" \
      description="Django con Python 3.6.7" \
      version="1.0"

# Set env variables used in this Dockerfile (add a unique prefix, such as DOCKYARD)
# Local directory with project source
ENV DOCKYARD_SRC=accesscontrol
# Directory in container for all project files
ENV DOCKYARD_SRVHOME=/srv/accesscontrol-backend/src
# Directory in container for project source files
ENV DOCKYARD_SRVPROJ=${DOCKYARD_SRVHOME}/${DOCKYARD_SRC}

# Update the default application repository sources list
RUN apt-get update &&  apt-get install -y python python-pip libpq-dev python-dev python-pil build-essential

# Create application subdirectories
WORKDIR $DOCKYARD_SRVPROJ

RUN mkdir logs
#RUN mkdir media
#VOLUME ["$DOCKYARD_SRVPROJ/media/", "$DOCKYARD_SRVPROJ/logs/"]

VOLUME ["$DOCKYARD_SRVPROJ/logs/"]

# Copy application source code to SRCDIR
COPY $DOCKYARD_SRC $DOCKYARD_SRVPROJ

RUN ls /srv/accesscontrol-backend/src

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r $DOCKYARD_SRVPROJ/requirements.txt

COPY $DOCKYARD_SRC $DOCKYARD_SRVPROJ


# Port to expose
EXPOSE 8000

WORKDIR $DOCKYARD_SRVPROJ
COPY docker-entrypoint.sh /


RUN chmod +x /docker-entrypoint.sh
#ENTRYPOINT ["/docker-entrypoint.sh"]


# Replace packages
#RUN cp -rf $DOCKYARD_SRVPROJ/paquetes_modificados/*/ /usr/local/lib/python2.7/dist-packages/
