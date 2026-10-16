# Módulo PDF - Servidor de Inventario

## Ejecución Local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt uvicorn
uvicorn main:app --reload
```

Servidor accesible en `http://127.0.0.1:8000`.

## Despliegue

Sube este repositorio a Vercel estableciendo la carpeta `pdfs-main` o la raíz como directorio de ejecución.
