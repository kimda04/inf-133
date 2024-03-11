from zeep import Client

try:
    client = Client("http://localhost:8000")
    result = client.service.Saludar(nombre="Dana")
    print(result)
except Exception as e:
    print(f"Error: {e}")
