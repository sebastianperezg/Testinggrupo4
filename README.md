# Testinggrupo4

Instrucciones para instalar el sistema de facturación de la farmacia

Requisitos previos:

Antes de instalar el sistema, es necesario tener instalado Python y pip (el administrador de paquetes de Python) en el equipo. Si no los tienes instalados, puedes descargarlos desde la página oficial de Python: https://www.python.org/downloads/ 

Instalación:

1. Abre una terminal (en Windows: CMD o PowerShell).
2. Ejecuta el siguiente comando para actualizar pip: 
   python.exe -m pip install --upgrade pip

Este comando actualiza la versión de pip a la última disponible.

3. Ejecuta el siguiente comando para instalar django-crispy-forms y crispy-bootstrap4:
   pip install django-crispy-forms crispy-bootstrap4

Estos paquetes son necesarios para el correcto funcionamiento del sistema.

4. Descarga e instala Django siguiendo las instrucciones de la página oficial: https://www.djangoproject.com/download/

5. Descarga y extrae el archivo .rar que contiene la carpeta del proyecto Django.

6. Instala la version Professional de PyCharm desde la página oficial: https://www.jetbrains.com/pycharm/download/

7. Abre PyCharm y crea una cuenta dentro de sus opciones, luego selecciona "trial" para probar PyCharm Professional durante 30 dias.

8. Selecciona "Open" desde el menú "File".

8. Navega hasta donde descargaste la carpeta del proyecto y selecciónala.

9. Ejecuta el proyecto haciendo clic en el botón "Run" en la barra de herramientas de PyCharm.

10. Ejecuta el siguiente comando para crear el servidor mysql en pycharm:
    python manager.py migrate


