# Invera ToDo-List Challenge (Python/Django Jr-SSr)

Esta app crea una API con Django Rest Framework que provee una To-do list en la que se puede crear, borrar y marcar tareas como completadas, así como poder ver una lista de todas las tareas juntas y filtrarlas según su fecha de creación o el contenido de las mismas.

## Cómo funciona
La API tiene un objeto:<br>
-TODO: Contiene el título de la tarea, así como su descripción, status de compleción y fecha de creación.

## Setup
1. Primero hay que clonar el repositorio:
```
$ git clone https://github.com/micaelagimenez/todo-challenge.git
$ cd todo-challenge
```
2. Crear el entorno virtual para instalar las dependencias y activarlo:
```
$ python -m venv myvenv
$ myvenv\Scripts\activate
```
3. Instalar las dependencias:
```
pip install -r requirements.txt
```
4. Iniciar el servidor.
```
(myvenv)$ python manage.py runserver
```
5. Navegar a http://127.0.0.1:8000/todo/

## Tests
Para correr los tests tipear en la consola dentro del projecto:
```
(myvenv)$ py manage.py test
```
