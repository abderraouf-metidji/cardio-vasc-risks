

## Contexte du projet



## Veille Regression logistique

#### Qu'est-ce que la regression

La regression logistique est un type de regression. 

Laregression est un type de modèle de prédiction de données utilisé afin d'identifier des relations entre une variable dépendante et une ou plusieurs variables indépendantes. 

Lorsque l'on utilise plusieurs variables indépendante dans notre modèle de prédiction on parlera alors de régression multiple ou multivariée.

L'analyse de regression est utilisé pour 3 points majeurs :
* La prédiction d'effets ou impacts de changement specifiques
* La prediction de données futures ou tendances
* Determiner l'impact de différentes variables indépendantes sur une variable dépendante

il existe 2 types de regression ; la regression linéaire et la regression logistique.

#### Qu'est-ce que la regression logistique

La regression logistique est un algorithme de classification. Elle est utilisée principalement pour prédire un résultat binaire basé sur un set de variables indépendantes. 

Un résultat binaire est un résultat qui ne possède que possibilitées; vrai (1) ou faux (0). Les variables indépendantes sont donc les variables qui vont impacté le résultat de cet algorithm. 

Bien entendu l'aspect binaire peut s'exprimer de plusieurs manières :
* oui ou non
* vrai ou faux
* pass or fail

Il est important de retenir que les variables indépendantes peuvent etre de plusieurs types:
* continue ; comme par exemple le poids
* discrète ordinale ; comme par exemple une échelle de bonheur
* discrète nominale ; comme par exemple la couleurs des yeux 

Pour déterminer si l'algorithme de regression logistique est le bon choix on peut se poser les questions suivantes :
* Est-ce que la variable dépendante est dichtomique ; est-ce que peut etre partagée en un ou deux une ou deux catégories
* Est-ce que les variables indépendantes sont des intervales, des ratios ou ordinales ; cela est lié aux 3 types de variables que nous avons vu au dessus

#### Les hypothèses de la regression logistique

1. La variable dépendante est binaire ou dichtomique. Elle peut donc se partager en une ou deux catègories distinctes. Exemple ; si nous avons des animaux dans notre dataset on peut classfier cette variable dépendnate en vrai c'est un animal ou faux ce n'est pas un animal. 

2. Les variables indépendantes ont une corrélation linéaire liée aux *log odds*. 

3. La regression logistique nécessite un dataset relativement large qui nous permettra d'avoir des résultats plus pertinents.

#### Pourquoi utiliser la regression logistique

La regression logistique est utilisé dans le but de calculer la probabilité qu'un évènement binaire ait lieu ainsi que répondre à des problématiques de classification. 

Par exemple prédire si un email est un spam ou non ou prédire si une transaction est frauduleuse ou non. 

#### Les différents types de regression logistique

1. La regression logistique binaire qui est utilisé afin de prédire la relation entre une variable dépendante (y) et la variable indépendante (x) avec une variable dépendante qui est binaire. 

2. La regression logistique multinominale qui est utilisée quand on a une variable dépendante catègorique qui possède plusieurs catégories. Par exemple si notre variable dépendante est le transport le plus populaire en 2020, le transport sera partagé en plusieurs choix possibles tel que la voiture, le bus, le tramway, le métro etc. Nous n'avons pas donc uniquement 2 choix possible avec notre variable dépendante. 

3. La regression logistique ordinale qui est elle utilisée lorsque nous avons une variable dépendnate (y) qui est ordonnée. C'est à dire qu'elle possède plusieurs catégories tout comme la regression logistique multinominale mais les différentes catégories sont ordonnées. Comme par exemple la taille de t-shirt (XS/S/M/L/XL)

#### Avantages de la regression logistique

1. Elle est plus simple à mettre en place que les autres méthodes de machine learning. 

2. Elle fonctionne bien pour les cas ou le dataset est linéaire et séparable. Par exemple si on peut séparer le dataset en deux catégories distinctes il est plus pertinent de les classifier en deux classes différentes. 

3. Elle permet d'obtenir des aperçu utiles notamment sur sur les relations entre les différentes variables. On peut également en savoir plus sur la direction des relations (positives ou négatives). 

#### Incovénients de la regression logistique

1. Elle ne permet pas de prédire des résultats continu. Par exemple ce modèle de regression n'est pas capable de prédire le niveau le plus haut d'une variable. Il permet uniquement de prédire si la température sera élevée ou non.

2. Elle assume une corrélation linéaire entre la variable prédite (dépendantes) et les variables permettant la prédiction (indépendantes). C'est une limitation car on ne peut pas toujours séparer les observations linéairement.

3. Elle peut ne pas etre précise si le dataset est trop petit. 

## les données et leur analyse



## les algorithmes utilisés



## conclusion

