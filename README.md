# 🩻 DICOM Image Anonymizer (Proof of Concept)

Ein Python-basiertes Skript zur automatisierten, DSGVO-konformen Anonymisierung von medizinischen Bilddaten (DICOM-Format).

## 📸 Projekt-Vorschau
### DICOM Anonymizer Vorschau
<img width="1080" height="113" alt="Screenshot 2026-08-09 221648" src="https://github.com/user-attachments/assets/90181dec-20d8-4900-8192-1360b9f6e97a" />
<img width="802" height="689" alt="Screenshot 2026-08-09 221545" src="https://github.com/user-attachments/assets/8bcf4d54-881d-4648-9441-93a9f91d214e" />


## 📌 Über das Projekt
In der Medizintechnik und der klinischen Forschung fallen täglich tausende radiologische Bilder (CT, MRT, Röntgen) an. Bevor diese Datensätze für Machine-Learning-Modelle oder Studien genutzt werden dürfen, müssen alle personenbezogenen Metadaten (PHI - Protected Health Information) restlos entfernt werden.

Dieses Proof of Concept liest DICOM-Dateien ein, überschreibt sensible Header-Informationen (wie `PatientName`, `PatientID`, `PatientBirthDate`) und speichert die Datei als anonymisierten Datensatz neu ab. Zusätzlich wird das Pixel-Array gerendert und zur visuellen Qualitätskontrolle dargestellt.

Das Projekt demonstriert Kenntnisse in:
* **Medizintechnik & Bildverarbeitung:** Umgang mit dem DICOM-Standard und Pixel-Arrays.
* **Datenschutz im Gesundheitswesen:** Praktische Umsetzung von DSGVO-Anforderungen an Forschungsdaten.
* **Python-Entwicklung:** Nutzung branchenspezifischer Bibliotheken (`pydicom`, `matplotlib`).

## 🛠️ Tech-Stack
* **Sprache:** Python 3
* **Bibliotheken:** `pydicom` (DICOM-Parsing), `matplotlib` (Bild-Rendering)
* **Datenstandard:** DICOM (.dcm)

## 🚀 Lokale Ausführung

1. **Repository klonen:**
   ```bash
   git clone https://github.com/youneslaaf/dicom-anonymizer-poc.git
   cd dicom-anonymizer-poc
