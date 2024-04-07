from django.core.management.base import BaseCommand
from django.utils import timezone
from authentification.models import User
from project_app.models import Project, Task
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Import sample data into the database'

    def handle(self, *args, **kwargs):
        # Création des utilisateurs
        username = 'toto'
        password = 'azerty123!'
        email = 'toto@toto.fr'
        user_role = 'MANAGER'
        toto = User.objects.create_user(username=username, password=password, email=email, user_role=user_role)
        toto.save()
        group_name = user_role
        group = Group.objects.get(name=group_name.lower())
        group.user_set.add(toto)

        username = 'tati'
        password = 'azerty123!'
        email = 'tati@tati.fr'
        user_role = 'EMPLOYER'
        tati = User.objects.create_user(username=username, password=password, email=email, user_role=user_role)
        tati.save()
        group_name = user_role
        group = Group.objects.get(name=group_name.lower())
        group.user_set.add(tati)

        # Création du projet d'aviation

        aviation_project = Project.objects.create(
            project_name='Projet Aviation',
            start_date=timezone.now(),
            delivery_date=timezone.now() + timezone.timedelta(days=30),
            status='planned',
            project_manager=toto
        )

        # Création des tâches pour le projet d'aviation
        task1 = Task.objects.create(
            task_name='Préparation du plan de vol',
            description='Élaborer un plan de vol détaillé pour le vol d\'essai',
            priority='high',
            start_date=timezone.now(),
            duration=5,
            status='planned',
            project=aviation_project,
            progress_reporter=tati
        )

        task2 = Task.objects.create(
            task_name='Maintenance de l\'avion',
            description='Effectuer la maintenance préventive sur l\'avion',
            priority='medium',
            start_date=timezone.now(),
            duration=3,
            status='ongoing',
            project=aviation_project,
            progress_reporter=tati
        )

        task3 = Task.objects.create(
            task_name='Vol d\'essai',
            description='Effectuer un vol d\'essai avec le pilote',
            priority='high',
            start_date=timezone.now() + timezone.timedelta(days=10),
            duration=2,
            status='planned',
            project=aviation_project,
            progress_reporter=tati
        )

        task4 = Task.objects.create(
            task_name='Rapport de vol',
            description='Générer un rapport détaillé sur le vol d\'essai effectué',
            priority='medium',
            start_date=timezone.now() + timezone.timedelta(days=15),
            duration=4,
            status='planned',
            project=aviation_project,
            progress_reporter=tati
        )

        # Affectation des tâches aux utilisateurs
        task1.assigned_to.add(tati)
        task2.assigned_to.add(tati)
        task3.assigned_to.add(tati)
        task4.assigned_to.add(tati)

        self.stdout.write(self.style.SUCCESS('Projet et tâches d\'aviation générés avec succès'))

        # Création du projet automobile
        automobile_project = Project.objects.create(
            project_name='Projet Automobile',
            start_date=timezone.now(),
            delivery_date=timezone.now() + timezone.timedelta(days=45),
            status='planned',
            project_manager=toto
        )
        # Création des tâches pour le projet automobile
        task1 = Task.objects.create(
            task_name='Conception du prototype',
            description='Développer le prototype de la nouvelle voiture',
            priority='high',
            start_date=timezone.now(),
            duration=10,
            status='ongoing',
            project=automobile_project,
            progress_reporter=tati
        )

        task2 = Task.objects.create(
            task_name='Tests de sécurité',
            description='Effectuer des tests de sécurité sur le prototype',
            priority='medium',
            start_date=timezone.now() + timezone.timedelta(days=10),
            duration=5,
            status='planned',
            project=automobile_project,
            progress_reporter=tati
        )

        task3 = Task.objects.create(
            task_name='Optimisation du moteur',
            description='Optimiser les performances du moteur de la voiture',
            priority='high',
            start_date=timezone.now() + timezone.timedelta(days=20),
            duration=7,
            status='planned',
            project=automobile_project,
            progress_reporter=tati
        )

        task4 = Task.objects.create(
            task_name='Rapport final',
            description='Rédiger le rapport final sur le projet automobile',
            priority='medium',
            start_date=timezone.now() + timezone.timedelta(days=35),
            duration=5,
            status='planned',
            project=automobile_project,
            progress_reporter=tati
        )

        # Affectation des tâches aux utilisateurs
        task1.assigned_to.add(tati)
        task2.assigned_to.add(tati)
        task3.assigned_to.add(tati)
        task4.assigned_to.add(tati)

        self.stdout.write(self.style.SUCCESS('Projet et tâches automobiles générés avec succès'))
