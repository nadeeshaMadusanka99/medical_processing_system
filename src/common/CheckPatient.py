import json

def CheckPatient(patient_id):
    # Load user data from the config file
    with open("config.json", 'r') as data_file:
        f_data = json.load(data_file)
        users = f_data['users']
        
        # Check if the given patient ID corresponds to a patient
        for user in users:
            if patient_id == str(user['id']) and user['user_type'] == 'patient':
                return True
    return False  
