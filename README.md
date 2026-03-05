# Football-Match-Manager-Redis-Python
Gestion de matchs de football en temps réel avec Redis – Hash, TTL, Sets, Pub/Sub natif et mise à jour de score en Python.


## 📋 Table des matières

- [Description](#-description)
- [Architecture du projet](#-architecture-du-projet)
- [Fonctionnalités](#-fonctionnalités)
- [Structure des données](#-structure-des-données)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [TTL & Expiration automatique](#-ttl--expiration-automatique)
- [Système Publisher / Subscriber](#-système-publisher--subscriber)
- [Technologies utilisées](#-technologies-utilisées)

---

## 📝 Description

Application Python de gestion de matchs de football en temps réel, reposant sur **Redis** comme base de données principale.

Le projet exploite les fonctionnalités clés de Redis :
- **HSET / HGETALL** — Stockage des matchs sous forme de Hash
- **EXPIRE** — TTL automatique sur chaque match
- **SADD / SMEMBERS** — Indexation des matchs par compétition via des Sets
- **PUBLISH / SUBSCRIBE** — Diffusion d'événements en temps réel par canal de compétition

L'application est organisée autour d'une classe `Match` et d'un notebook Jupyter démontrant le cycle complet : création → publication → abonnement → mise à jour.

> 🔗 **Version alternative avec MongoDB** : [football-match-manager-mongodb](https://github.com/votre-username/football-match-manager-mongodb)

---

## 🏗 Architecture du projet

```
football-redis/
│
├── match.ipynb        # Notebook principal : classe Match + Publisher + Subscriber
└── README.md
```

**Flux de données :**

```
Classe Match                Redis                    Subscriber
────────────────            ──────────────────       ──────────────────────
match.save(ttl)  ──HSET──►  match:<id>  (Hash)
                 ──EXPIRE─►  TTL automatique
                 ──SADD───►  competition:<nom> (Set)
                 ──PUBLISH─► canal:<competition> ───► Réception du match_id
                                                       HGETALL match:<id>
                                                       Affichage des infos
                                                       Mise à jour score/statut
```

---

## ✅ Fonctionnalités

| Fonctionnalité | Commande Redis | Description |
|---|---|---|
| ➕ Sauvegarder un match | `HSET` + `EXPIRE` | Stockage complet avec TTL |
| 🗂 Indexer par compétition | `SADD` | Regroupement des matchs par compétition |
| 📢 Publier un événement | `PUBLISH` | Diffusion de l'ID du match sur le canal |
| 📡 S'abonner à un canal | `SUBSCRIBE` | Écoute en temps réel par compétition |
| 🔍 Récupérer un match | `HGETALL` | Lecture de toutes les infos du match |
| ⚽ Mettre à jour le score | `HSET` + `EXPIRE` | Uniquement si match `en cours` |
| 🔄 Changer le statut | `HSET` + `EXPIRE` | Avec prolongation du TTL |

---

## 🗄 Structure des données

### Hash Redis — un match

Chaque match est stocké sous la clé `match:<id>` :

```
match:001
├── id          → "001"
├── domicile    → "Maroc"
├── exterieur   → "France"
├── date_heure  → "2025-12-25 20:00"
├── statut      → "prévu"
├── score       → "0-0"
├── competition → "Coupe du Monde"
├── stade       → "Stade de Marrakech"
└── arbitre     → "Mr. Dupont"
```

### Set Redis — index par compétition

```
competition:Coupe du Monde  →  { "001", "002", ... }
competition:Ligue des Champions  →  { "003", "004", ... }
```

### Canal Pub/Sub

```
canal:Coupe du Monde        →  diffuse les IDs des matchs en temps réel
canal:Ligue des Champions   →  diffuse les IDs des matchs en temps réel
```

### Classe Python `Match`

```python
class Match:
    def __init__(self, id, domicile, exterieur, date_heure,
                 statut, score, competition, stade, arbitre):
        ...

    def save(self, ttl=3600):
        key = f"match:{self.id}"
        r.hset(key, mapping={...})   # Stockage Hash
        r.expire(key, ttl)           # TTL
        r.sadd(f"competition:{self.competition}", self.id)  # Index
```

---

## ⚙️ Installation

### Prérequis

- Python 3.8+
- Redis installé et en cours d'exécution sur `localhost:6379`
- Jupyter Notebook ou JupyterLab

### Démarrer Redis

```bash
# Linux / macOS
redis-server

# Windows (via WSL ou Redis for Windows)
redis-server.exe
```

### Installer les dépendances Python

```bash
pip install redis notebook
```

---

## 🚀 Utilisation

### Lancer le notebook

```bash
jupyter notebook match.ipynb
```

### Étape 1 — Définir la classe Match

```python
import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

class Match:
    def __init__(self, id, domicile, exterieur, date_heure,
                 statut, score, competition, stade, arbitre):
        self.id = id
        self.domicile = domicile
        ...

    def save(self, ttl=3600):
        key = f"match:{self.id}"
        r.hset(key, mapping={...})
        r.expire(key, ttl)
        r.sadd(f"competition:{self.competition}", self.id)
        print(f"✅ Match {self.id} ajouté avec succès")
```

### Étape 2 — Créer et publier un match (Publisher)

```python
match1 = Match(
    id="001",
    domicile="Maroc",
    exterieur="France",
    date_heure="2025-12-25 20:00",
    statut="prévu",
    score="0-0",
    competition="Coupe du Monde",
    stade="Stade de Marrakech",
    arbitre="Mr. Dupont"
)

# Sauvegarder dans Redis
match1.save()

# Publier sur le canal de la compétition
canal = f"canal:{match1.competition}"
r.publish(canal, match1.id)
print(f"📢 Match publié sur {canal}")
```

**Sortie :**
```
✅ Match 001 ajouté avec succès
📢 Match publié sur canal:Coupe du Monde
```

### Étape 3 — S'abonner et recevoir (Subscriber)

```python
pubsub = r.pubsub()
pubsub.subscribe("canal:Coupe du Monde")

for message in pubsub.listen():
    if message["type"] == "message":
        match_id = message["data"]
        match_data = r.hgetall(f"match:{match_id}")
        print("🔔 Nouveau match reçu !")
        for k, v in match_data.items():
            print(f"  {k} : {v}")
```

---

## ⏱ TTL & Expiration automatique

Redis supprime automatiquement les clés dont le TTL est expiré :

```python
r.expire(key, ttl)   # ttl en secondes (ex: 3600 = 1 heure)
```

| Action | Effet sur le TTL |
|---|---|
| `match.save(ttl=3600)` | TTL initial de 1 heure (configurable) |
| Mise à jour du statut | TTL prolongé via `r.expire()` |
| Mise à jour du score | TTL prolongé via `r.expire()` |
| Aucune activité | La clé est supprimée automatiquement par Redis |

Vérifier le TTL restant d'un match :

```bash
# Dans redis-cli
TTL match:001
```

---

## 📡 Système Publisher / Subscriber

Redis Pub/Sub natif — chaque compétition a son propre canal :

```
Publisher                          Redis Pub/Sub                Subscriber
──────────────────                 ─────────────────            ──────────────────────
r.publish(                         canal:Coupe du Monde  ──►   pubsub.subscribe(...)
  "canal:Coupe du Monde",          canal:Ligue Champions ──►   for message in listen()
  match_id                                                        match = HGETALL(id)
)                                                                 afficher infos
```

**Protection de la cohérence du score :**

```python
# Le score ne peut être modifié que si le match est "en cours"
match_data = r.hgetall(f"match:{match_id}")
if match_data["statut"] != "en cours":
    print("❌ Impossible : le match n'est pas en cours")
else:
    r.hset(f"match:{match_id}", "score", nouveau_score)
```

---

## 🛠 Technologies utilisées

| Technologie | Rôle | Version |
|---|---|---|
| Python | Langage principal | 3.8+ |
| Redis | Base de données in-memory (Hash, Set, Pub/Sub, TTL) | 7.x |
| redis-py | Driver Python officiel pour Redis | 5.x |
| Jupyter Notebook | Environnement d'exécution interactif | — |

---

## 👤 Auteur
Imane boujaj-
Projet réalisé dans le cadre du cours **BDSI S1 – Base de données avancées**  
Faculté des Sciences Dhar El Mahraz — Département Informatique  
A.U : 2025/2026
