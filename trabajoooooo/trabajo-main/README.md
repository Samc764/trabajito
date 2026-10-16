# Sistema de Gestión e Informes de Productos

Proyecto enfocado en la consulta de inventario y generación dinámica de reportes en formato PDF mediante FastAPI y Jinja2.

## Características

- Vista principal con indicador de existencias.
- Tabla detallada de artículos por sección.
- Generación y descarga de reporte PDF sin requerir motor gráfico externo.

## Instrucciones de Instalación y Uso

1. Acceder al directorio del proyecto:
   ```bash
   cd pdfs-main
   ```
2. Crear y activar el entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Instalar librerías necesarias:
   ```bash
   pip install -r requirements.txt uvicorn
   ```
4. Iniciar el servidor local:
   ```bash
   uvicorn main:app --reload
   ```
5. Navegar a `http://127.0.0.1:8000`.

## Endpoints Disponibles

- `GET /`: Panel de bienvenida.
- `GET /report`: Vista de la lista completa de artículos.
- `GET /report/pdf`: Descarga del archivo PDF generado (`inventario.pdf`).

## Despliegue en Vercel

Configurado mediante el archivo `vercel.json` tanto en la raíz como en el directorio interno para ejecución en entorno serverless.
