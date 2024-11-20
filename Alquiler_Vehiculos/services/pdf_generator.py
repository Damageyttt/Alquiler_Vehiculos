from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def generar_resumen_pdf(vehiculos, archivo_pdf):
    "Genera un archivo PDF con el resumen de vehículos"
    doc = SimpleDocTemplate(archivo_pdf, pagesize=letter)
    elementos = []

    
    data = [["Tipo", "Matrícula", "Kilómetros", "Estado"]]
    for vehiculo in vehiculos:
        estado = "Disponible" if vehiculo.estado else "Alquilado"
        color = colors.green if vehiculo.estado else colors.red
        data.append([vehiculo.__class__.__name__, vehiculo.matricula, vehiculo.km, estado])

    
    tabla = Table(data)
    estilo = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
    ])

    
    for i, fila in enumerate(data[1:], start=1):
        color = colors.green if fila[3] == "Disponible" else colors.red
        estilo.add("TEXTCOLOR", (0, i), (-1, i), color)

    tabla.setStyle(estilo)
    elementos.append(tabla)

    
    doc.build(elementos)
