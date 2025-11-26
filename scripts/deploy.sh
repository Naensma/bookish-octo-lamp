#!/bin/bash

echo "Starting deployment..."
kubectl apply -f k8s/
echo "Deployment finished"
exit 0
