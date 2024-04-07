

# tache id        Date de début               Durée         date de fin  tache parent depend de
# tache 1        8 septembre                   2j           10 septembre       -              -
# tache 2        10 septembre                  5j           15 septembre       -              1
# tache 2.1      10 septembre                  1j           11 septembre        2             1
# tache 2.2      11 septembre                  4j           14 septembre        2             1
# tache 3              3                       7j
# tache 4              10                      20j


# prendre le projet
# function (request, project_id)
# crée un tableau a 6 colonnes avec le nom des taches leurs date de début, leurs durée ainsi que la date de démarrage et la dépendace de la tache
# chercher toutes les taches qui appartient au projet id et les mettres dans le tableau avec tous leurs attribut ( 6 collones)
# vérifié si les taches ont des sous taches
# si elles ont des sous taches, elles seront ordonnées avec sa ou ses sous taches avec dans le champ tache parent la tache du parent.
# une fois les sous taches ordonnées avec leurs taches nous allons trier les taches par dépendances
# les taches parentes seront aussi une dépendence, qu'il faudra ajouter aux champs dépendance.
# si une taches a une dépendence alors l'ajouter la tache après le nom de la tache de la dépendance
# après le trie des dépendances nous allons calculer les dates avec leurs durrée pour obtenir la date de fin de chaque tache.


import datetime
from django.shortcuts import get_object_or_404
from .models import Task, Project


def gantt_chart(project_id):
    # # prendre le projet en cours
    project = get_object_or_404(Project, pk=project_id)

    # chercher toutes les taches qui appartient au projet id
    tasks = Task.objects.filter(project=project).order_by('start_date')

    task_details = {}
    gantt_chart = []

    # chercher toutes les taches qui appartient au projet id et les mettres dans le tableau avec tous leurs attribut
    # ( 6 collones)
    for task in tasks:
        task_id = task.id
        start_date = task.start_date
        duration = task.duration
        end_date = start_date + datetime.timedelta(days=duration)  # calculer la date de fin
        parent_task = task.parent_task_id
        depend_on_tasks = task.depend_on.all()

        if depend_on_tasks.exists():

            max_depend_end_date = max(
                task_details.get(depend_task.id, {'end_date': start_date})['end_date'] for depend_task in
                depend_on_tasks)
            task_start_date = max(start_date, max_depend_end_date)
        else:
            task_start_date = start_date
        # crée un tableau a 6 colonnes avec le nom des taches leurs date de début, leurs durée ainsi que la date de
        # démarrage et la dépendace de la tache
        task_details[task_id] = {
            'task_name': task.task_name,
            'start_date': task_start_date,
            'end_date': end_date,
            'duration': duration,
            'parent_task': parent_task,
            'depend_on': list(depend_on_tasks.values_list('id', flat=True))
        }
        gantt_chart.append(
            [task_id, task_start_date, duration, end_date, parent_task, task_details[task_id]['depend_on']])

    # trier les taches par dépendances
    gantt_chart.sort(key=lambda x: (x[5], task_details[x[0]]['start_date']))


    for task_id, start_date, duration, end_date, parent_task, dependencies in gantt_chart:
        if parent_task:

            parent_start_date = task_details[parent_task]['start_date']
            task_details[task_id]['start_date'] = max(start_date, parent_start_date)

        task_details[task_id]['end_date'] = task_details[task_id]['start_date'] + datetime.timedelta(days=duration)

    max_end_date = max(task_details[task_id]['end_date'] for task_id in task_details)

    return gantt_chart, max_end_date
