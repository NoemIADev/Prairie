# La programation réactive.

La réactivité, c’est la capacité d’un système (site, application, interface) à réagir automatiquement et immédiatement à un changement, sans action supplémentaire de l’utilisateur.

Ce changement peut venir :

-de l’utilisateur (clic, saisie clavier, scroll…)

-du système (données reçues, timer, API, état interne)

-du réseau (réponse serveur, erreur, chargement terminé)

 **Point clé** :

L’interface se met à jour parce que l’état change, pas parce qu’on lui dit explicitement de se rafraîchir.

exemple : quand vous faites une recherche google les propositions s'actualisent en temps réel lorsque vous rentrez du texte.

![reactgoogle](images/google.png)


## Reacive  ≠ Rapide

Il ne faut pas confondre un système rapide avec un système réactive ce n'est pas la même chose. Un programme, une interface peut être rapide sans pour autant être réactive, un petit exemple pour bien saisir la différence :

![rapide](images/rapide.gif)

On peut courir vite et ne pas etre reactive ici le bonhomme court mais marque une pause avant de sauté car il n'a pas **anticipé** l'obstacle donc il s'arrete pour **reflechir** à comment reagir a cette nouvelle information puis il saute.

![react](images/react.gif)

Maintenant on peut voir que le bonhomme court sans interuption et reagis **imediatement** face au roché sans avoir besoin de **s'arreter pour reflechir**