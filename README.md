## 📦 Project Structure

```
minikube-quotes-app/
├── app.py
├── Dockerfile
├── requirements.txt
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
└── README.md
```
```
cd Downloads
git clone https://github.com/atulkamble/minikube-quotes-app.git
cd minikube-quotes-app
```
## minikube start 
```
minikube start
```
---

## **minikube-quotes-app**

````markdown
# 📖 Minikube Quotes App 🚀

A lightweight Python Flask web app serving random developer wisdom quotes, EQ reflections, and coding GIFs — deployable easily on **Docker** and **Minikube (Kubernetes)**!

---

## 📦 Features

- 📝 30 developer wisdom quotes
- 🎨 20 coding-themed GIFs
- 💖 10 EQ affirmations
- 🔄 No immediate GIF repeats
- 📄 JSON API endpoint
- 📊 Health check route
- 🐳 Docker container support
- ☸️ Minikube-ready Kubernetes deployment

---

## 📥 Local Installation & Usage

### 📦 Install dependencies

```bash
pip install -r requirements.txt
````

### ▶️ Run locally

```bash
python app.py
```

Visit: `http://localhost:5000/`

---

## 🐳 Docker Deployment

### 📦 Build and Push Docker image

```bash
docker build -t atuljkamble/minikube-quotes-app .
docker push atuljkamble/minikube-quotes-app
```

### ▶️ Run Docker container

```bash
docker run -d -p 5000:5000 atuljkamble/minikube-quotes-app
```

Visit: `http://localhost:5000/`

---

## ☸️ Minikube Kubernetes Deployment

### 📦 Load Docker image into Minikube

```bash
minikube image load minikube-quotes-app:latest
```

### 📄 Apply Kubernetes manifests

```bash
kubectl apply -f k8s/
```

### 📊 Expose the service

```bash
minikube service minikube-quotes-service
```

It will open your app in the browser.

---

## 📑 JSON API Endpoints

* `http://localhost:5000/?format=json`
* `http://localhost:5000/health`

---

## 📚 Project Structure

```
minikube-quotes-app/
├── app.py
├── Dockerfile
├── requirements.txt
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
└── README.md
```

---

## 📌 Author

👤 Atul Kamble

---

## 📜 License

MIT License


---

## 📃 Updated `Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY app.py /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
````

---

## 📃 Updated `k8s/deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: minikube-quotes-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: minikube-quotes
  template:
    metadata:
      labels:
        app: minikube-quotes
    spec:
      containers:
      - name: minikube-quotes-container
        image: minikube-quotes-app:latest
        imagePullPolicy: Never
        ports:
        - containerPort: 5000
```

---

## 📃 Updated `k8s/service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: minikube-quotes-service
spec:
  type: NodePort
  selector:
    app: minikube-quotes
  ports:
    - protocol: TCP
      port: 5000
      targetPort: 5000
      nodePort: 30080
```
```
minikube dashboard
```
---
