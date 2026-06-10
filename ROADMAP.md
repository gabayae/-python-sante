# Roadmap — chantiers à venir

Ce fichier liste les améliorations identifiées comme utiles mais non
encore implémentées, classées par priorité et estimation d'effort. À
reprendre lors d'une prochaine session de travail.

Contexte : ce matériel est conçu pour du **renforcement de capacités**.
Les chantiers ci-dessous transforment progressivement un matériel
d'« excellent auto-apprentissage » en « formation institutionnellement
reconnaissable » (avec attestation, mesure d'impact, transférabilité à
d'autres facilitateurs).

---

## Décision stratégique sur le curriculum

> **À trancher AVANT d'ajouter de nouveaux modules.**

### Le diagnostic

Le matériel actuel couvre superbement la **biostatistique computationnelle**
(nettoyage, descriptif, IC, tests, régression ajustée, ML calibré) — soit
exactement ce qu'il faut pour rédiger un papier scientifique en santé.

Mais pour du **renforcement de capacités en science des données**, il
manque trois compétences cruciales du quotidien du data scientist :

1. **Travailler sur des données réelles cassées.** Joindre plusieurs
   sources (4 fichiers Excel, 1 export ODBC), parser des dates en formats
   mixtes, réconcilier des IDs qui changent selon le système source. C'est
   60-80 % du temps d'un data scientist.
2. **Communiquer une analyse.** Produire un rapport reproductible
   (Quarto / PDF / HTML), embarquer figures + tableaux + texte, exporter
   dans un format lisible par le directeur de district, le PNLP, l'OMS.
3. **Reproductibilité opérationnelle.** Au-delà des graines aléatoires :
   versionner son code (Git), organiser un projet en dossiers, lancer une
   analyse par ligne de commande. Pour qu'un collègue reprenne l'analyse
   6 mois plus tard.

### Trois options à arbitrer

#### Option A — Recadrer le titre (5 min, conservateur)

Renommer le cours **« Biostatistique computationnelle avec Python pour la
santé »**. Plus honnête, plus précis, plus défendable devant un comité
scientifique. Le contenu actuel devient parfaitement aligné avec son
nom — il n'y a plus de promesse non tenue.

**Coût** : 5 min (édition de quelques fichiers).
**Bénéfice** : crédibilité immédiate, pas d'ajout de maintenance.
**Limite** : n'aide pas les apprenants qui ont besoin de la couche
« data scientist » pour leur poste réel.

#### Option B — Étendre à 7-8 heures (recommandé, ~2-3 h de travail)

Ajouter deux nouveaux modules :

- **Module 7 — Données réelles : jointures, dates, IDs** (1 h)
- **Module 8 — Communication et reporting Quarto** (1 h)

Le cours devient « formation 8 heures » et couvre l'épine dorsale data
science de bout en bout.

**Coût** : ~2-3 h de rédaction par module + tests + intégration.
**Bénéfice** : matériel qui forme vraiment des data scientists en santé.
**Limite** : plus long à animer ; certains formats (atelier d'une
journée) deviennent serrés.

#### Option C — Réallouer dans les 6 heures (radical, ~2 h de travail)

Compresser **Module 4 (tests d'hypothèses) à 45 min** et **Module 6 (ML)
à 45 min**, ce qui libère 30 min × 2 = 1 heure pour un **Module 7
condensé** combinant *données réelles* + *reporting* en une seule heure.

**Coût** : ~2 h (refonte des modules existants + nouveau module).
**Bénéfice** : tient en 6 h, couvre l'essentiel data science.
**Limite** : Module 4 et 6 perdent en profondeur ; un Module 7 condensé
sur deux sujets est forcément superficiel.

### Recommandation

**Option B est ma préférence pour du capacity-building DS sérieux.**
Les six heures actuelles sont déjà denses ; vouloir ajouter du data
engineering et du reporting dans la même enveloppe (Option C) sacrifie la
qualité des modules existants. Mieux vaut assumer un format 8 h.

Si la contrainte 6 h est non négociable (financement, format imposé par
un bailleur), Option C est défendable. Option A est la solution la
plus prudente.

---

## Nouveaux modules à concevoir si Option B ou C retenue

### Module 7 — Données réelles : jointures, dates, IDs (~1 h)

**Effort** : 2-3 h de rédaction + tests.

**Objectifs pédagogiques (Bloom)** :
- *Appliquer* `pd.merge` avec les quatre types de jointure (inner, left,
  right, outer) sur des cas cliniques.
- *Analyser* les implications d'une jointure (combien de lignes
  perdues ? doublons créés ? IDs orphelins ?).
- *Évaluer* la qualité d'une intégration multi-sources.

**Contenu suggéré** :
- Charger 3-4 fichiers hétérogènes (CSV, Excel, TSV).
- `pd.merge` : inner / left / right / outer avec exemples cliniques.
- Détection de duplicats post-merge (`df.duplicated`).
- Parsing de dates en formats mixtes (`pd.to_datetime` avec
  `format="mixed"`, `errors="coerce"`).
- Standardisation d'IDs (strip, casefold, leading zeros, fuzzy matching
  basique avec `rapidfuzz`).
