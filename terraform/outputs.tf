output "public_ip" {
  description = "IP publique du serveur"
  value       = aws_instance.app.public_ip
}

output "app_url" {
  value = "http://${aws_instance.app.public_ip}:5000"
}

output "health_url" {
  value = "http://${aws_instance.app.public_ip}:5000/health"
}

output "grafana_url" {
  value = "http://${aws_instance.app.public_ip}:3000"
}

output "ssh_command" {
  value = "ssh -i ~/.ssh/projet-cloud ubuntu@${aws_instance.app.public_ip}"
}
