# DevOps Challenge - The Disaster Recovery

## Context

Identify and fix all critical issues.

## Objectives

### CI/CD Pipeline
- Make the GitHub Actions pipeline fully functional
- Properly dockerize the application following best practices
- Remove all obvious security vulnerabilities
- Optimize build time and image size

### Kubernetes
- Fix all manifests to be production-ready
- Implement RBAC correctly using the principle of least privilege
- Configure probes, resources, and security contexts
- Solve networking issues between services

### IaC & Automation
- Repair the Terraform code and make it modular
- Create automation scripts for validation and deployment
- Implement pre-deployment security validations
- Document the proposed architecture

## Initial Setup

### Install Docker
- Official guide: [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)

### Install Minikube
- Official guide: [https://minikube.sigs.k8s.io/docs/start/](https://minikube.sigs.k8s.io/docs/start/)

```bash
# Clone the repository
git clone <repo-url>
cd devops-challenge

# Install local dependencies
pip install -r app/requirements.txt

# Docker setup
docker-compose up -d

# Optional: local Kubernetes setup
minikube start
kubectl apply -f k8s/

# Validate Terraform
cd terraform
terraform init
terraform validate
terraform plan
```

## Evaluation Criteria

| Category | Explanation |
|-----------|-------------------|
| **Identification** | Did you find all critical issues? |
| **Technical Solution** | Did you implement correct and efficient fixes? |
| **Security** | Did you eliminate vulnerabilities? Did you apply hardening? |
| **Best Practices** | Did you follow industry standards? |
| **Documentation** | Are your decisions clearly explained? |