- Validation post-intégration : effectifs attendus, plages plausibles,
  cohérence inter-fichier.
- Cas pratique : reconstituer un dossier patient complet à partir de 3
  sources (registre démographique + résultats labo + résultats imagerie).

**Données suggérées** : créer un jeu pédagogique multi-fichier avec
volontairement des incohérences (IDs avec espaces, dates JJ-MM vs
MM-JJ, encodages différents).

### Module 8 — Communication et reporting Quarto (~1 h)

**Effort** : 2 h de rédaction.

**Objectifs pédagogiques (Bloom)** :
- *Comprendre* le modèle de reporting reproductible : un seul document
  qui contient code + texte + sorties.
- *Appliquer* Quarto pour produire un rapport PDF + HTML.
- *Créer* un rapport paramétré qui peut être généré pour N régions /
  périodes différentes.

**Contenu suggéré** :
- Pourquoi un rapport reproductible ? (versus PowerPoint copié-collé).
- Syntaxe Quarto basique : YAML frontmatter, blocs de code exécutables,
  texte Markdown.
- Embarquer figures matplotlib/seaborn générées par le code.
- Embarquer tableaux pandas formatés avec `pd.DataFrame.to_html()` /
  Quarto `gt` ou similaire.
- Paramétrage : variable `region` ou `annee` injectée depuis la ligne de
  commande (`quarto render rapport.qmd -P region:Adamaoua`).
- Exporter en PDF (LaTeX) et HTML (autonome).
- Cas pratique : transformer l'analyse Module 6 (heart disease prediction)
  en rapport de 3 pages pour un comité technique.

**Bonus** : intro à Streamlit ou Quarto dashboards pour les cas où un
rapport statique ne suffit pas.

---

## Priorité haute — critique pour reconnaissance institutionnelle

### 1. Guide du formateur (`formateur.qmd`)

**Effort estimé** : 30-40 min de rédaction.

**Ce que ça apporte.** Sans un guide d'animation explicite, seul
l'auteur peut animer cette formation. Avec ce guide, n'importe quel
formateur qualifié peut s'approprier et délivrer le contenu.

**Contenu suggéré** :

- Vue d'ensemble (objectifs, public, durée totale, format)
- Module par module :
  - Durée recommandée (50 min de présentation + 10 min Q&A par exemple)
  - Points d'attention pédagogique (concepts qui résistent souvent)
  - Démos live à faire en plus du notebook
  - Variations selon le niveau du groupe
  - FAQ des questions courantes
- Trois scénarios de séquence :
  - Atelier d'une journée (6 × 1 h)
  - Trois demi-journées (2 × 1 h chacune)
  - Formation en ligne asynchrone (rythme libre + sessions de Q&A)
- Logistique pré-session : checklist Colab fonctionne, comptes Google
  testés, données téléchargées en backup hors ligne
- Méthodologie d'animation : pédagogie active, démos, exercices
  individuels vs en binôme

**Publication** : ajouter au navbar dans le menu Modules ou comme entrée
dédiée « Pour les formateurs ».

---

### 2. Pré-test et post-test (`evaluation/`)

**Effort estimé** : 45 min.

**Ce que ça apporte.** Sans mesure quantitative du gain de capacité, on
ne peut pas justifier l'efficacité de la formation auprès des
financeurs (OMS, AFD, World Bank, Affordable Health Initiative, etc.).
Avec un pré/post-test, on peut rapporter : *« 87 % des participants ont
amélioré leur score de ≥ 40 % entre l'entrée et la sortie »*.

**Contenu suggéré** :

- 15-20 questions QCM
- Couverture proportionnelle aux objectifs Bloom déclarés dans
  `about.qmd` (compréhension, application, analyse, évaluation)
- Format : Quarto avec onglets `## Question N` + révélation de la
  réponse au clic ; ou Google Form pour la collecte
