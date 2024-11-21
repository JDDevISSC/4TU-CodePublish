FROM python:3-alpine3.19

WORKDIR /app

COPY pyproject.toml .
COPY _4tu_codepublish .
COPY module_build.sh .
COPY module_install.sh .

RUN ./module_build.sh
RUN ./module_install.sh

CMD ["4tu-codepublish"]