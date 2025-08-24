## 🧠 Start API

```
uvicorn dashApi.main:app --reload

poetry run uvicorn dashApi.main:app --reload
```

# Visit Swagger

````
http://localhost:8000/docs
```

```
curl http://127.0.0.1:8000/ping
curl -v "http://127.0.0.1:8000/plot?year=2007" --output plot.png

curl http://127.0.0.1:8000/duckdb-table?table=pointers
```


```
[project]
name = "dashApi"
version = "0.1.0"
description = "A FastAPI backend for data science dashboards"
authors = [{ name = "Your Name", email = "you@example.com" }]
dependencies = [
    "fastapi",
    "uvicorn[standard]",
    "pydantic",
    "pydantic_settings",
    "typer"
]

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
````
