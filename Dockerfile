FROM python:3.7.4
WORKDIR /real_estate_API
RUN pip install pipenv
COPY . /real_estate_API
RUN pipenv install
ENV PORT = 8080
EXPOSE 8080
# RUN pipenv shell
CMD flask run