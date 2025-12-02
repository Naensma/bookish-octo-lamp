# DevOps Challenge - The Disaster Recovery

## Context

This project was originally created by a junior developer who was eager to deliver fast, but missed several best practices and introduced critical issues along the way. Now, you’ve been brought in as the experienced DevOps engineer to rescue the codebase.

**Your mission:** review the work, identify what went wrong, and fix all the problems to make the system robust, secure, and production-ready.

## First Steps
- Download repo

    ```bash
    git clone <repo_url>
    ```
- Understand [Objectives](#objectives) and [Evaluation Criteria](#evaluation-criteria)
- Start checking the code and follow objectives
- Enjoy!

## Suggestion - Hints
- First and most importantly: **Feel free to ask question** and **be wrong about things**.
- If you feel blocked just **start with what you think its going to be easier** or what you think you are best with.

- If you feel that you need to test things out locally check this [**section**](#local-development---installation-guides)

## Objectives

### CI/CD Pipeline
- Fix GitHub Actions pipeline
- Dockerize the application
- Remove security vulnerabilities
- Optimize build time and image size

### Kubernetes
- Fix all manifests to be production-ready
- Implement RBAC correctly using the principle of least privilege
- Configure probes, resources, and security contexts
- Solve networking issues between services

### IaC & Automation
- Fix Terraform code
- Make Terraform code modular
- Create automation scripts for validation and deployment
- Implement pre-deployment security validations
- Document the proposed architecture

## Evaluation Criteria

| Category | Explanation |
|-----------|-------------------|
| **Identification** | Did you find all critical issues? |
| **Technical Solution** | Did you implement correct and efficient fixes? |
| **Security** | Did you eliminate vulnerabilities? Did you apply hardening? |
| **Best Practices** | Did you follow industry standards? |
| **Documentation** | Are your decisions clearly explained? |

## Local development - Installation Guides
- [Docker](https://docs.docker.com/engine/install/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Act](https://nektosact.com/installation/index.html)
