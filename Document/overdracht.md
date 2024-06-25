# Overdracht Flappy Bird Project

## Project Overzicht
Dit project is een eenvoudige versie van het spel Flappy Bird, ontwikkeld met behulp van Python en Pygame.

## Vereisten

### Hardware
- **Computer**: MacBook Air 2020 M1
- **Processor**: M1
- **RAM**: 8 GB
- **Opslag**: 256 GB
- **GPU**: Apple-designed integrated graphics (7–8 cores)

### Software
- **Besturingssysteem**: macOS
- **Game Engine**: Pygame versie 2.5.2
- **Versiebeheer**: Git met repository op GitHub
- **IDE**: Visual Studio Code

## Installatie
1. **Python installeren**: Zorg dat Python geïnstalleerd is (minimaal versie 3.7).
2. **Virtuele omgeving maken**:
    ```bash
    python3 -m env venv
    ```
3. **Virtuele omgeving activeren**:
    - macOS/Linux:
        ```bash
        source env/bin/activate
        ```
    - Windows:
        ```bash
        .\venv\Scripts\activate
        ```
4. **Benodigde pakketten installeren**:
    ```bash
    pip install -r requirements.txt
    ```

## Projectstructuur
- **main.py**: Hoofdbestand van het spel.
- **assets/**: Map met afbeeldingen en geluiden.
- **documents/**: Map met documentatie en logboeken.
- **venv/**: Virtuele omgeving map.
- **requirements.txt**: Lijst met benodigde Python-pakketten.

## Workflow
- **Versiebeheer**:
    - Dagelijks committen en pushen naar GitHub.
    - Gebruik duidelijke commitberichten.
- **Documentatie**:
    - Voeg commentaar toe in de code voor duidelijkheid.
    - Houd een dagelijks logboek bij in de `documents/`-map.

## Uitvoeren van het spel
Na installatie en activering van de virtuele omgeving, start het spel met:
```bash
python main.py
