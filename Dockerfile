FROM python:3.7.4
WORKDIR /real_estate_API
RUN pip install pipenv
COPY . /real_estate_API
RUN pipenv install
<<<<<<< HEAD
=======
ENV PORT = 8080
EXPOSE 8080
>>>>>>> 9201233 (dockerfile)
# RUN pipenv shell
CMD flask run
