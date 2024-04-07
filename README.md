procédure d'installation à la main

sudo apt update
sudo apt install -y python3 python3-venv python3-pip
python3 -m venv myenv
source myenv/bin/activate
git clone https://github.com/mikamttr/django_project.git
cd django_project
git checkout feature/global
python3 -m pip install django
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py import_data
# si ça fail c'est que c'est déja importé, il y'aura une erreur au niveau des user disant qu'ils sont unique
python3 manage.py runserver
# si ça failt c'est que le port et déja utilisé


J'ai aussi crée un script cependant il est nécessaire d'avoir crée son environnement virtual avant car sinon cela ne fonctionne pas car je n'ai pas réussi a activer un environnement par script
pour que le script puisse être éxécuter il faut faire un chmod +x path/script.sh





##########################################SCRIPT##########################################################

#!/bin/bash
#le script fonctionne uniquement si un environnement virtuel est activé merci d'activé votre environemment virtuel : 
#python3 -m venv NomEnvironnement
#source NomEnvironnement/bin/activate

function check_error {
    if [ $? -ne 0 ]; then
        echo "Erreur : $1"
        exit 1
    fi
}


sudo apt update
check_error "Échec de la mise à jour des paquets"
sudo apt install -y python3 python3-venv python3-pip
check_error "Échec de l'installation de Python et pip"


git clone https://github.com/mikamttr/django_project.git
check_error "Échec du clonage du dépôt Git"
cd django_project
check_error "Répertoire du projet introuvable"


git checkout feature/global
check_error "Échec du changement de branche Git"


python3 -m pip install django
check_error "Échec de l'installation de Django"


python3 manage.py makemigrations
check_error "Échec de la création des migrations"
python3 manage.py migrate
check_error "Échec de l'application des migrations"



python3 manage.py runserver
