# This  builder section is optimized to allow this layer to cache since dependencies will not change often
FROM ghcr.io/astral-sh/uv:python3.12-bookworm AS builder
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv export --frozen --no-dev --format requirements-txt > requirements.txt \
 && uv pip install --no-deps --target /opt/python -r requirements.txt

# This is the main layer that the app will run inside of
FROM public.ecr.aws/lambda/python:3.12
# Copy files from builder - this allows us to keep the final image smaller
COPY --from=builder /opt/python /opt/python
# Copy main src files - this can be optimized for multi module building
COPY src/ ${LAMBDA_TASK_ROOT}/src/
# Copy main entrypoint script
COPY lambda.py ${LAMBDA_TASK_ROOT}/

# entrypoint
CMD ["lambda.handler"]