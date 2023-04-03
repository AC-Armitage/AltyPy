import requests
import json

main_url = "https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/user-learning-paths/language/fr_FR"
main_headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Cookie": "deviceuuid=b773b828-b15a-41ec-b731-a2a389eb2e00; NG_TRANSLATE_LANG_KEY=%22en-GB%22",
    "Host": "app.ofppt-langues.ma",
    "Origin": "https://app.ofppt-langues.ma",
    "Referer": "https://app.ofppt-langues.ma/platform/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0",
    "x-altissia-token": "080840e715d2239e221000df8899e9199501142eccb564beef909414152d1672",
    "x-device-uuid": "b773b828-b15a-41ec-b731-a2a389eb2e00"

}
while True:
        try:
            #goal = every hole lmao
            goal = int(input("What level are you Aiming for! \n[1]==A1\n[2]==A1\n[3]==B1\n[4]==B2\n[5]==C1\n[6]==C2\n(To avoid being sussy dont go past B2)\nplease select a valid number: "))
            if goal < 1 or goal > 6:
                raise ValueError("Please enter a number between 1 and 6.")
            break
        except ValueError as e:
            print("Please eneter a valid number!!")      
def counter():
    response = requests.get(main_url, headers=main_headers)

    data = response.json()

    A1Mcount = 0
    A1count = 0
    A2count = 0
    B1count = 0
    B2count = 0
    C1count = 0
    for mission in data["missions"]:
        if mission['validated'] == False:
            for lesson in mission["lessons"]:
                if lesson["level"] == "A1_MINUS":
                    A1Mcount += 1
                elif lesson["level"] == "A1":
                    A1count += 1
                elif lesson["level"] == "A2":
                    A2count += 1
                elif lesson["level"] == "B1":
                    B1count += 1
                elif lesson["level"] == "B2":
                    B2count += 1
                elif lesson["level"] == "C1":
                    C1count += 1
    totalact = A1Mcount + A1count + A2count + B1count + B2count + C1count

    print(f"Total undone activities: {totalact}\n==> A1- activities: {A1Mcount}\n==> A1  activities: {A1count}\n==> A2  activities: {A2count}\n==> B1  activities: {B1count}\n==> B2  activities: {B2count}\n==> C1  activities: {C1count}\n\n=======================================================\n\n")
    print("These lessons are yet to be finished!!\n\n")
    for mission in data["missions"]:
        if mission['validated'] == False:
            for lesson in mission["lessons"]:
                if lesson["level"] == "A1_MINUS" and goal >= 1:
                    if lesson["status"] != "VALIDATED":
                        print(" (A1-)> " + lesson["title"])
                if lesson["level"] == "A1" and goal >= 2:
                    if lesson["status"] != "VALIDATED":
                        print(" (A1)> " + lesson["title"])
                if lesson["level"] == "A2" and goal >= 3:
                    if lesson["status"] != "VALIDATED":
                        print(" (A2)> " + lesson["title"])
                if lesson["level"] == "B1" and goal >= 4:
                    if lesson["status"] != "VALIDATED":
                        print(" (B1)> " + lesson["title"])
                if lesson["level"] == "B2" and goal >= 5:
                    if lesson["status"] != "VALIDATED":
                        print(" (B2)> " + lesson["title"])
                if lesson["level"] == "C1" and goal >= 6 :
                    if lesson["status"] != "VALIDATED":
                        print(" (C1)> " + lesson["title"])


def passer():
    payload_header ={
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "x-device-uuid": "b773b828-b15a-41ec-b731-a2a389eb2e00",
        "x-altissia-token": "080840e715d2239e221000df8899e9199501142eccb564beef909414152d1672",
        "Content-Type": "application/json",
        "Origin": "https://app.ofppt-langues.ma",
        "Connection": "keep-alive",
        "Referer": "https://app.ofppt-langues.ma/platform/",
        "Cookie": "deviceuuid=b773b828-b15a-41ec-b731-a2a389eb2e00; NG_TRANSLATE_LANG_KEY=%22fr-FR%22",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"    
    }
    response = requests.get(main_url, headers=main_headers)

    data = response.json()
    for mission in data["missions"]:
        for lesson in mission["lessons"]:
            det_url = "https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/lessons/"+lesson["externalId"]+"?learningPathExternalId=PROGRESS_IN_THE_LANGUAGE_FR_FR"
            det_response = requests.get(det_url, headers=main_headers)
            ev_mo_data = det_response.json()
            print("============== Working on lesson: "+ev_mo_data["externalId"]+" ==============\n")
            if ev_mo_data["level"] == "A1_MINUS" and goal >= 1:
                if ev_mo_data["status"] != "VALIDATED":
                    for activity in ev_mo_data["activities"]:
                        print("Found activity: "+activity["externalId"]+" undone [X]\n")
                        if activity["title"] == "video":
                            print("> bypassing this video\n ")
                            vid_payload = {
                                "externalActivityId": activity["externalId"],
                                "externalLessonId": "FR_FR_A1_MINUS_VOCABULARY_LES_CONSONNES_PREMIERE_PARTIE",
                                "externalMissionId": "PARLONS_FRANCAIS_A1",
                                "externalLearningPathId": "PROGRESS_IN_THE_LANGUAGE_FR_FR",
                                "status": "SUCCESS"
                            }
                            print("video payload up")
                            fire = requests.put(det_url, headers=payload_header, data=json.dumps(vid_payload))
                            print("payload sent")
                            try:
                                if fire.status_code >= 200 and fire.status_code < 300:
                                    print('activity successfully terminated [+]')
                                else:
                                    print('Request failed with status code:', response.status_code)
                            except Exception:
                                pass
                        else:
                            print("> bypassing this activity\n")        
                elif ev_mo_data["status"] == "VALIDATED":
                    for activity in ev_mo_data["activities"]:
                        print("Found activity:"+activity["externalId"]+" already done [V]\n")
counter()
passer()