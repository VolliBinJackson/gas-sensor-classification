# Attention Mechanismen für multivariate Zeitreihen -
# Interpretierbare Sensorik-Analysen bei Sensordrift

Dieses Projekt untersucht die Klassifikation von Gasarten (1–6) anhand multivariater Sensordaten unter Berücksichtigung von Sensordrift.
Neben der reinen Vorhersageleistung liegt ein starker Fokus auf Interpretierbarkeit mittels Attention-Mechanismen und Feature-Analysen.


# Motivation & Problemstellung

In realen Sensorsystemen (z. B. industrielle Gasdetektion) treten zwei zentrale Herausforderungen auf:

1. Multivariate Zeitreihen
   → Viele Sensoren liefern gleichzeitig Messwerte, die zeitlich voneinander abhängen.
2- Sensordrift
    → Sensoren verändern ihr Verhalten über die Zeit (Alterung, Umweltbedingungen),
    wodurch sich Datenverteilungen verschieben und Modelle an Genauigkeit verlieren.

Ziel:
Robuste Klassifikation der Gasarten und gleichzeitige Erklärbarkeit, um zu verstehen:

- welche Sensoren
- zu welchen Zeitpunkten
- unter Driftbedingungen

entscheidend für die Modellentscheidung sind.


 # Datensatz

- UCI Gas Sensor Array Drift Dataset
- Multivariate Zeitreihen von Gassensoren
- Labels: 6 verschiedene Gasarten
- Enthält explizit zeitabhängige Drift-Effekte


# Ziele des Projekts

- Klassifikation der Gasarten (1–6)
- Vergleich klassischer ML-Modelle mit Deep-Learning-Ansätzen
- Analyse der Auswirkungen von Sensordrift
- Interpretierbarkeit durch Feature Importance & Attention Scores
- Saubere, modulare und reproduzierbare ML-Pipeline


# Modellarchitektur & Baselines
# Klassische ML-Baseline

Random Forest
  - Trainiert auf aggregierten Features
  - Nach Training:
     - Konfusionsmatrix
     - Feature Importance Analyse
   
LSTM und Transformer
   - Sequenzbasierte Inputs
   - Modellierung zeitlicher Abhängigkeiten
   - Attention-Scores zur Gewichtung wichtiger Zeitpunkte
   - Driftanalyse zur Identifikation des Zeitpunkts modellinterner Wahrnehmung des Drifts (mit Schwellenwert)
   - Nach Training:
        - Erstellung von Sequenzen
        - Visualisierung von Train/Test-Loss
        - Anzeige der ersten N Klassifikationen auf Testdaten
        - Analyse & Visualisierung der Attention Scores
        - Driftanalyse anhand von Hidden States und Attention-Gewichten
    

# Training & Evaluation

- Alle 3 Modelle wurden vollständig trainiert
- 5-Fold Cross-Validation zur stabilen Evaluation
- Grid Search für Hyperparameter-Optimierung der neuronalen Modelle
- Vergleich der Modelle anhand:
   - Accuracy
   - Konfusionsmatrix
   - Robustheit gegenüber Drift
   - Interpretierbarkeit
 


# Interpretierbarkeit

- Random Forest:
   - Feature Importance zur Identifikation relevanter Sensoren

- LSTM & Transformer:
  - Attention Scores zur Analyse:
  - Welche Zeitpunkte entscheidend sind
  - Welche Sensoren unter Drift besonders gewichtet werden
  - Zusammenhang zwischen Drift und Modellfokus
 

# Technologien & Tools

- Python
- NumPy, Pandas, Scikit-Learn
- PyTorch 
- Matplotlib, Seaborn
- Jupyter Notebook
- Modularer Projektaufbau



# Modellübersicht & Ergebnisse

Ziel:
Klassifikation von Gasarten aus multivariaten Zeitreihen unter Sensordrift mit Fokus auf Interpretierbarkeit.

# Gemeinsames Setup

- Datensatz: UCI Gas Sensor Array Drift Dataset
- Train/Test Split: 80 % / 20 %
- Evaluation: 5-Fold Cross-Validation
- Hauptmetrik: Accuracy
- Zusätzliche Analyse:
     - Attention Scores
     - Hidden-State-Driftanalyse


🌲 Random Forest

- Accuracy: 99,53 % (höchste)
- Sehr geringer Trainingsaufwand
- Feature Importance zur globalen Interpretierbarkeit
- Limitationen:
   - Keine Sequenzmodellierung
   - Keine zeitabhängige Interpretierbarkeit
   - Keine Attention-Mechanismen

-> Stark für effiziente Klassifikation, eingeschränkt für Drift- und Zeitreihenanalyse



🔁 LSTM + Attention

- Accuracy: 97,29 %
- Sehr gut geeignet für zeitliche Abhängigkeiten
- Attention Scores zeigen relevante Zeitpunkte innerhalb der Sequenz
- Hidden-State-Analyse erhöht Interpretierbarkeit
- Keine Drift-Warnungen erkannt
- Trainingsaufwand: mittel

-> Gute Balance zwischen Performance und zeitlicher Interpretierbarkeit



🔀 Transformer + Self-Attention

- Accuracy: 98,54 %
- Robuste Modellierung komplexer Sequenzen
- Self-Attention reagiert sensitiv auf Veränderungen in Zeitreihen
- Attention Scores + Hidden-State-Analyse
- Mehrere Drift-Warnungen erkannt
- Trainingsaufwand: mittel

-> Höchste Interpretierbarkeit und beste Drift-Sensitivität



# Fazit

- Alle Modelle sind für die Gasklassifikation geeignet
- Random Forest: effizient & sehr genau
- LSTM & Transformer: klare Vorteile bei zeitlicher Modellierung und Erklärbarkeit
- Transformer: besonders geeignet für driftkritische und sicherheitsrelevante Anwendungen
