# bbclub

1/ Introduction :
=================

FFClub est un système de gestion de ligue de Blood Bowl, tel que définit dans le lrb6.
L'application est composé d'un frontend et d'un backend.
Le front est un client angular2, le back est un ensemble de webservice REST écrit en python sur Django.

Le système permet de s'enregistrer en tant que coach, de participer à une ligue.
Donc de créer une équipe, de saisir des rapports de match, et de gèrer l'évolution de ses joueurs.

2/ Création de compte :
=======================

la création de compte se fait classiquement, login / mot de passe / confirmation de l'email et activation du compte



3 / Création d'équipe :
=======================
3.1 / Inscription à une ligue
3.2 / Choix des joueurs
3.3 / Choix du stuff d'équipe
3.4 / Choix des compétences de base
3.5 / Finalisation d'une équipe
3.6 / Achat de stuff

Un achat peut être être fait sur une équipe published. Un achat permet de modifier le stuff ou la compo de sont équipe.
Pour être validé un achat doit être compatible de la trésorerie de l'équipe.
A la suite d'un achat, la trésorerie doit diminuer en conséquence.

4 / Création d'un rapport de match :
====================================

4.1 / Choix des équipes
4.2 / Données du rapport
4.3 / Séquence d'avant match
4.4 / Rapport d'équipe
4.5 / Séquence d'après match
4.6 / Publication d'un rapport de match

L'équipe n'est modifié que lorsque le rapport de match est validé.

5/ Evolution des joueurs :
==========================

A la suite de la validation d'un rapport de match, les joueurs de l'équipe, la pop ainsi que la trésorerie
peuvent être amenés à évoluer.

Publication d'un upgrade de joueur.


pré-conditions :
- aucunes,

un rapport de match peut être crée sur n'importe qu'elle équipe
les données de l'équipe sont recalculé

Définition d'un Roster :
========================

Un roster est


Définition d'une Equipe :
=========================


Cycle de vie d'une équipe :
===========================

* Equipe en mode draft :
------------------------
Une équipe en mode draft peut être modifiée sur les axes suivants :
- ajout de stuff d'équipe : apo, RR, Pop, Cheerleader, Assistants etc.
- ajout de joueurs
- ajout des compétences de base pour les joueurs

1/ Comment ajouter du stuff d'équipe ?
On peut modifier une équipe en faisant des appels put ou patch

2/ Comment ajouter des joueurs ?
On peut modifier une équipe directement

* Publication d'une équipe :
----------------------------
Il n'existe qu'un seul moyen de publier une équipe : une appel get /team/<id>/publish
Cet appel fait passer une équipe de l'état draft dans l'état publish

Une team peut repasser dans l'état draft tant qu'aucun rapport de match n'a été enregistré pour l'équipe, en faisant
un get sur /team/<id>/unpublish
Un admin peut faire repasser une équipe dans l'état draft, sans conditions.


* Equipe en mode published :
----------------------------
Une équipe en mode published peut être modifiée suite aux matchs qu'elle fait, ou aux achats qui sont réalisés.
En conséquence, une équipe en mode published ne peut pas être modifiée directement par un appel rest de type put ou patch.
En revanche, la création d'un rapport d'équipe doit influer sur l'équipe en question.
De même la mise à jour d'un rapport d'équipe doit influer sur l'équipe en question.
La suppression d'un rapport d'équipe doit également déclencher la mise à jour de l'équipe.


Publcation d'un upgrade de joueur :
-----------------------------------

Permet de gérér l'avancement en Xp des joueurs.


Cycle de vie d'un rapport de match :
====================================


Quand est-ce que des achats peuvent être faits ?
- n'importe quand
==> prévoir un écran de modification de l'équipe avec les fonctions suivantes :
- acheter du matos
- acheter des joueurs
==> les actions sont donc des achats
==> une actions d'achat doit être

- les mises à jour d'équipe sont faites uniquement sur rapport de match
==> seuls les commis peuvent créer un rapport de match
==> la création d'un rapport de match se fait en plusieur étapes :
- création du rapport avec les équipes concernées
- modification des rapport d'équipe pour ajouter la séquence d'avant match
- modification des rapports d'équipe pour ajouter les rapports de joueurs
==> la création des rapports de jouers déclenche une mise à jour de l'état des joueurs ciblés par le rapport de joueur
- choix des éventuels upgrade pour les joueurs qui ont des upgrade non encore settés

après le rapport de match et à tout moment les équipes peuvent dépenser leur pognon en achat divers et variés
En conséquence une team peut être dans deux états :
- draft : lors de la création
    - une team nouvellement crée est toujours dans l'état "draft"
    - les mise à jours sont possible tant qu'elle restent dans le cadre définit par les règles de la ligue
    - les mise à jour de joueurs sont également possible, on crée alors des upgrade "gratuit" qui ne sont pas pris en compte dans la progression normale des personnages.
    - il faut prévoir un écran ou le joureur voit toutes ses team, afin de pouvoir reprendre et publier celle qui sont en draft

- il faut prévoir une action de publication de la team genre : team/id/publish, c'est cette action qui fait passer la team dans l'état published

- publiée :
    - les achats de matos et de joueurs ne sont possibles que si la trésorerie le permet
    - la trésorerie doit être débitées des achats effectuée
    - la team est prête à recevoir des rapport de match

cas de test de mise à jour des joueurs :
 =======================================


V0 :
---
 - inscription / création de compte

 - publication d'une news
    - ajout de titre
    - ajout de contenu
    - upload de photo / Gif
    - gestion d'une bibliothèque de média

 - création d'une équipe
    - équipe brouillon
    - ajout des compétences de base

 - Saisie d'un rapport de match
    - séquence d'avant match
    - rapport d'équipe
    - séquence d'après match
        - gestion des journaliers
        - gestion des blessure et des morts
        - gestion des points d'expérience des joueurs

 - achats de stuff et de joueurs

 - calcul automatique du classement basé sur les données des rapports de match


V1.1 :
----
 - gestion des commentaires sur une news
 - gestion des likes sur une news
 - gestion des vidéos youtube sur les news
 - gestion du retour de publication des upgrades
 - gestion de la récupération du classement... ?
 - gestion de la publication des upgrades de base
 - gestion de la tendance du classement : hausse / baisse / stable
 - séquence d'aprè match : gestion de l'ajout de joueurs gratuit (invoqués par un nécromant)


V2 :
----
 - inscription a différentes ligues :
    - règles de classement : mode de calcul des points de classement et des points bonus
 - gestion des inducements
 - gestion des renvoi des joueurs, de personnel ou de rr
 - reprendre les TU Team, MatchReport et TeamReport pour les rendre isolés
 - gestion de la dépublication d'un rapport de match
 - gestion des dépenses exponentielles pour les équipe high power




