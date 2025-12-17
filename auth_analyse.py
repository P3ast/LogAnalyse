import re 

def analyze_auth_logs(logs):
    with open(logs, 'r') as file:
        lines = file.readlines()
    failed_attempts = [line for line in lines if "Invalid user" in line]
    extracted_ips = []
    for attempt in failed_attempts:
        parts = attempt.split()
        for part in parts:
            if part.count('.') == 3 and all(0 <= int(num) < 256 for num in part.split('.') if num.isdigit()):
                extracted_ips.append(part)
                break
    return extracted_ips

if __name__ == "__main__":
    logs_file = input("Entrez le chemin du fichier de logs: ").strip()
    if not logs_file:
        print("Erreur: Aucun fichier fourni")
    else:
        try:
            results = analyze_auth_logs(logs_file)
            print(f"Nombre de tentatives échouées: {len(results)}")
            for attempt in results:
                print(f"  - {attempt.strip()}")
        except FileNotFoundError:
            print(f"Erreur: Le fichier '{logs_file}' n'existe pas")
        except Exception as e:
            print(f"Erreur: {e}")