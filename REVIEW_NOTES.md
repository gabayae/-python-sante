# 6hours/ — note de construction

Version condensee 6 h du cours, en francais, prete pour Colab et Jupyter local.

## Resultat de la verification

| Module | Titre                          | Cellules | Code | Md  | Erreurs | Warns | Encarts Syntaxe | Taille corrige |
|-------:|--------------------------------|---------:|-----:|----:|--------:|------:|----------------:|---------------:|
| 1      | Python + Pandas                |   46     |  23  |  23 |   0     |   0   | 15              |   80 KB        |
| 2      | Nettoyage + descriptif         |   40     |  20  |  20 |   0     |   0   | 10              |   56 KB        |
| 3      | Visualisation                  |   34     |  17  |  17 |   0     |   0   |  9              | 1057 KB        |
| 4      | Tests d'hypotheses             |   34     |  17  |  17 |   0     |   0   |  9              |  136 KB        |
| 5      | Regression                     |   36     |  18  |  18 |   0     |   0   |  9              |  218 KB        |
| 6      | ML clinique                    |   35     |  18  |  17 |   0     |   0   |  8              |  502 KB        |

**Total** : 225 cellules (112 markdown, 113 code), toutes executees, **0 erreur, 0 stderr-warning**, **60 encarts Syntaxe**.

## Charte visuelle (revision finale)

Chaque module commence par :

- **Banniere en gradient** (couleurs Wong colour-blind-safe) avec
  intitule du cours, numero de module, titre, duree.
- **Badges d'information** (niveau, duree, prerequis, "Colab compatible").
- **Badge "Open in Colab"** avec URL placeholder editable dans
  `_build/style.py` (variable `COLAB_REPO`).
- **Panneau "Objectifs du module"** — encadre stylise vert.
- **Callout d'introduction** (Astuce / Attention / Note selon le module).

Chaque module se termine par :

- **Section Ressources** (doc officielle, manuels, datasets GitHub, etc.).
- **Footer de navigation** avec liens `← Module N-1 · Sommaire · Module N+1 →`.

En sus, chaque module contient 2 a 4 **callouts inline** pour les conseils
cliniques et les pieges courants.

**Index de cours** : un nouveau notebook `index.ipynb` sert de page
d'accueil. Il contient un hero header en gradient et 6 cartes de modules
avec :

- Titre + numero de module + duree
- Resume en 2-3 lignes
- Datasets utilises et prerequis
- Boutons "Ouvrir le notebook" et "Ouvrir dans Colab"

L'index propose aussi 2 cartes "Demarrage rapide" (Colab vs Jupyter local) et
un arbre de fichiers commenter.

## Single source of truth de la charte

Toute la presentation visuelle vit dans `_build/style.py`. Modifier la
couleur primaire, le format des badges, le contenu du footer — il suffit
d'editer ce fichier et de relancer `python _build/run_all.py`. Les sept
notebooks recoivent automatiquement la nouvelle charte.

## Enrichissements pedagogiques (revision precedente)

Chaque module a ete enrichi avec :

1. **Encarts \"Syntaxe\" avant chaque construct nouveau** — un bloc citation
   markdown qui montre le **patron abstrait** avant l'exemple concret.
   Exemple :
   ```
   > **Syntaxe — for**
   > ```python
   > for element in collection:
   >     # corps de la boucle
   >     print(element)
   > ```
   ```
2. **Commentaires lourds dans les cellules de code** — chaque ligne non
   triviale a un `#` explicatif a droite. Au lieu de supposer le code
   comprehensible, on dit *pourquoi* chaque ligne fait ce qu'elle fait.
3. **Section \"Ressources et liens utiles\" en fin de chaque module** :
   - Documentation officielle (Python, pandas, numpy, matplotlib, seaborn,
     scipy, sklearn, statsmodels).
   - Manuels gratuits en ligne (VanderPlas, McKinney, James et al.).
   - Articles methodologiques cles (Rubin 1976, Wong 2011, Wasserstein &
     Lazar 2016, Cohen 1988, Benjamini-Hochberg 1995).
   - Repos GitHub des datasets utilises.
   - Outils complementaires (Pingouin, fairlearn, SHAP, XGBoost).
   - Checklists de rapportage (STROBE, TRIPOD).

