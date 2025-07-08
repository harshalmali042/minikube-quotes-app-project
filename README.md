## 📦 Project Idea: **Simple Quotes Web App on Minikube**

A basic web app (Node.js or Python Flask) that serves random quotes via HTTP, containerized via Docker, deployed on Kubernetes via Minikube, exposed using a **LoadBalancer** service.

---

## 📁 Directory Structure

```bash
minikube-quotes-app/
├── Dockerfile
├── app/
│   └── app.py
├── requirements.txt
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── .gitignore
└── README.md
```

---

## 📜 Application Code — `app/app.py` (Python Flask Example)

```python
from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "Stay hungry, stay foolish.",
    "Talk is cheap. Show me the code.",
    "First, solve the problem. Then, write the code.",
    "Code never lies, comments sometimes do."
]

@app.route('/')
def get_quote():
    return f"<h2>{random.choice(quotes)}</h2>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```

---

## 📦 Dockerfile

```dockerfile
# Use Python base image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy app code
COPY app/ /app
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
```

---

## 📜 `requirements.txt`

```
flask
```

---

## 📦 Kubernetes Deployment — `k8s/deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: quotes-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: quotes-app
  template:
    metadata:
      labels:
        app: quotes-app
    spec:
      containers:
      - name: quotes-app
        image: atuljkamble/quotes-app:latest
        ports:
        - containerPort: 5000
```

---

## 📦 Kubernetes Service — `k8s/service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: quotes-service
spec:
  type: LoadBalancer
  selector:
    app: quotes-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000
```

---

## ✅ Commands to Run (Mac + Docker Desktop + Minikube)

1️⃣ **Start Minikube using Docker driver**

```bash
minikube start --driver=docker
```

2️⃣ **Build Docker image inside Minikube’s Docker**

```bash
eval $(minikube docker-env)
docker build -t atuljkamble/quotes-app:latest .
```

3️⃣ **Deploy to Kubernetes**

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

4️⃣ **Access the Service URL**

```bash
minikube service quotes-service
```

> It will open your browser at the external LoadBalancer URL.

---

## 📄 .gitignore

```
__pycache__/
.env
*.pyc
*.pyo
.DS_Store
```

---

## 📑 README.md Overview

````markdown
# 📝 Quotes Web App on Minikube

A simple Python Flask web app deployed on Kubernetes using Minikube (Docker Desktop as runtime), exposing a LoadBalancer service accessible via browser.

## 📦 Project Setup
- Python Flask app
- Dockerized
- Deployed with Kubernetes Deployment + LoadBalancer Service
- Load-balanced output via browser on Minikube

## 🚀 Quickstart
```bash
minikube start --driver=docker
eval $(minikube docker-env)
docker build -t atuljkamble/quotes-app:latest .
kubectl apply -f k8s/
minikube service quotes-service
````

## 📸 Output

![app-screenshot](images/app-output.png)

---

```

---

## ✅ Bonus: Auto Image Push (Optional)
You can also push your Docker image to Docker Hub and pull it inside Minikube if you prefer.

---

## 📌 Final Note:
This project is:
- Lightweight ✅
- No external cloud dependency ✅
- Visual browser output ✅
- Load Balancer service ✅
- Docker Desktop on Mac compatible ✅
- Clean repo-ready ✅
