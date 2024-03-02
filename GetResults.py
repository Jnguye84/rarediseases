from get_ncts import get_ncts

def main(ncts):
    # import subprocess
    # subprocess.run(["pip", "install", "selenium"])
    import sys
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    class ClinicalTrialsInfo:
        def __init__(self, NCTid):
            self.url = "https://clinicaltrials.gov/study/" + str(NCTid).strip(',') # + "?aggFilters=results:with&rank=1&tab=results"
            self.adverse_events = None
            self.collaborators = None

        def get_adverse_events(self):
            driver = webdriver.Chrome()  # You can change this according to your WebDriver

            try:
                driver.get(self.url)
                element = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.ID, "adverse-events"))
                )

                element_list = element.text.split("\n")
                element_list = element_list[element_list.index('Serious Adverse Events'):]
                totals = []
                totals_indices = []
                for index, item in enumerate(element_list):
                    if "Total" in item.split(" "):
                        totals.append(item)
                        totals_indices.append(index)
                for index, item in enumerate(element_list):
                    if index > max(totals_indices) and "%" in list(item):
                        totals.append(item)

                self.adverse_events = totals

            finally:
                driver.quit()

        def get_collaborators(self):
            driver = webdriver.Chrome()  # You can change this according to your WebDriver

            try:
                driver.get(self.url)
                element = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "contacts-box"))
                )

                # Extract text within the "contacts-box" div
                contacts_text = element.text
                print(contacts_text)
                # Split the text based on newline character to get a list of lines
                contacts_lines = contacts_text.split("\n")

                # Extract collaborators by excluding the labels (e.g., "Sponsor", "Collaborators", "Investigators")
                colabs = [line.strip() for line in contacts_lines if line.lower() not in ["sponsor", "collaborators", "investigators"]]

                self.collaborators = colabs

            finally:
                driver.quit()

    def get_adverse_events(nct_list):
        adverse_events = []

        for nct in nct_list:
            try:
                trial_info = ClinicalTrialsInfo(nct)
                
                trial_info.get_adverse_events()

                adverse_events.append(trial_info.adverse_events)
            except Exception as e:
                
                # print(f"Error processing NCT ID {nct}: {str(e)}")
                adverse_events.append(None)  

        return adverse_events


    def get_collabs(nct_list):
        collabs = []

        for nct in nct_list:
            try:
                trial_info = ClinicalTrialsInfo(nct)
                
                trial_info.get_collaborators()

                collabs.append(trial_info.collaborators)
            except Exception as e:
                
                print(f"Error processing NCT ID {nct}: {str(e)}")
                collabs.append(None)  

        return collabs
    return get_collabs(ncts)
# print(main(['NCT04469283', 'NCT05136495', 'NCT04351360', 'NCT03481491']))
print(main(get_ncts("ADCY5")))
# def main():
#     if len(sys.argv) < 2:
#         print("Usage: python script.py NCTid1 NCTid2 NCTid3 ...")
#         sys.exit(1)

#     nct_list = sys.argv[1:]

#     adverse_events = get_adverse_events(nct_list)
#     collabs = get_collabs(nct_list)

#     for nct, events, collaborators in zip(nct_list, adverse_events, collabs):
#         print(f"NCT ID: {nct}")
#         # print("Adverse Events:", events, end='\n')
#         print("Collaborators:", collaborators)
#         # print("\n")
#         with open("temp_results.txt","a") as file:
#             file.write(f"NCT ID: {nct}, Adverse Events: {events}, Collaborators: {collaborators}")


# if __name__ == "__main__":
#     main()
# #call using python3 /Users/manas/Documents/GitHub/trading/virtenv/GetResults.py NCT02199574
    
# sys.exit()