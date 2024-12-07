output "aks_cluster_name" {
  description = "The name of the AKS cluster."
  value       = azurerm_kubernetes_cluster.aks_cluster.name
}

output "aks_fqdn" {
  description = "The fully qualified domain name (FQDN) of the AKS cluster."
  value       = azurerm_kubernetes_cluster.aks_cluster.fqdn
}

output "kube_config" {
  description = "The raw kubeconfig for the AKS cluster."
  value       = azurerm_kubernetes_cluster.aks_cluster.kube_config_raw
}