# Docker-k8s-project

This repository is a collection of DevOps projects showcasing containerization and orchestration skills.

## Projects Included

### 1. Chat App (3-Tier Architecture)
A real-time chat application deployed on a Kubernetes cluster.
- **Frontend:** Nginx serving a static interface.
- **Backend:** Flask (Python) handling API requests.
- **Database:** PostgreSQL for persistent data storage.
- **Infrastructure:** Managed via Kubernetes manifests (Deployments, Services, PV, PVC, Ingress).

##  How to Deploy the Chat App
1. **Create Namespace:** `kubectl apply -f k8s/namespace.yaml`
2. **Setup Persistence:** `kubectl apply -f k8s/pv.yaml -f k8s/pvc.yaml`
3. **Deploy Database:** `kubectl apply -f k8s/postgres-db.yaml`
4. **Deploy Application:** `kubectl apply -f k8s/backend-deployment.yaml -f k8s/frontend-deployment.yaml`
