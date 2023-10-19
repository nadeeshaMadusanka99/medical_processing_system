import json

class Patient:
    @staticmethod
    def read_sickness_details(patient_id):
        with open("data.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data['sickness_details']

            for detail in details:
                if detail['id'] == patient_id:
                    print(f"{detail['date']} - {detail['sickness']}")

    @staticmethod
    def read_drug_prescription(patient_id):
        with open("data.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data['drug_presc']

            for detail in details:
                if detail['id'] == patient_id:
                    print(f"{detail['date']} - {detail['drug_presc']}")

    @staticmethod
    def read_labtest_prescription(patient_id):
        with open("data.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data['labtest_presc']

            for detail in details:
                if detail['id'] == patient_id:
                    print(f"{detail['date']} - {detail['labtest_presc']}")
