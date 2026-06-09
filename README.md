<h1 align="center">
  Analyse de Données avec Python
  <br/>
  <sub>pour Professionnels de la Santé</sub>
</h1>

<p align="center">
  <i>Six modules d'une heure — du Python de base au machine learning clinique.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Langue-Fran%C3%A7ais-0072B2?style=flat-square" alt="Langue"/>
  <img src="https://img.shields.io/badge/Niveau-D%C3%A9butant-009E73?style=flat-square" alt="Niveau"/>
  <img src="https://img.shields.io/badge/Dur%C3%A9e-6h-D55E00?style=flat-square" alt="Durée"/>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter"/>
  <img src="https://img.shields.io/badge/Colab-Compatible-F9AB00?style=flat-square&logo=googlecolab&logoColor=white" alt="Colab"/>
</p>

<p align="center">
  Version compacte du cours en 30 h, pensée pour une journée (6 × 1 h)
  ou trois demi-journées (3 × 2 h).<br/>
  <b>Public</b> : professionnels de santé, épidémiologistes, étudiants
  en santé publique, sans pré-requis en programmation.
</p>

---

## Contenu

| Module | Titre | Durée | Notebook (corrigé) | Lancer dans Colab |
|:------:|-------|:-----:|----------|:-----------------:|
| 1 | Python + Pandas pour la santé | 1 h | [`module_01_python_pandas.ipynb`](https://github.com/gabayae/-python-sante/blob/main/notebooks_executes/module_01_python_pandas.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gabayae/-python-sante/blob/main/notebooks_vierges/module_01_python_pandas.ipynb) |
| 2 | Nettoyage et statistique descriptive | 1 h | [`module_02_nettoyage_descriptif.ipynb`](https://github.com/gabayae/-python-sante/blob/main/notebooks_executes/module_02_nettoyage_descriptif.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gabayae/-python-sante/blob/main/notebooks_vierges/module_02_nettoyage_descriptif.ipynb) |
| 3 | Visualisation pour données de santé | 1 h | [`module_03_visualisation.ipynb`](https://github.com/gabayae/-python-sante/blob/main/notebooks_executes/module_03_visualisation.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gabayae/-python-sante/blob/main/notebooks_vierges/module_03_visualisation.ipynb) |
| 4 | Tests d'hypothèses | 1 h | [`module_04_tests_hypotheses.ipynb`](https://github.com/gabayae/-python-sante/blob/main/notebooks_executes/module_04_tests_hypotheses.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gabayae/-python-sante/blob/main/notebooks_vierges/module_04_tests_hypotheses.ipynb) |
| 5 | Régression (linéaire + logistique) | 1 h | [`module_05_regression.ipynb`](https://github.com/gabayae/-python-sante/blob/main/notebooks_executes/module_05_regression.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gabayae/-python-sante/blob/main/notebooks_vierges/module_05_regression.ipynb) |
| 6 | Machine learning clinique | 1 h | [`module_06_ml_clinique.ipynb`](https://github.com/gabayae/-python-sante/blob/main/notebooks_executes/module_06_ml_clinique.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gabayae/-python-sante/blob/main/notebooks_vierges/module_06_ml_clinique.ipynb) |

Le lien dans la colonne **Notebook (corrigé)** ouvre la version exécutée
avec les sorties — utile comme référence ou si vous voulez seulement
lire. Le badge **Open In Colab** lance la version vierge (sans
sorties) directement dans Google Colab — utile pour exécuter les
cellules vous-même, sans installation locale.

**Notes de cours en PDF** : voir [`notes/notes_6h.pdf`](notes/notes_6h.pdf).
Les notes développent la matière théorique et méthodologique, avec des
extraits de code illustratifs (le code complet est dans les notebooks).

Pour l'analyse géospatiale, l'analyse temporelle approfondie et le
projet capstone, voir la version 30 h dans `../code/notebooks/`.

---

## Structure du dossier

```
python-sante/
|-- README.md                       <-- ce fichier
|-- data/                           <-- jeux de données en cache
|   |-- fetch_data.py               <-- rafraîchit le cache
|   |-- gapminder.tsv
|   |-- pima_indians_diabetes.csv
|   |-- heart_uci.csv
|   `-- framingham.csv
|-- notes/                          <-- notes de cours PDF (LaTeX)
|   |-- notes_6h.tex                <-- source LaTeX
|   `-- notes_6h.pdf                <-- PDF compilé (26 pages)
|-- notebooks_vierges/              <-- a distribuer aux apprenants
|   |-- index.ipynb                 <-- page d'accueil (sommaire visuel)
|   |-- module_01_python_pandas.ipynb
|   |-- module_02_nettoyage_descriptif.ipynb
|   |-- ...
|   `-- module_06_ml_clinique.ipynb
`-- notebooks_executes/             <-- corrigés, avec sorties
    |-- index.ipynb
    |-- module_01_python_pandas.ipynb
    |-- ...
    `-- module_06_ml_clinique.ipynb
```

**Point d'entrée recommandé** : ouvrir `notebooks_vierges/index.ipynb`. Cette
page d'accueil présente les 6 modules avec une carte cliquable par module
et un bouton « Ouvrir dans Colab ».

Les notebooks de `notebooks_vierges/` ont **les mêmes cellules** que ceux
de `notebooks_executes/` mais sans les sorties. Distribuez les vierges
aux apprenants ; gardez les exécutés comme correction.

---

<h2 align="center">Lancer les notebooks</h2>

<p align="center">
  <i>Deux chemins pour démarrer — choisissez selon votre confort.</i>
</p>

<table width="100%">
<tr>
<th width="50%" align="center">
  <img src="https://img.shields.io/badge/-Option%20A-0072B2?style=flat-square" alt="Option A"/>
  <br/>Google Colab
</th>
<th width="50%" align="center">
  <img src="https://img.shields.io/badge/-Option%20B-009E73?style=flat-square" alt="Option B"/>
  <br/>Jupyter en local
</th>
</tr>
<tr>
<td width="50%" align="center" valign="top">
  <b>Aucune installation.<br/>Tout se passe dans le navigateur.</b>
</td>
<td width="50%" align="center" valign="top">
  <b>Pour travailler hors ligne,<br/>adapter, ré-utiliser.</b>
</td>
</tr>
<tr>
<td width="50%" align="center" valign="top">
  <a href="https://colab.research.google.com/github/gabayae/-python-sante/blob/main/notebooks_vierges/index.ipynb">
    <img src="https://img.shields.io/badge/Lancer%20l'index%20dans%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white" alt="Open in Colab"/>
  </a>
</td>
<td width="50%" align="center" valign="top">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"/>
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter"/>
</td>
</tr>
<tr>
<td width="50%" valign="top">

**Comment démarrer**

1. Cliquer un badge **Open In Colab** ci-dessus
2. Exécuter avec <kbd>Maj</kbd> + <kbd>Entrée</kbd>
3. Les données se chargent depuis l'URL automatiquement

</td>
<td width="50%" valign="top">

**Comment démarrer**

```bash
git clone https://github.com/gabayae/-python-sante.git python-sante
cd python-sante
jupyter notebook
```

</td>
</tr>
<tr>
<td width="50%" align="center" valign="top">
  <sub>Recommandé pour la formation,<br/>la découverte rapide,<br/>les apprenants sans Python installé.</sub>
</td>
<td width="50%" align="center" valign="top">
  <sub>Recommandé pour adapter le matériel,<br/>ajouter des exercices,<br/>enseigner hors connexion.</sub>
</td>
</tr>
</table>

<details>
<summary><b>Voir les étapes détaillées de l'installation locale</b></summary>

<br/>

#### 1. Installation de Python (si besoin)

Le plus simple est [Anaconda](https://www.anaconda.com/download) :
Python + tous les paquets scientifiques en un seul installeur.

Alternative légère :
[Miniconda](https://docs.anaconda.com/miniconda/) +
`pip install` des paquets ci-dessous.

#### 2. Paquets requis

Tous déjà inclus dans Anaconda. Avec `pip` :

```bash
pip install jupyter pandas numpy matplotlib seaborn scipy scikit-learn statsmodels
```

#### 3. Cloner le dépôt

```bash
# Le nom du depot commence par un tiret, ce qui peut perturber certains
# shells. On clone en imposant un nom de dossier propre :
git clone https://github.com/gabayae/-python-sante.git python-sante
cd python-sante
```

#### 4. Lancer Jupyter

```bash
jupyter notebook
# ou
jupyter lab
```

#### 5. Rafraîchir le cache des données (optionnel)

Les fichiers de `data/` sont déjà à jour. Pour les retélécharger :

```bash
python data/fetch_data.py
```

</details>

---

## Forker le dépôt et rester à jour avec l'original

Si vous voulez **garder votre propre copie modifiable** du cours
(traduction, annotations personnelles, exercices supplémentaires) tout
en récupérant les corrections et améliorations du dépôt original :

### 1. Forker via l'interface GitHub

Sur la page du dépôt
[https://github.com/gabayae/-python-sante](https://github.com/gabayae/-python-sante),
cliquez sur le bouton **« Fork »** en haut à droite. GitHub crée une
copie du dépôt sous votre compte
(`https://github.com/<votre-username>/-python-sante`).

### 2. Cloner votre fork

```bash
git clone https://github.com/<votre-username>/-python-sante.git python-sante
cd python-sante
```

### 3. Ajouter le dépôt original comme « upstream »

Par convention, le remote `origin` pointe vers votre fork, et le remote
`upstream` pointe vers le dépôt original :

```bash
git remote add upstream https://github.com/gabayae/-python-sante.git
git remote -v
# origin     https://github.com/<votre-username>/-python-sante.git (fetch / push)
# upstream   https://github.com/gabayae/-python-sante.git           (fetch / push)
```

### 4. Synchroniser quand le dépôt original évolue

```bash
# Recuperer les nouveautes du dépôt original
git fetch upstream

# Se placer sur main et fusionner les changements
git checkout main
git merge upstream/main

# Pousser la mise a jour sur VOTRE fork
git push origin main
```

> **Astuce.** GitHub propose désormais un bouton
> **« Sync fork »** directement dans l'interface de votre fork
> (page d'accueil du dépôt forké). Il fait l'équivalent des étapes 4
> en un clic, sans terminal.

### 5. Si vous avez modifié des fichiers localement

```bash
# Mettre vos modifications de cote
git stash

# Synchroniser comme ci-dessus
git fetch upstream
git merge upstream/main

# Recuperer vos modifications
git stash pop
# Si conflit : git mergetool puis git add + git commit
```

### 6. Proposer une amélioration au dépôt original

Si vous corrigez une coquille ou ajoutez un exercice utile :

```bash
git checkout -b ma-correction
# ... modifications ...
git commit -m "Description courte de la modification"
git push origin ma-correction
```

Puis sur GitHub : **« Compare & pull request »** -> ouvrir une PR
vers le dépôt original.

---

## Comment chaque notebook charge ses données

Tous les notebooks utilisent le même patron, robuste **en Colab comme en
local** :

```python
from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def load_csv(name, url, **kwargs):
    """Cherche dans ./data/ d'abord, sinon télécharge depuis l'URL."""
    local = DATA_DIR / name
    if local.exists():
        return pd.read_csv(local, **kwargs)
    df = pd.read_csv(url, **kwargs)
    try:
        df.to_csv(local, index=False)
    except OSError:
        pass
    return df
```

- **Jupyter local** : la fonction trouve le fichier dans `data/` -> aucun
  accès internet nécessaire.
- **Colab** : `data/` n'existe pas au démarrage -> la fonction
  télécharge depuis l'URL et la met en cache pour les cellules
  suivantes.

---

## Convention pédagogique des notebooks

Chaque module suit la même structure :

1. **Objectifs d'apprentissage** — ce que l'apprenant saura faire a la
   fin.
2. **Cellule de reproductibilité** — graine aléatoire fixée, versions
   des bibliothèques affichées.
3. **Sections numérotées** — chaque section combine *prose
   explicative* (qui dit *pourquoi*) + *cellule de code* (qui montre
   *comment*).
4. **Exercices avec corrigé** — chaque exercice a deux cellules :
   - `# Votre essai ici` (vide)
   - `# Solution` (remplie, a consulter apres avoir essayé)
5. **Résumé** — récapitulatif d'une page + lien vers le module suivant.

---

## Données utilisées

| Jeu de données | Origine | Utilise dans |
|----------------|---------|--------------|
| **Gapminder** (espérance de vie, PIB, population par pays/année) | [jennybc/gapminder](https://github.com/jennybc/gapminder) | Modules 1, 2, 3 |
| **Pima Indians Diabetes** (n = 768) | [jbrownlee/Datasets](https://github.com/jbrownlee/Datasets) | Module 5 |
| **UCI Heart Disease (Cleveland)** (n = 303) | [sharmaroshan/Heart-UCI-Dataset](https://github.com/sharmaroshan/Heart-UCI-Dataset) | Module 6 |
| **Framingham Heart Study** (extrait pédagogique, n ~ 4 200) | [GauravPadawe/Framingham-Heart-Study](https://github.com/GauravPadawe/Framingham-Heart-Study) | Module 4 |

Tous sont des jeux **publics**, distribués sous licence ouverte par leurs
auteurs originaux.

---

## Résolution des problèmes courants

**Problème.** *Une cellule de chargement renvoie `HTTPError 404`.*

Cela signifie que l'URL distante a bouge depuis la creation du
notebook. Vérifiez que le fichier correspondant est present dans
`data/`. Si oui, le notebook devrait tomber dessus automatiquement. Si
non, recopiez-le depuis votre propre archive ou relancez
`python data/fetch_data.py`.

**Problème.** *`ModuleNotFoundError: No module named 'statsmodels'` (ou
similaire).*

Installez le paquet manquant :

```bash
pip install statsmodels        # ou seaborn, scikit-learn, etc.
```

En Colab : ajoutez une cellule en haut avec
`!pip install statsmodels` puis ré-exécutez.

**Problème.** *Le notebook tourne lentement en Colab.*

Le runtime gratuit de Colab partage les ressources. Pour les modules
4-6 (régression, ML), utilisez l'option **Exécution > Modifier le
type d'exécution > GPU** seulement si vous en avez besoin (les
modèles de ce cours sont assez légers pour le CPU).

---

<h2 align="center">Aller plus loin</h2>

<table>
<tr>
<td width="50%" valign="top">

### Approfondir un module

Chaque module est listé dans la section [Contenu](#contenu) tout en
haut, avec un lien vers la **version corrigée** (lecture confortable
sur GitHub) et un badge **Open In Colab** (exécution interactive).

Pour la théorie et les références bibliographiques :

<p align="center">
  <a href="https://github.com/gabayae/-python-sante/blob/main/notes/notes_6h.pdf">
    <img src="https://img.shields.io/badge/Notes%20de%20cours-PDF%20(26%20p.)-8A4FFF?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Notes PDF"/>
  </a>
</p>

</td>
<td width="50%" valign="top">

### Sujets non couverts par les 6 h

Trois sujets font partie de la **version 30 h** (distribuée séparément) :

- **Analyse temporelle approfondie** — décomposition saisonnière,
  ARIMA, retards de déclaration.
- **Analyse spatiale** — `geopandas`, choroplèthes, indices de Moran
  et Getis-Ord.
- **Projet capstone** — analyse end-to-end + rapport + soutenance.

Voir la [Section 7 des notes PDF](https://github.com/gabayae/-python-sante/blob/main/notes/notes_6h.pdf)
pour les références bibliographiques associées.

</td>
</tr>
</table>

---

## Licence et citation

Matériel pédagogique distribué sous licence ouverte. Si vous le réutilisez,
mentionnez la source.