- Grille de correction par question avec barème
- Mêmes questions au pré et au post (pour comparaison)
- Optionnel : mini-projet final noté sur 3 critères (qualité du code,
  rigueur de l'analyse, qualité de la communication)

**Publication** : `evaluation/pre-test.qmd` + `evaluation/post-test.qmd`
+ `evaluation/grille-correction.qmd`. Liens dans la page À propos
section « Modalités d'évaluation ».

---

### 3. Template d'attestation de participation

**Effort estimé** : 15 min.

**Ce que ça apporte.** Concrètement, qu'est-ce que les participants
emportent en quittant la formation ? Une attestation officielle est ce
qu'ils peuvent ajouter à leur CV ou présenter à leur employeur.

**Contenu suggéré** :

- Format LaTeX (Beamer A4 paysage) avec placeholders : nom du
  participant, dates, modules complétés, signature, logo bailleur
  optionnel
- Mise en page sobre, cohérente avec la palette du site
- Script Python qui génère un PDF par participant à partir d'un CSV
  d'inscription
- Optionnel : QR code de vérification pointant vers une page « cette
  attestation est-elle authentique ? »

**Publication** : `attestation/template.tex` + `attestation/generate.py`.

---

## Priorité moyenne — rend la formation transférable

### 5. Slides Beamer ou Quarto-revealjs par module

**Effort estimé** : 2-3 h pour les 6 modules.

**Ce que ça apporte.** Pour l'animation en présentiel ou en webinaire,
les notebooks seuls ne suffisent pas — il faut une projection
synthétique qui structure l'attention.

**Contenu suggéré** :

- 15-20 slides par module
- Source `.qmd` avec format `revealjs` (Quarto natif) ou `beamer` (PDF)
- Reprend la palette du site
- Inclut les démos en direct (rappel : exécuter cette cellule du
  notebook M1, etc.)
- Adaptable par le formateur

**Publication** : `slides/module-0N.qmd` × 6.

---

### 6. Jeu de données pédagogique contextualisé (Afrique / LMIC)

**Effort estimé** : 1 h de préparation, 30 min de notebook bonus.

**Ce que ça apporte.** Gapminder et Pima sont génériques. Pour une
formation Afrique francophone, des données plus contextualisées (DHS,
WHO GHO Afrique, AfricaCDC) auraient plus d'impact pédagogique et
politique.

**Contenu suggéré** :

- Choisir un jeu : par exemple les données WHO GHO sur la couverture
  vaccinale africaine, ou un sous-ensemble DHS sur la santé maternelle
  et infantile
- Préparer une version anonymisée et nettoyée
- Notebook « Module bonus » qui refait l'analyse type des Modules 4 ou
  5 mais sur ces données contextuelles
- Document brièvement les conventions de codage du jeu (le DHS a son
  propre vocabulaire)

**Publication** : `data/afrique_*.csv` + `notebooks_executes/module_bonus_afrique.ipynb`.

---

### 7. Glossaire tri-domaine (`glossaire.qmd`)

**Effort estimé** : 1 h.

**Ce que ça apporte.** Les apprenants croisent du vocabulaire de trois
disciplines (épidémiologie, statistique, Python) qu'ils maîtrisent
inégalement. Un glossaire évite l'abandon devant un terme inconnu.

**Contenu suggéré** :

- Format alphabétique avec catégorie (épi / stat / Python)
- Définition courte (2-3 phrases)
- Renvoi vers le module et la section où le terme est introduit
- Optionnel : équivalent anglais entre parenthèses

**Publication** : `glossaire.qmd`, lien dans la sidebar « Ressources ».

---

## Priorité basse — améliorations confort

### 8. FAQ apprenants (`faq.qmd`)

**Effort estimé** : 30 min, puis 5 min par question récurrente
identifiée en session.

À enrichir au fur et à mesure des sessions réelles. Démarrer avec :
Colab plante, package manquant, données qui ne se chargent pas,
erreur d'encodage, comment partager mon travail, etc.

---

### 9. Vidéos walk-through par module

**Effort estimé** : 4-6 h par module (enregistrement + montage).

**Ce que ça apporte.** Certains apprenants préfèrent l'audiovisuel à
l'écrit. Une captation YouTube/Vimeo de 15-20 min par module avec
voix off explicative démultiplie l'audience.

---

### 10. Reconnaissance bailleur / partenaire

**Effort estimé** : 5 min.

Bloc dédié dans le footer du site et la page d'accueil. Souvent
contractuellement requis si le matériel a été financé par un
programme spécifique (Mucha, OMS-AFRO, Wellcome, etc.).

À activer quand un partenariat précis est en place.

---

### 11. Forum / community of practice

**Effort estimé** : 10 min de setup ; engagement variable.

**Options** :

- Activer **GitHub Discussions** sur le repo (Settings > Features >
  Discussions). Catégories : Q&A pédagogique, Partage d'analyses,
  Suggestions.
- Créer un **canal Slack** ou **WhatsApp** dédié, listé dans la page À
  propos.

Sans community de suivi, l'effet de la formation s'estompe en 3-6
mois après la session.

---

## Maintenance générale

### Documentation interne du code

- Le dossier `_build/` (gitignoré, donc local seulement) gagne à avoir
  un `_build/README.md` qui explique le workflow : modifier `m0N.py` →
  `python _build/run_all.py` → rebuild notebooks → `quarto render` →
  commit.

### Tests automatisés

- L'Action GitHub vérifie déjà que le site rend sans erreur. On
  pourrait ajouter un test qui ouvre quelques URL clés et vérifie
  qu'elles contiennent les éléments attendus (titres, badges Colab,
  liens externes).

### Versioning

- Adopter un système de tags SemVer (`v6.1.0`, `v6.2.0`...) pour les
  versions stables. Permet à des organisations qui adoptent le
  matériel de figer une version précise.

---

## Notes de la dernière session de travail

- Le titre de la marque est `Python pour la Santé` dans le navbar.
- L'audience est élargie au-delà des cliniciens (surveillance, santé
  environnementale, etc.).
- La page À propos a été déplacée en deuxième position dans la navbar
  (juste après Accueil) et enrichie avec objectifs Bloom, prérequis,
  modalités d'évaluation, contact pour organisations.
- Le pré-test, post-test, attestation et guide formateur sont
  mentionnés dans la page À propos comme « en développement », ce qui
  prépare leur ajout sans rupture.
