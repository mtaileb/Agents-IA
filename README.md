Ce dépôt contient le code des exemples d'agents. Le code démontre comment créer et exécuter un agent d'IA en utilisant les outils et les API compatibles avec le standard OpenAI.

## Instructions d'installation

### 1. Cloner le dépôt

Pour commencer, clonez ce dépôt sur votre machine locale :

    git clone https://github.com/cxbxmxcx/AI-Agent-Workflows.git
    cd AI-Agent-Workflows

### 2. Créer votre environnement

Ce projet nécessite **Python 3.11+**. Créez et activez un environnement virtuel Python :

#### Sous macOS/Linux :

    python3 -m venv venv
    source venv/bin/activate

#### Sous Windows :

    python -m venv venv
    venv\Scripts\activate

Si vous préférez utiliser un environnement Python externe, assurez-vous de définir le chemin Python dans VS Code :

  1. Ouvrez la Palette de commandes (`Ctrl+Maj+P` ou `Cmd+Maj+P` sur macOS).
  2. Recherchez "Python : Sélectionner l'interpréteur".
  3. Choisissez l'interpréteur Python pour votre environnement.

### 3. Installer les dépendances

#### Méthode A : Utilisation du débogage de VS Code

Si vous avez VS Code, vous pouvez simplement lancer le débogage (appuyez sur `F5`) pour exécuter les exemples. Les dépendances requises seront installées automatiquement dans le cadre du processus de débogage.

#### Méthode B : Installation manuelle

Alternativement, vous pouvez installer manuellement les dépendances en utilisant uv et pip :

    pip install uv && uv pip install -r requirements.txt

### 4. Configurer l'environnement

Créez un fichier `.env` à la racine du répertoire pour stocker votre clé API OpenAI. Utilisez le fichier `.env.example` fourni comme modèle :

#### Exemple de fichier `.env` :

    OPENAI_API_KEY=votre_clé_api_openai_ici

Remplacez `votre_clé_api_openai_ici` par votre véritable clé API OpenAI. Vous pouvez obtenir une clé API depuis la page des clés API d'OpenAI.

### 5. Exécuter le code

Pour exécuter le code d'exemple, naviguez vers le fichier Python. Par exemple :

    python 01_first_agent.py

Cela exécutera l'agent et affichera la sortie dans le terminal.

## Remarques

  * Assurez-vous d'utiliser l'interpréteur Python correct qui correspond à votre environnement.
  * Le fichier `.env` ne doit pas être partagé ou committé dans le contrôle de version pour garder votre clé API sécurisée.
