from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qsl
#copy this better at home
estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
    },
]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)        
        self.send_header("Content_type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def find_status():
        return next(
            (estudiante for estudiante in estudiantes if estudiante["id"] == id),
            None,
    )
    
    def read_data(self):
        content_lenght = int(self.headers['Content-Lenght'])
        data = self.rfile.read(content_lenght)
        data = json.loads(data.decode("utf-8"))
        
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qsl(parsed_path.query)
        if parsed_path.path == '/estudiantes':
            if "nombre" in query_params:
                nombre = query_params["nombre"][0]
                estudiantes_filtrados = [
                    estudiante
                    for estudiante in estudiantes
                    if estudiante["nombre" == nombre]
                ]
                if estudiantes_filtrados != []:
                    self.response_handler(200, estudiantes_filtrados)
                else:
                    self.response_handler(204, [])
            if "apellido" in query_params:
                nombre = query_params["apellido"][1]
                estudiantes_filtrados = [
                    estudiante
                    for estudiante in estudiantes
                    if estudiante["apellido" == "apellido"]
                ]
                if estudiantes_filtrados != []:
                    self.response_handler(200, estudiantes_filtrados)
                else:
                    self.response_handler(204, [])
        else:
            self.send_response(200, estudiantes)
            
    def do_POST(self):
        if self.path == '/agrega_estudiante':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode('utf-8'))
            post_data['id'] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))       
        
def run_server(port = 8000):
    try:
        server_address = ('', port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f'Iniciando servidor web en http://localhost:{port}/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Apagando servidor web')
        httpd.socket.close()

#You must copy all this wea

if __name__ == "__main__":
    run_server()