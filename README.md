# ToDo-List Challenge

Esta app crea una API con Django Rest Framework que provee una To-do list en la que se puede crear, borrar y marcar tareas como completadas, así como poder ver una lista de todas las tareas juntas y filtrarlas según su fecha de creación o el contenido de las mismas.

## Cómo funciona
La API tiene un objeto:<br>
-TODO: Contiene el título de la tarea, así como su descripción, status de compleción y fecha de creación.<br>
<br>
En http://127.0.0.1:8000/todo/ aparece la lista de tareas de esta manera:
```
[
    {
        "id": 1,
        "title": "Finish challenge",
        "description": "Finish the app",
        "completed": true,
        "date": "2021-01-08"
    },
    {
        "id": 2,
        "title": "Learn about the needed requirements",
        "description": "Search online",
        "completed": false,
        "date": "2021-01-08"
    }
]
```
En la parte posterior se pueden agregar nuevas tareas y configurar su título, descripción y status de compleción. Al ser creadas, las tareas tedrán automáticamente asignadas la fecha de creación de las mismas. <br><br>
Las tareas pueden ser filtradas según su contenido o la fecha de elaboración.<br><br>
Se puede acceder a una tarea en particular a través de su número de id: http://127.0.0.1:8000/todo/1/, por ejemplo. Allí se puede eliminar la tarea si así lo desea.

## Setup
1. Clonar el repositorio:
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
(myvenv) $ pip install -r requirements.txt
```
4. Realizar migraciones:
```
(myvenv) $ python manage.py migrate
```
5. Iniciar el servidor:
```
(myvenv)$ python manage.py runserver
```
6. Navegar a http://127.0.0.1:8000/todo/

## Tests
Para correr los tests tipear en la consola dentro del projecto:
```
(myvenv)$ py manage.py test
```
