import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected string, got {type(template).__name__}.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Invalid input type for attendees. Expected list of dictionaries.")
        return
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    for index, attendee in enumerate(attendees, start=1):
        processed_content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None: value = "N/A"
            processed_content = processed_content.replace("{" + key + "}", str(value))
        with open(f"output_{index}.txt", 'w') as f:
            f.write(processed_content)
