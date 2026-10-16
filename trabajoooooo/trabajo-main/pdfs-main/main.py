from io import BytesIO
from pathlib import Path
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, Response
from fastapi.templating import Jinja2Templates
from xhtml2pdf import pisa

DIR_BASE = Path(__file__).resolve().parent
plantillas = Jinja2Templates(directory=DIR_BASE / "templates")

api = FastAPI(title="Gestor de Inventario")

ARTICULOS = [
    {"codigo": 1, "denominacion": "Laptop Pro 14", "seccion": "Computo", "costo": 18999.00, "unidades": 12},
    {"codigo": 2, "denominacion": 'Monitor 27" 4K', "seccion": "Pantallas", "costo": 7499.50, "unidades": 30},
    {"codigo": 3, "denominacion": "Teclado Mecanico", "seccion": "Accesorios", "costo": 1299.99, "unidades": 85},
    {"codigo": 4, "denominacion": "Mouse Inalambrico", "seccion": "Accesorios", "costo": 499.00, "unidades": 120},
    {"codigo": 5, "denominacion": "Webcam Full HD", "seccion": "Video", "costo": 899.00, "unidades": 45},
]

@api.get("/", response_class=HTMLResponse)
async def inicio(req: Request) -> HTMLResponse:
    return plantillas.TemplateResponse(
        request=req,
        name="index.html",
        context={"encabezado": "Catalogo de Articulos", "total_items": len(ARTICULOS)},
    )

@api.get("/report", response_class=HTMLResponse)
async def ver_tabla(req: Request) -> HTMLResponse:
    return plantillas.TemplateResponse(
        request=req,
        name="report.html",
        context={
            "encabezado": "Catalogo de Articulos",
            "articulos": ARTICULOS,
            "es_previsualizacion": True,
        },
    )

@api.get("/report/pdf")
def exportar_documento() -> Response:
    codigo_html = plantillas.get_template("report.html").render(
        encabezado="Catalogo de Articulos",
        articulos=ARTICULOS,
        es_previsualizacion=False,
    )
    flujo_bytes = BytesIO()
    estado = pisa.CreatePDF(src=codigo_html, dest=flujo_bytes)
    if estado.err:
        raise HTTPException(status_code=500, detail="Fallo en procesamiento de archivo")
    return Response(
        content=flujo_bytes.getvalue(),
        media_type="application/pdf",
        headers={"Content-Disposition": 'attachment; filename="inventario.pdf"'},
    )

app = api
