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
## 📸 Screenshots

### 🖥️ App Interface  
![Minikube Quotes App](screenshots/quotes-app.png)

---

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

```
minikube dashboard
```
```
minikube service minikube-quotes-service

```
# Commands
```
cd Downloads
git clone https://github.com/atulkamble/minikube-quotes-app.git
cd minikube-quotes-app
cd app
// manually run app

python3 app.py

docker login 

// build image and push to dockerhub 

docker build -t atuljkamble/minikube-quotes-app .
docker push atuljkamble/minikube-quotes-app

// locally create container 

docker run -d -p 5000:5000 atuljkamble/minikube-quotes-app

// access from browser 

http://localhost:5000/

// stop container 

docker container stop b6c3480f212f

// start k8s cluster 

minikube start

minikube addons enable metrics-server

minikube dashboard 

// update your dockerhub username in k8s/deployment.yaml

// apply yaml templates 

kubectl apply -f k8s

// list nodes, deployments,, services, pods 

kubectl get nodes
kubectl get deployments
kubectl get pods
kubectl get svc

kubectl get all 

minikube service minikube-quotes-service

// open output in browser 

http://127.0.0.1:50891

minikube ip

```
---

**Atul Kamble**

- 💼 [LinkedIn](https://www.linkedin.com/in/atuljkamble)
- 🐙 [GitHub](https://github.com/atulkamble)
- 🐦 [X](https://x.com/Atul_Kamble)
- 📷 [Instagram](https://www.instagram.com/atuljkamble)
- 🌐 [Website](https://www.atulkamble.in)

---

## 📜 License

MIT License

---
