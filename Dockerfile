FROM mcr.microsoft.com/playwright/python:v1.50.0-noble
RUN pip install playwright pyyaml
RUN playwright install 