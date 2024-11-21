FROM python:3-alpine3.19

WORKDIR /app

COPY ./dist ./dist
COPY pyproject.toml .
COPY module_install.sh .

RUN ./module_install.sh

CMD ["4tu-codepublish"]