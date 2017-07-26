# Sivigik

Source du site [Sivigik](http://sivigik.com).

## Deployer l'environnement de développement.

### Sous Linux
Vous aurez besoin de python, pip et virtualenv.

Si vous avez déjà python et pip :

    pip install --user virtualenv

Ensuite rendez-vous dans votre répertoire de travail puis,

    mkdir Sivigik
    cd Sivigik
    virtualenv ./

Vous pouvez dès à présent activer l'environnement (il faudra le faire à chaque
fois que vous travaillez sur le projet).

    source bin/activate

Clonez le projet.

    git clone https://github.com/Klafyvel/Sivigik.git

Rendez vous dans le dossier téléchargé puis téléchargez les dépendances. Grâce
à virtualenv ces dépendances seront installées localement et ne viendront pas
polluer votre système.

    cd Sivigik
    pip install -r requirements.txt

Mettre à jour la base de données et créer le super-utilisateur.

    ./manage.py migrate
    ./manage.py createsuperuser

Vous pouvez maintenant lancer le serveur de développement.

    ./manage.py runserver

Le site est disponible sur http://127.0.0.1:8000/.

### Sous Windows (en partant de zéro !)

1. Télécharger [python3](https://www.python.org/) (cocher "add python to PATH");
2. Lancer `cmd.exe`;
3. Installer virtualenv;
   ```shell 
    pip install virtualenv
    ```
4. Installer git (si vous voulez modifier le code) [ici](https://desktop.github.com/) par exemple;
5. Cloner `https://github.com/Klafyvel/Sivigik.git` ou téléchargez simplement l'archive [ici](https://github.com/klafyvel/Sivigik) si vous n'avez pas git;
6. Depuis la ligne de commande, aller dans le répertoire qui contient Sivigik;
7. Créer l'environnement de travail;
   ```shell
   virtualenv env_sivigik
   ```
8. L'activer;
   ```shell
   env_sivigik\Scripts\activate.bat
   ```
9. Se rendre dans le répertoire du site et télécharger les dépendances;
   ```shell
   cd Sivigik
   pip install -r requirements.txt
   ```
10. On s'occupe de la base de données;
    ```shell
    python manage.py migrate
    ```
11. On crée un super-utilisateur;
    ```shell
    python manage.py createsuperuser
    ```
12. Enfin, lancer le serveur.
    ```shell
    python manage.py runserver
    ```

Le site est disponible sur http://127.0.0.1:8000/.
	
Lorsque vous souhaitez travailler sur le site, seule les étapes 8 et 12 sont à répéter. N'oubliez pas de mettre à jour votre dépôt local de temps à autres pour travailler sur la dernière version !
