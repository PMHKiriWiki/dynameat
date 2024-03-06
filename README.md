# Instrucciones
1. Descargar el proyecto del repositorio
2. En la raiz hay un fichero Makefile con una gran cantidad de comandos. Se llaman con make [nombre_comnado] (p.e make up)
3. Hacer make up
4. Una vez levantados los contendores, si se quiere observar la información en el admin de django, ejecutar make createsuperuser. Introducir los valores que solicita por prompt y acceder a localhost:8000/admin para ver que tenemos acceso.
5. Al inicio tendremos cargados unos Observtories y Devices por defecto. Serán lo que aparecen en el fichero de avistamientos. Esto se carga a través de fixtures.
6. Si no se quiere ver el admin, acceder directamente a localhost:8000/docs y se abrirá Swagger con las endpoints definidos. Se ha hecho un ejemplo sencillo de algunos de los enpodints mas relevantes como el de consulta de asteroides o el de carga de el fichero csv.
7. Para la prueba del endpoint /sightings/upload_file se extrae el fichero de una carpeta del proyecto ya que por limitaciones de tiempo no se ha realizado la integración con el front.
8. Al llamar a este endpoint se podra consultar la api de asteroides para ver que se ha cargado correctamente.
9. Para ejecutar los tests usar el comando make run-tests que se encuentra en el Makefile. **Hay que encontrarse en la raiz del proyecto para que funcionen los comando de make**