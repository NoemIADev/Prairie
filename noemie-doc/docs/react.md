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

<video controls autoplay loop muted width="500">
  <source src="video/rapide.mp4" type="video/mp4">
</video>