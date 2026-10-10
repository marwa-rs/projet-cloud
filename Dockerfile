# ===== Etape 1 : base commune (Python + dependances + code) =====
FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .

# ===== Etape 2 : tests (jetee apres usage) =====
FROM base AS test
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt
COPY tests/ tests/
RUN python -m pytest -v

# ===== Etape 3 : image finale deployee =====
FROM base AS final
RUN pip uninstall -y pip setuptools wheel \
    && useradd --create-home --uid 10001 appuser
USER appuser
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:5000/health', timeout=2)" || exit 1
CMD ["python", "app.py"]
