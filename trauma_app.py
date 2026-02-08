### 2. The Code: trauma_app.py
This code uses a dictionary-based scoring system and file handling to save patient data.

```python
import datetime

def get_gcs_score():
    print("\n--- Glasgow Coma Scale Assessment ---")
    
    # Eye Opening (E)
    print("Eye Opening (1-4): [4] Spontaneous, [3] To sound, [2] To pressure, [1] None")
    e = int(input("Score: "))

    # Verbal Response (V)
    print("Verbal Response (1-5): [5] Oriented, [4] Confused, [3] Words, [2] Sounds, [1] None")
    v = int(input("Score: "))

    # Motor Response (M)
    print("Motor Response (1-6): [6] Obeys commands, [5] Localizing, [4] Normal flexion, [3] Abnormal flexion, [2] Extension, [1] None")
    m = int(input("Score: "))

    total = e + v + m
    
    if total <= 8:
        severity = "Severe (GCS ≤ 8)"
    elif 9 <= total <= 12:
        severity = "Moderate (GCS 9-12)"
    else:
        severity = "Mild (GCS 13-15)"
        
    return {"E": e, "V": v, "M": m, "total": total, "severity": severity}

def save_report(data, patient_id):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"Patient_{patient_id}_Report.txt"
    
    with open(filename, "w") as f:
        f.write(f"TRAUMA ASSESSMENT REPORT\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Patient ID: {patient_id}\n")
        f.write("-" * 25 + "\n")
        f.write(f"GCS Score: {data['total']}/15\n")
        f.write(f"Breakdown: E{data['E']}, V{data['V']}, M{data['M']}\n")
        f.write(f"Classification: {data['severity']}\n")
    
    print(f"\n✅ Report saved successfully as {filename}")

def main():
    p_id = input("Enter Patient ID/Initials: ")
    results = get_gcs_score()
    
    print(f"\nFinal Score: {results['total']}/15")
    print(f"Status: {results['severity']}")
    
    save_it = input("\nSave this report? (y/n): ")
    if save_it.lower() == 'y':
        save_report(results, p_id)

if __name__ == "__main__":
    main()
