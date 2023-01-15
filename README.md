# Space-Invader

Bienvenue au Space Invader de Lise et Mélanie!

Participants: Lise MARCHANDON & Mélanie MARIOTTE

-----------------------------------------------------------------------------
Principe : 

T'as l'opportunité d'être un petit chat dans un monde qui se fait attaquer par des souris et son boss. Ton but est de tiré sur les souris avant qu'elles soient arrivées tout en bas. Pour pas non plus rendre l'affaire difficile, tu peux te protéger derrière les paniers qui sont mis à ta disposition mais attention parce que une fois atteints par un missile (que ce soit de l'ennemi ou le tien), ils disparaîtront. Ainsi, plus tu tireras sur les souris plus tu gagneras de points et une fois toute les souris éliminées tu pourras passer à la prochaine étape.
 
------------------------------------------------------------------------------
Comment jouer? 

Afin de déplacer le petit chat, tu devras utiliser les touches 'q' et 'd' pour te déplacer à gauche ou à droite. Ainsi, si tu veux tirer sur l'ennemi, il suffit de taper sur la touche 'espace'.

Attention: le déplacement du petit chat n'est pas fluide, c'est-à-dire que si tu tapes sur la touche 'd' pour te déplacer à droite il faudra réappuyer pour faire un autre déplacement à droite

------------------------------------------------------------------------------
Détails sur l'implémentation du TAD:

Nous nous servons principalement des listes. En effet, elles ont été implémentées lorsqu'on devait gérer les ennemies, les missiles et les paniers. Ceci nours permettait de accèder à un élément connaissant son rang et donc visé sa supression. On utilise aussi de méthodes pour savoir si une liste est vide ou pas et des méthodes pour connaître sa longueur. 
Il y a eu un essai de travailler avec les piles dans les classes Boucliers et Ennemie où on récupérer l'identifiant du premier bouclier/ ennemie séparément des autres identifiants. 

------------------------------------------------------------------------------
Autres détails: 
Notre projet est composé de:
- un programme principal (Space Invader)
- fichier Vaisseau qui gère la classe Vaisseau
- fichier Bouclier qui gère la classe Bouclier
- fichier Fonctions qui gère les fonctions du clavier ainsi que une partie des fonctions qui gèrent les missiles
- fichier Missile qui gère la classe Missile
- fichier Niveau qui gère la classe Niveau
- fichier Ennemie qui gère la classe Ennemie

On vous demande pardon puisque nous avons écrit en snake_case et en CamelCase donc ceci fait partie des To Do.
Les détails des améliorations qu'on aurait pu faire sont détaillées sur chaque fichier dans la partie To Do: 


