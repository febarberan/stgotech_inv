from locust import HttpUser, task, constant, SequentialTaskSet

class HelloWorldUser(HttpUser):
    @task
    def test(self):
        self.client.get("/buscar_productos_inicio/?n=")


# class ComatFormTaskSet(SequentialTaskSet):
#     @task
#     def post_comat_form(self):
#         payload = {
#             'stdf_pk': 123,
#             'awb': 'AWB123',
#             'hawb': 'HAWB123',
#             'num_manifiesto': '1234',
#             'corr_interno': 'CI123',
#             'pcs': 10,
#             'peso': 50.5,
#             'f_control': '2023-11-10T12:00',  # Ajusta la fecha y hora según el formato que acepta tu formulario
#             'f_manifiesto': '2023-11-10T12:00',
#             'f_recepcion': '2023-11-10T12:00',
#             'f_stdf': '2023-11-10',
#             'fob': 1000.50,
#             'flete': 150.75,
#             'seguro': 25.30,
#             'observaciones': 'Alguna observación',
#             'prioridad': 'ALTA',
#             'bodega_fk': 1,  # Reemplaza con el ID correcto de tu Bodega
#             'origen_fk': 1,  # Reemplaza con el ID correcto de tu Origen
#             'compania_fk': 1,  # Reemplaza con el ID correcto de tu Compañia
#         }

#         headers = {'Content-Type': 'application/x-www-form-urlencoded'}

#         # Realiza la solicitud POST al formulario Django
#         self.client.get('/comat', data=payload, headers=headers)

# class MyUser(HttpUser):
#     wait_time = constant(1)  # Tiempo de espera constante entre las tareas
#     tasks = [ComatFormTaskSet]


