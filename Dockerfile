FROM python:3.10-slim AS builder

COPY ./app/requirements.txt requirements.txt
COPY ./app/requirements-dev.txt requirements-dev.txt

RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup

USER appuser

RUN pip install --upgrade pip && \
    pip install --user --no-cache-dir -r requirements.txt

ARG ENV
RUN if [ "$ENV" = "test" ]; then \
    pip install --user --no-cache-dir -r requirements-dev.txt; \
    fi;

FROM python:3.10-slim AS production

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

COPY --from=builder /home/appuser/.local/ /home/appuser/.local/

ENV PATH=/home/appuser/.local/bin:$PATH

EXPOSE 8080

WORKDIR /app

COPY ./app /app

RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup

RUN chown -R appuser:appgroup /app

USER appuser

CMD ["python", "main.py"]

