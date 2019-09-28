FROM python:alpine

RUN pip install poetry

COPY . /3on3bot/
WORKDIR /3on3bot

RUN poetry install

CMD ["poetry", "run", "python", "run_bot.py"]
