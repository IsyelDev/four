from fpdf import FPDF
import os

# Datos del proyecto
proyecto = "Naruto"
horas_estimadas = 15
valor_hora = 10
tiempo_estimado = 12
costo_total = horas_estimadas * valor_hora

class PDF(FPDF):
    def header(self):
        if os.path.exists("isyel.png"):
            self.image("isyel.png", x=75, y=10, w=60)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", align='C')

    def contenido_presupuesto(self):
        self.set_y(120)

        # Centrar la tabla horizontalmente
        tabla_ancho = 140  # 90 + 50 mm
        margen_izquierdo = (210 - tabla_ancho) / 2  # A4 = 210 mm
        self.set_x(margen_izquierdo)

        # Título
        self.set_font("Arial", 'B', 15)
        self.cell(tabla_ancho, 10, f"Presupuesto del Proyecto: {proyecto}", ln=True, align='C')
        self.ln(10)
        self.set_x(margen_izquierdo)

        # Tabla
        self.set_font("Arial", "", 14)
        self.set_fill_color(200, 200, 200)
        self.cell(90, 10, "Descripción", 1, 0, 'C', True)
        self.cell(50, 10, "Valor", 1, 1, 'C', True)

        self.set_x(margen_izquierdo)
        self.cell(90, 10, "Horas estimadas", 1)
        self.cell(50, 10, str(horas_estimadas), 1, 1)

        self.set_x(margen_izquierdo)
        self.cell(90, 10, "Valor por hora ($)", 1)
        self.cell(50, 10, f"${valor_hora}", 1, 1)

        self.set_x(margen_izquierdo)
        self.cell(90, 10, "Tiempo estimado (días)", 1)
        self.cell(50, 10, f"{tiempo_estimado}", 1, 1)

        self.set_x(margen_izquierdo)
        self.set_font("Arial", "B", 12)
        self.cell(90, 10, "Costo total ($)", 1)
        self.cell(50, 10, f"${costo_total}", 1, 1)

# Crear y guardar PDF
pdf = PDF()
pdf.add_page()
pdf.contenido_presupuesto()
pdf.output("presupuesto.pdf")
print("📄 PDF generado con tabla centrada horizontalmente.")
