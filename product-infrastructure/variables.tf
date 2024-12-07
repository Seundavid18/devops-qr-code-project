# General Settings
variable "location" {
  description = "The location where the resources will be created."
  default     = "East US"
}

variable "resource_group_name" {
  description = "The name of the resource group where resources will be created."
  default     = "aks-resource-group"
}

# Virtual Network Settings
variable "vnet_name" {
  description = "The name of the virtual network."
  default     = "aks-vnet"
}

variable "vnet_address_space" {
  description = "The address space for the virtual network."
  default     = "10.0.0.0/16"
}

variable "subnet_name" {
  description = "The name of the subnet."
  default     = "aks-subnet"
}

variable "subnet_prefix" {
  description = "The subnet address prefix."
  default     = "10.0.1.0/24"
}

# AKS Settings
variable "aks_cluster_name" {
  description = "The name of the Azure Kubernetes Service cluster."
  default     = "aks-cluster"
}

variable "dns_prefix" {
  description = "The DNS prefix for the AKS cluster."
  default     = "akscluster"
}

variable "node_pool_name" {
  description = "The name of the AKS default node pool."
  default     = "nodepool1"
}

variable "node_count" {
  description = "The number of nodes in the default node pool."
  default     = 2
}

variable "node_vm_size" {
  description = "The size of the VMs in the default node pool."
  default     = "Standard_DS2_v2"
}