## Arborescence livree

```
6hours/
|-- README.md                         <-- consignes utilisateurs (FR)
|-- REVIEW_NOTES.md                   <-- ce fichier
|-- data/                             <-- 4 datasets caches + fetch_data.py
|   |-- fetch_data.py
|   |-- framingham.csv                (187 KB)
|   |-- gapminder.tsv                  (80 KB)
|   |-- heart_uci.csv                  (11 KB)
|   `-- pima_indians_diabetes.csv      (23 KB)
|-- notebooks_vierges/                <-- a distribuer aux apprenants
|   |-- module_01_python_pandas.ipynb           (25 KB, sans sorties)
|   |-- module_02_nettoyage_descriptif.ipynb    (26 KB)
|   |-- module_03_visualisation.ipynb           (28 KB)
|   |-- module_04_tests_hypotheses.ipynb        (24 KB)
|   |-- module_05_regression.ipynb              (23 KB)
|   `-- module_06_ml_clinique.ipynb             (26 KB)
|-- notebooks_executes/               <-- corriges, avec sorties
|   `-- (memes noms, tailles plus grosses car sorties incluses)
`-- _build/                           <-- sources qui generent tout
    |-- nbutil.py                     <-- helper nbformat
    |-- loader.py                     <-- snippet load_csv (cache + URL)
    |-- m01.py ... m06.py             <-- un builder par module
    `-- run_all.py                    <-- build + execute + strip outputs
```

## Decisions de conception

### Quel contenu garder pour 6 h ?

Six modules de 1 heure. J'ai garde l'epine dorsale analytique :

- Module 1 (1 h) — Python + Pandas       <-- chapitres 1, 2 du 30 h
- Module 2 (1 h) — Nettoyage + descriptif <-- chapitres 3, 4
- Module 3 (1 h) — Visualisation         <-- chapitre 5
- Module 4 (1 h) — Tests d'hypotheses     <-- chapitre 6
- Module 5 (1 h) — Regression            <-- chapitre 7
- Module 6 (1 h) — ML clinique           <-- chapitre 8

Coupes :
- **Chapitre 9 — geospatial / temporel** : 1 h n'est pas suffisant.
  Signale dans le README comme "pour aller plus loin".
- **Chapitre 10 — capstone** : meme raison ; pointe vers la version 30 h.

### Deux dossiers : `notebooks_vierges/` et `notebooks_executes/`

- **Vierges** (24-28 KB chacun) : memes cellules, sorties effacees,
  `execution_count = null`. C'est ce que l'instructeur distribue.
- **Executes** (47-1046 KB) : meme structure, mais avec toutes les
  sorties + graphiques inclus dans le JSON. Sert de **corrige** que
  l'instructeur garde sous la main et que l'apprenant peut consulter
  apres avoir essaye.

Les vierges sont produits automatiquement par `_build/run_all.py` qui
copie chaque execute en effacant les outputs (pas besoin de
maintenance separee).

### Chargement de donnees — Colab et local en une seule API

Tous les modules utilisent le meme snippet `load_csv` :

```python
_CANDIDATES = [Path("data"), Path("../data")]   # racine OU sous-dossier
DATA_DIR = next((p for p in _CANDIDATES if p.is_dir()), Path("data"))

def load_csv(name, url, **kwargs):
    for candidate_dir in _CANDIDATES:
        local = candidate_dir / name
        if local.exists():
            return pd.read_csv(local, **kwargs)
    df = pd.read_csv(url, **kwargs)
    try:
        sep = kwargs.get("sep", ",")
        df.to_csv(DATA_DIR / name, index=False, sep=sep)
    except OSError:
        pass
    return df
