variable "aws_access_key" {
  description = "AWS Access Key"
  type        = string
  sensitive   = true
}

variable "aws_secret_key" {
  description = "AWS Secret Key"
  type        = string
  sensitive   = true
}

variable "aws_region" {
  description = "AWS Region"
  type        = string
  default     = "us-east-1"
}

variable "elastic_ip" {
  description = "Elastic IP publica ya asignada"
  type        = string
  default     = "78.13.184.200"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.medium"
}

variable "project_name" {
  description = "Nombre del proyecto"
  type        = string
  default     = "acuaponia-monitor"
}

variable "github_repo" {
  description = "URL del repositorio"
  type        = string
  default     = "https://github.com/upmh-andresbardales/proyecto-responsabilidad.git"
}
