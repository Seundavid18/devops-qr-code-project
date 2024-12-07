location           = "East US"
resource_group_name = "rg-qr-code"

vnet_name          = "qr-code-aks-vnet"
vnet_address_space = "10.1.0.0/16"
subnet_name        = "qr-code-aks-subnet"
subnet_prefix      = "10.1.1.0/24"

aks_cluster_name   = "qr-code-aks-cluster"
dns_prefix         = "qrcodeakscluster"
node_pool_name     = "qrcodepool"
node_count         = 3
node_vm_size       = "Standard_DS3_v2"
