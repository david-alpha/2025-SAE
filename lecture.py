import re

def parse_ics(file_path):
    # Ouvrir le fichier .ics
    with open("testEv.ics", 'r', encoding='utf-8') as file:
        content = file.read()

    # Liste pour stocker les événements
    events = []

    # Expression régulière pour extraire les informations d'un événement
    event_pattern = re.compile(
        r'BEGIN:VEVENT.*?END:VEVENT', re.DOTALL)
    
    # Recherche de tous les événements dans le fichier
    events_raw = event_pattern.findall(content)

    for event in events_raw:
        event_data = {}

        # Extraction des informations spécifiques à partir des événements
        for key, pattern in {
            'DTSTAMP': r'DTSTAMP:(\S+)',
            'DTSTART': r'DTSTART:(\S+)',
            'DTEND': r'DTEND:(\S+)',
            'SUMMARY': r'SUMMARY:(.*?)(?=\n|$)',
            'LOCATION': r'LOCATION:(.*?)(?=\n|$)',
            'DESCRIPTION': r'DESCRIPTION:(.*?)(?=\n|$)',
            'UID': r'UID:(\S+)',
            'CREATED': r'CREATED:(\S+)',
            'LAST-MODIFIED': r'LAST-MODIFIED:(\S+)',
            'SEQUENCE': r'SEQUENCE:(\S+)'
        }.items():
            match = re.search(pattern, event)
            if match:
                event_data[key] = match.group(1).strip()

        events.append(event_data)

    return events


# Exemple d'utilisation
file_path = 'exemple.ics'  # Remplacez par le chemin de votre fichier ICS
events = parse_ics("testEv.ics")

# Affichage des événements extraits
for event in events:
    print("Événement:")
    for key, value in event.items():
        print(f"{key}: {value}")
    print("\n")