FROM tensorflow/tensorflow

WORKDIR /code

COPY TaylorLM.py .
COPY main.py .
COPY taylor_blstm_model/ taylor_blstm_model/
COPY tokenizer.pickle .

RUN pip install fastapi
RUN pip install uvicorn

CMD ["python", "main.py"]