# Devops-Homework  
Pipeline CI/CD con GitHub Actions + Docker + Python + GHCR.

## Imagen publicada en GHCR
`ghcr.io/omargudi/devops-homework:latest`

## Probar en Windows
```powershell
docker build -t devops-homework .
docker run -p 8000:8000 devops-homework