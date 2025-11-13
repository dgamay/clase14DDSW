import requests

STUDENT_SERVICE_URL = "http://student-service:3000/students"

def get_students_summary():
    try:
        response = requests.get(STUDENT_SERVICE_URL, timeout=5)
        response.raise_for_status()
        students = response.json()
        return {
            "total_students": len(students),
            "student_names": [s["name"] for s in students],
            "source": STUDENT_SERVICE_URL,
        }
    except requests.RequestException as e:
        return {"error": f"Failed to connect to student-service: {e}"}
