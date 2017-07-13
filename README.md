# Sivigik

Source du site [Sivigik](http://sivigik.com).

## Deployer l'environnement de développement.

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

Vous pouvez maintenant lancer le serveur de développement.

    ./manage.py runserver

Le site est disponible sur http://127.0.0.1:8000/.
