resource "google_container_node_pool" "default" {
  name       = "default-pool"
  cluster    = var.cluster_name
  node_count = 1
}
