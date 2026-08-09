import pydicom
from pydicom.data import get_testdata_file
import matplotlib.pyplot as plt

def anonymize_dicom(input_path, output_path):
    """
    Liest eine DICOM-Datei ein, anonymisiert die personenbezogenen Daten 
    und zeigt das Bild zur Kontrolle an.
    """
    try:
        print(f"Lese DICOM-Datei ein: {input_path}")
        ds = pydicom.dcmread(input_path)

        # 1. Metadaten vor der Anonymisierung ausgeben
        print(f"[VORHER] Patientenname: {ds.get('PatientName', 'Unbekannt')}")
        print(f"[VORHER] Patienten-ID: {ds.get('PatientID', 'Unbekannt')}")

        # 2. Anonymisierung durchführen (DSGVO-konform)
        print("\nStarte Anonymisierungsprozess...")
        ds.PatientName = "ANONYMOUS^PATIENT"
        ds.PatientID = "123456789"
        
        if 'PatientBirthDate' in ds:
            ds.PatientBirthDate = "19000101" # Fiktives Datum

        # 3. Anonymisierte Datei speichern
        ds.save_as(output_path)
        print(f"[NACHHER] Erfolg! Anonymisierte Datei gespeichert als: '{output_path}'\n")

        # 4. Bild zur Kontrolle anzeigen (Bone-Colormap für CT/Röntgenbilder)
        plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
        plt.title(f"DICOM Viewer - Anonymisiert\nPatient: {ds.PatientName}")
        plt.axis('off') # Versteckt die Achsen für eine saubere Ansicht
        plt.show()

    except Exception as e:
        print(f"Fehler bei der Verarbeitung der Bilddatei: {e}")

if __name__ == "__main__":
    # Lädt automatisch eine sichere, kleine CT-Testdatei aus der Bibliothek
    test_file = get_testdata_file("CT_small.dcm")
    
    if test_file:
        anonymize_dicom(test_file, "anonymized_CT_scan.dcm")
    else:
        print("Testdatei konnte nicht geladen werden.")