FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PORT=8080
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt     && useradd --create-home --uid 10001 appuser
COPY --chown=appuser:appuser service ./service
USER 10001
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s --start-period=15s     CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')" || exit 1
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--access-logfile", "-", "--error-logfile", "-", "service:app"]
