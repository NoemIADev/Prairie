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


## Reactive  ≠ Rapide

Il ne faut pas confondre un système rapide avec un système réactive ce n'est pas la même chose. Un programme, une interface peut être rapide sans pour autant être réactive, un petit exemple pour bien saisir la différence :

![rapide](images/rapide.gif)

On peut courir vite et ne pas etre reactive ici le bonhomme court mais marque une pause avant de sauté car il **n'a pas anticipé** l'obstacle donc il s'arrete pour **reflechir** à comment reagir a cette nouvelle information puis il saute.

![react](images/react.gif)

Maintenant on peut voir que le bonhomme court sans interruptions et **réagies immédiatement** face au rocher sans avoir besoin de **s'arrêter pour réfléchir**.

c'est la différence entre rapide et réactive, être rapide ne signifie pas savoir faire face au problème rencontré et y réagir en conséquence de manière immédiate.

Pour une application,un jeu ou autre ne pas être réactive c'est ne pas réagir en temps réel aux actions de l'utilisateur ou l'arrivée d'une nouvelle donnée.Si votre programme a besoin de s'actualiser en permanence dès qu'il reçoit une nouvelle information il n'est pas réactif même s'il le fait rapidement.