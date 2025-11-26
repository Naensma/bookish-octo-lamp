provider "google" {
  project = "hardcoded-project"
  region  = "us-central1"
}

resource "google_container_cluster" "primary" {
  name     = "primary-cluster"
  location = "us-central1"
  initial_node_count = 1
}

