FROM python:latest as development

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip && \
  pip install -r requirements.txt --no-cache-dir

COPY . /app

# Alias for python - py
RUN ln -s $(which python) /usr/bin/py

# Alias for db:migrate
RUN echo -e "#!/bin/sh\npython ./main/manage.py migrate" > /usr/bin/db:migrate && chmod +x /usr/bin/db:migrate

# Alias for db:create
RUN echo -e "#!/bin/sh\npython ./main/manage.py makemigrations" > /usr/bin/db:create && chmod +x /usr/bin/db:create

# Alias for create superuser
RUN echo -e "#!/bin/sh\npython ./main/manage.py createsuperuser" > /usr/bin/create:admin && chmod +x /usr/bin/create:admin

# Alias for django - python ./main/manage.py
RUN echo -e "#!/bin/sh\npython ./main/manage.py \$@" > /usr/bin/django && chmod +x /usr/bin/django
