# Screen ta préfecture

## Contexte

L’idée de cet outil est née de deux épisodes. Le premier est une recherche ethnographique dans le cadre d’un travail de thèse sur les trajectoires administratives des familles migrantes en France : les échanges avec les familles enquêtées et avec des bénévoles associatifs font ressortir avec acuité la lourdeur des démarches de régularisation dans le cadre d’une dématérialisation accrue des administrations migratoires. Le second épisode est une réunion publique du collectif « Bouge ta préfecture » en novembre 2021, qui a mis en évidence le blocage des rendez-vous en préfecture, en particulier pour « l’admission exceptionnelle au séjour » (qui est en réalité une des seules voies d’accès à la régularisation pour les personnes en situation irrégulière qui résident et travaillent, souvent en famille, depuis plusieurs années en France).

Depuis une dizaine d'année, la dématérialisation des services publics s'est grandement développée. Celle-ci est particulièrement prégnante en ce qui concerne le droit des étrangers. La préfecture impose à ces derniers de prendre rendez-vous en ligne pour accomplir leurs démarches : première demande ou renouvellement de titre de séjour, changement d'adresse, etc. 

La dématérialisation a 2 conséquences. D'une part, elle exclut les publics les plus précaires des démarches administratives (ne disposant pas d'ordinateur ou de connexion internet, peu à l'aise avec internet ou la lecture de contenu en français). D'autre part, elle invisibilise les files d'attentes devant la préfecture. En effet, le principal problème auquel doivent faire face les étrangers qui cherchent à mener des démarches administratives est aujourd'hui l'absence de disponibilité des rendez-vous en ligne. Face à cette pénurie de rendez-vous, le contentieux dans les tribunaux administratifs s'est développé. Les individus déposent des recours en exhibant des mois de captures d'écran prouvant l'absence de créneaux disponibles, afin de forcer la préfecture à leur délivrer un rendez-vous. La prise de capture d'écran n'est pas seulement une tâche ingrate et répétitive qui fait peser une charge mentale sur les demandeurs et demandeuses : elle fait également durer davantage des démarches déjà très longues.

## Méthode

L’association La Cimade a déjà produit les chiffres de ce blocage des rendez-vous via le site <a href="https://aguichetsfermes.lacimade.org">« À guichets fermés »</a>. L’outil proposé ici fonctionne de la même manière, mais projette de mettre à disposition non pas des chiffres mais les captures d’écran concrètes des sites des préfectures, afin de fournir de manière rapide et exhaustive de la matière aux mails de relance à la préfecture, ou encore aux dossiers de recours dans les tribunaux administratifs. 

De la même manière que le bot de La Cimade, cet outil se rend sur les sites des préfectures, et pour chaque type de titre de séjour ouvert à la prise de rendez-vous en ligne, simule une prise de rendez-vous. Une capture d’écran est prise au moment où s’affiche la page finale (en général celle qui annonce qu’aucun créneau de rendez-vous n’est disponible). 

En l’état actuel, le bot navigue sur le site de la préfecture de Paris, et celui de la préfecture de Bobigny. Il se concentre sur les demandes de rendez-vous pour un premier titre de séjour « Admission exceptionnelle au séjour » pour différents motifs : vie privée et familiale, travail, raisons médicales (dans le cas de la préfecture de Paris), et vie privée et familiale et travail (dans le cas de la préfecture de Bobigny). Pour Paris, le bot teste également les rendez-vous pour un « premier titre de séjour étudiant » pour les étudiants non munis d’un visa long séjour. 

## Stockage des fichiers

Les images au format .png sont automatiquement stockées dans un dossier correspondant au motif du titre de séjour correspondant. Le titre de chaque fichier indique la date à laquelle la capture d’écran a été prise. Pour l’admission exceptionnelle au titre du travail à la préfecture de Paris (CRE Charcot), le site propose 2 plages d’accès aux rendez-vous : « salarié » et « salarié 2 ». Le bot teste ces 2 plages et capture le résultat pour chacune d’entre elle. 

## Continuations et améliorations possibles

Cet outil pourrait être élargi à d’autres préfectures. Si cela n’a pas été fait dans un premier temps, c’est en raison des différentes interfaces et arborescences de chaque site, ce qui rend fastidieux la généralisation de la navigation du bot. Par ailleurs, tous les types de démarches ne peuvent pas être screenées par le bot, car depuis très récemment, les préfectures ont changé leur mode d’accès : les démarches doivent être menées via une plateforme nominative (« France Connect »), ce qui fait peser la charge des captures d’écran sur les individus, et entrave l’action des associations. 

D'autre part, si le bot travaille seul, il doit pour l’instant être lancé manuellement. Une continuation immédiate sera ainsi d’automatiser le lancement de Python, à des horaires aléatoires au cours de chaque journée, afin d’en faire une pure tâche de fond. 

Enfin, l'ensemble du processus est très lent (parfois plus de 20 minutes en semaine). Ce n'est pas dû à une lenteur du bot, mais du site des préfectures. Ces derniers mettent un temps infini à charger, voire crashent complètement ("Service surchargé"). Sur cet aspect, le bot n'a pas la main, donc il n'est pas possible d'y faire grand chose !
