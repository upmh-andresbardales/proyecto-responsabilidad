output "instance_id" {
  description = "ID de la instancia EC2"
  value       = aws_instance.app.id
}

output "public_ip" {
  description = "IP publica (Elastic IP)"
  value       = aws_eip.app.public_ip
}

output "ssh_command" {
  description = "Comando SSH para conectarse"
  value       = "ssh -i infra/${var.project_name}.pem ubuntu@${aws_eip.app.public_ip}"
}

output "dashboard_url" {
  description = "URL del frontend dashboard"
  value       = "http://${aws_eip.app.public_ip}:3000"
}

output "api_url" {
  description = "URL de la API (Swagger)"
  value       = "http://${aws_eip.app.public_ip}:8000/docs"
}

output "emqx_url" {
  description = "URL del dashboard EMQX"
  value       = "http://${aws_eip.app.public_ip}:18084"
}

output "private_key_path" {
  description = "Ruta de la llave privada generada"
  value       = local_file.private_key.filename
}
