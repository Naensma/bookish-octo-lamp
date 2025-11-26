# 🔥 DevOps Challenge - The Disaster Recovery

## 📖 Context

You've been hired as a DevOps engineer to rescue a legacy project in crisis. The previous team left the codebase in a chaotic state before leaving. Your mission: identify and fix all critical issues within 60 minutes.

## ⚠️ Current Situation

- The CI/CD pipeline fails constantly
- Production containers crash randomly
- Kubernetes reports permission and resource errors
- The Terraform infrastructure is corrupted
- Multiple security vulnerabilities are present

## 🎯 Objetivos

### Level 1: CI/CD Pipeline (20 min)
✅ Make the GitHub Actions pipeline fully functional
✅ Properly dockerize the application following best practices
✅ Remove all obvious security vulnerabilities
✅ Optimize build time and image size

### Nivel 2: Kubernetes (20 min)
✅ Fix all manifests to be production-ready
✅ Implement RBAC correctly using the principle of least privilege
✅ Configure probes, resources, and security contexts
✅ Solve networking issues between services

### Nivel 3: IaC & Automation (20 min)
✅ Repair the Terraform code and make it modular
✅ Create automation scripts for validation and deployment
✅ Implement pre-deployment security validations
✅ Document the proposed architecture

## 📦 Estructura del Repositorio

```
.
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Broken pipeline
├── app/
│   ├── main.py                # Python application
│   ├── requirements.txt
│   └── tests/
├── docker/
│   ├── Dockerfile             # Multiple issues
│   └── docker-compose.yml     # Incorrect configuration
├── k8s/
│   ├── deployment.yml         # No limits, broken probes
│   ├── service.yml            # Wrong selector
│   ├── configmap.yml          # Exposed secrets
│   ├── rbac.yml               # Excessive permissions
│   └── ingress.yml            # Insecure configuration
├── terraform/
│   ├── main.tf                # Syntax errors
│   ├── variables.tf           # Poorly defined
│   ├── outputs.tf             # Not working
│   └── modules/
│       └── gke/               # Faulty module
├── scripts/
│   ├── deploy.sh              # Buggy bash script
│   └── validate.py            # Buggy Python
└── docs/
    └── PROBLEMS.md            # List of identified issues
```

## 🚀 Initial Setup

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


## 📋 Deliverables

### 1. Fixed Code
- Make atomic commits with descriptive messages
- Each identified issue must have its own commit
- Use conventional commit messages: fix:, feat:, sec:, etc.

### 2. Documentation (docs/PROBLEMS.md)
For each issue you find and fix, document it using the provided template:
    - **Category**: CI/CD, Docker, Kubernetes, Terraform, Security, Scripting, etc.
    - **Severity**: Critical, High, Medium, Low
    - **Description**: What was wrong?
    - **Impact**: What consequences did it cause?
    - **Solution**: How did you fix it?
    - **Prevention**: How can it be avoided in the future?

### 3. Implemented Improvements
- List any additional optimizations
- Provide technical justification for your decisions
- Note any trade-offs considered


## 🎯 Evaluation Criteria

| Categoría | Peso | Aspectos Evaluados |
|-----------|------|-------------------|
| **Identification** | 25% | Did you find all critical issues? |
| **Technical Solution** | 35% | Did you implement correct and efficient fixes? |
| **Security** | 20% | Did you eliminate vulnerabilities? Did you apply hardening? |
| **Best Practices** | 15% | Did you follow industry standards? |
| **Documentation** | 5% | Are your decisions clearly explained? |

## 🔍 Hints (Do not open before trying)

<details>
<summary>Hint 1: CI/CD</summary>

- Check the secrets in the workflow
- Look at job order and dependencies
- Verify action versions
- Look for race conditions

</details>

<details>
<summary>Hint 2: Docker</summary>

- How many layers does the image have?
- What user is running inside the container?
- Where are the credentials stored?
- Does the healthcheck work?

</details>

<details>
<summary>Hint 3: Kubernetes</summary>

- Are resource limits set?
- Are probes configured correctly?
- Does RBAC follow least privilege?
- Are there secrets inside ConfigMaps?

</details>

<details>
<summary>Hint 4: Terraform</summary>

- Are variables validated?
- Are there hardcoded resources?
- Are the modules well structured?
- Is the remote state backend missing?

</details>

## 🏆 Bonus Points

- Implement automated security scanning
- Create an automatic rollback pipeline
- Add monitoring with Prometheus queries
- Implement a GitOps pattern
- Cost optimization for GCP resources
- Disaster recovery plan
