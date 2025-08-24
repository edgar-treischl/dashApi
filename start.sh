#!/bin/bash
source .venv/bin/activate
uvicorn dashApi.main:app --host 0.0.0.0 --port 8000
