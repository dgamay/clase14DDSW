from fastapi import FastAPI
from app.services.student_client import get_students_summary

app = FastAPI(title="Report Service", version="1.0.0")

@app.get("/reports/summary") #esta es la rut de entrada a la aplicacion 
def summary():
    """
    Genera un informe simple que resume los datos de los estudiantes
      obtenidos del student-service (microservicio en Node.js)
    """
    return get_students_summary()

''' hola mundo '''