```

**Pourquoi ce design.** Les notebooks vivent dans
`notebooks_vierges/` ou `notebooks_executes/` ; les donnees sont une
fois pour toutes dans `data/`. Le notebook tente d'abord `./data/`
(au cas ou il aurait ete deplace), puis `../data/` (cas normal),
puis tombe sur l'URL si ni l'un ni l'autre n'existe (cas Colab).

**Bonus** : le cache respecte le separateur d'origine. Le TSV de
Gapminder reste un TSV (corrige d'un bug que j'ai trouve a la
construction : `to_csv` ignorait `sep` des `read_csv_kwargs` et
sauvait toujours en virgule-separe).

### Aliasing des URLs (anti-bitrot)

Les URLs hardcodees dans les notebooks sont toutes confirmees
fonctionnelles a la date de construction :

- **Gapminder** : `jennybc/gapminder` (stable depuis des annees)
- **Pima** : `jbrownlee/Datasets`
- **UCI Heart** : `sharmaroshan/Heart-UCI-Dataset`
- **Framingham** : `GauravPadawe/Framingham-Heart-Study`

Si l'une casse, le fichier reste dans `data/` et le notebook le
trouve. Pour rafraichir le cache : `python data/fetch_data.py`.

## Reconstruire et re-verifier

Depuis `6hours/` :

```bash
python data/fetch_data.py     # optionnel - rafraichit le cache
python _build/run_all.py      # rebuild + execute + strip outputs
```

`run_all.py` :
1. Pour chaque module : execute `_build/m0N.py` -> genere le `.ipynb`
   dans `notebooks_executes/`.
2. Execute le notebook avec `jupyter nbconvert --execute`.
3. Copie sans outputs dans `notebooks_vierges/`.
4. Affiche un tableau recapitulatif par module.

Le code de sortie est non-nul si une cellule echoue ou s'il manque une
execution. Utile en CI.

## Differences vs la version 30 h

- **Densite par notebook** : un peu plus compacte
  (15-20 cellules de code par module au lieu de 20-30).
- **Langue** : francais (tout le texte, les commentaires de code,
  les noms de fonctions et de variables francisees quand pertinent).
- **Pas de geospatial** ni de capstone (renvoyes au 30 h).
- **Distribution dual vierges + executes** : specifique a la version
  6 h. La version 30 h ne livre que les notebooks executes.

## Dependances logicielles

Aucune nouvelle bibliotheque. Identique a la version 30 h :

- Python 3.10+
- pandas 2.x, numpy 2.x, scipy 1.17+
- matplotlib 3.x, seaborn 0.13+
- scikit-learn 1.x, **statsmodels 0.14.6+** (la 0.14.4 est cassee
  avec scipy 1.17)

En Colab tout est deja present par defaut.

## Workflow d'utilisation pour l'instructeur

1. Telechargez le dossier `6hours/` (par exemple via `git clone` ou
   un zip).
2. **Distribuez** `notebooks_vierges/` aux apprenants — un .ipynb par
   module + le fichier `data/` (ou laissez le chargement par URL
   faire son office en Colab).
3. **Gardez** `notebooks_executes/` comme corrige a votre disposition.
4. En seance, projetez ou faites travailler les apprenants sur les
   vierges. Les solutions sont incluses dans la cellule
   `# Solution` qui suit chaque cellule `# Votre essai ici`.

## Workflow d'utilisation pour l'apprenant

- En **Colab** : aucune installation. Glisser-deposer un .ipynb de
  `notebooks_vierges/` dans Colab. Les donnees se chargent par URL.
- En **Jupyter local** : Anaconda + `jupyter notebook` dans le
  dossier `6hours/`. Les donnees se chargent depuis `data/`.

## Verifications residuelles

J'ai laisse `_build/` accessible pour que vous puissiez :

- ajuster une formulation et regenerer (`python _build/m0N.py`),
- ajouter un module 7 si besoin (copier `m06.py` comme squelette),
- re-executer tout (`python _build/run_all.py`).

Aucune dependance externe au-dela des bibliotheques scientifiques
standards.
