terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_ecr_repository" "todo_repo" {
  name = "todo-api"
  
  tags = {
    Project = "todo-app"
    Cost    = "free"
  }
}

output "ecr_repository_url" {
  value = aws_ecr_repository.todo_repo.repository_url
}
