# cbm-upv-cto-pf-django

1. Instalar Python.
2. Descargar el repositorio.
```bash
git clone https://github.com/cristianbm-hub/cbm-upv-cto-pf-django
```
3. Ubicarse en el directorio
```bash
cd cristianbm-hub/cbm-upv-cto-pf-django
```
4. Instalar las dependendias.
```bash
pip install --upgrade -r requirements.txt
```
5. Aplicar las migraciones
```bash
python manage.py migrate
```
6. Crear un superusuario para administrar la base de datos
```bash
python manage.py createsuperuser
```
Seguir las instrucciones para incluir las credenciales
7. Arrancar Django
```bash
python manage.py runserver
```
8. Acceder al panel de administración para crear soldados:
http://127.0.0.1:8000/admin/


