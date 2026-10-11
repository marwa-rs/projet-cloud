variable "aws_region" {
  description = "Region AWS (Paris)"
  type        = string
  default     = "eu-west-3"
}

variable "aws_profile" {
  description = "Profil AWS CLI utilise par Terraform"
  type        = string
  default     = "terraform"
}

variable "project_name" {
  description = "Nom du projet "
  type        = string
  default     = "projet-cloud"
}

variable "instance_type" {
  description = "Type d'instance EC2 "
  type        = string
  default     = "t3.small"
}

variable "my_ip_cidr" {
  description = "Ton IP publique au format CIDR"
  type        = string

  validation {
    condition     = can(cidrhost(var.my_ip_cidr, 0)) && endswith(var.my_ip_cidr, "/32")
    error_message = "my_ip_cidr doit etre une seule adresse IP au format x.x.x.x/32."
  }
}

variable "ssh_public_key_path" {
  description = "Chemin de la cle SSH publique"
  type        = string
  default     = "~/.ssh/projet-cloud.pub"
}

variable "repo_url" {
  description = "Depot Git a deployer"
  type        = string
  default     = "https://github.com/marwa-rs/projet-cloud.git"
}

variable "grafana_admin_password" {
  description = "Mot de passe admin Grafana sur AWS"
  type        = string
  sensitive   = true

  validation {
    condition     = length(var.grafana_admin_password) >= 12 && !strcontains(var.grafana_admin_password, "'")
    error_message = "Le mot de passe doit faire au moins 12 caracteres et ne pas contenir d'apostrophe."
  }
}
