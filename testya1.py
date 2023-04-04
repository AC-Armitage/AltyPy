import requests
import json
import sys
import time
import webbrowser
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

#while True:
#        try:
#            #goal = every hole lmao
#            goal = int(input("What level are you Aiming for! \n[1]==A1\n[2]==A1\n[3]==B1\n[4]==B2\n[5]==C1\n[6]==C2\n(To avoid being sussy dont go past B2)\nplease select a valid number: "))
#            if goal < 1 or goal > 6:
#                raise ValueError("Please enter a number between 1 and 6.")
#            break
#        except ValueError as e:
#            print("Please eneter a valid number!!")      
goal = 2
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
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "x-device-uuid": "b773b828-b15a-41ec-b731-a2a389eb2e00",
        "x-altissia-token": "080840e715d2239e221000df8899e9199501142eccb564beef909414152d1672",
        "Content-Type": "application/json",
        "Origin": "https://app.ofppt-langues.ma",
        "Connection": "keep-alive",
        "Content-Length": "289",
        "Host": "app.ofppt-langues.ma",
        "Referer": "https://app.ofppt-langues.ma/platform/",
        "Cookie": "deviceuuid=b773b828-b15a-41ec-b731-a2a389eb2e00; NG_TRANSLATE_LANG_KEY=%22fr-FR%22",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
        "Authorization": "080840e715d2239e221000df8899e9199501142eccb564beef909414152d1672"
    })
    session.cookies.update({
        "deviceuuid": "b773b828-b15a-41ec-b731-a2a389eb2e00",
        "NG_TRANSLATE_LANG_KEY": "fr-FR"
        })

    response = requests.get(main_url, headers=main_headers)
    data = response.json()
    for mission in data["missions"]: 
        missionid = mission["externalId"]
        for lesson in mission["lessons"]:
            live_url = "https://app.ofppt-langues.ma/gw//eventapi/main/api/event/internal/events"
            det_url = "https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/lessons/"+lesson["externalId"]+"?learningPathExternalId=PROGRESS_IN_THE_LANGUAGE_FR_FR"
            det_response = requests.get(det_url, headers=main_headers)
            ev_mo_data = det_response.json()
            print("============== Working on lesson: "+ev_mo_data["externalId"]+" ==============\n")
            lessonid = lesson["externalId"]
            vfin_url = "https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/lessons/"+lessonid+"/activities?interfaceLanguage=fr_FR"
            get_url = "https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/lessons/"+lessonid+"?learningPathExternalId=PROGRESS_IN_THE_LANGUAGE_FR_FR"
            
#A1-
            if ev_mo_data["level"] == "A1" and goal >= 2 and ev_mo_data["status"] != "VALIDATED": 
                    for activity in ev_mo_data["activities"]:
                        activityid = activity["externalId"]
                        failsafe_url = "https://app.ofppt-langues.ma/platform/#/learning-path/mission/"+missionid+"/lesson/"+lessonid+"/activity/"+activityid+"/exercise/item/0"
                        ex_payload = {
                                "externalActivityId": activity["externalId"],
                                "externalLessonId": lessonid,
                                "externalMissionId": missionid,
                                "externalLearningPathId": "PROGRESS_IN_THE_LANGUAGE_FR_FR",
                                "score": "100",
                                "status": "SUCCESS"
                            }


                        print("Found activity: "+activity["externalId"]+" undone [X]\n")
                        if activity["activityType"] == "EXERCISE" or activity["activityType"] == "SUMMARY_TEST" or activity["activityType"] == "WRITTEN_PRODUCTION":
                            print("bypassing this exercise!\n")
                           
                            print("Activity payload up")
                            while True:
                                print(vfin_url)
                                exfire = session.put(vfin_url, json=ex_payload, timeout=10)

                                if exfire.status_code == 200:
                                    print('Activity successfully terminated [+]')
                                    break
                                else:
                                    webbrowser.open(failsafe_url)
                                    time.sleep(1)
                                    print("something went wrong !!!")
                                    pass
                        else:
                            print("> Bypassing this video\n")
                            vid_payload = {

                                "externalActivityId": activityid,
                                "externalLessonId": lessonid,
                                "externalMissionId": missionid,
                                "externalLearningPathId": "PROGRESS_IN_THE_LANGUAGE_FR_FR",
                                "status": "SUCCESS"
                            }
                            vid_payload2 = {
                                "externalActivityId":activityid,
                                "externalLessonId":lessonid,
                                "status": "SUCCESS"
                            }
                                
                            vfire = session.put(vfin_url, json=vid_payload)
                            print(vfire.status_code)
                            print("Video payload up")
                            if vfire.status_code == 200:
                                print('Video successfully terminated [+]')
                                break
                            else:
                                webbrowser.open("failsafe_url")
                                time.sleep(1)
                                print("hmmm")
                                pass      
                            pass
                                       

            elif ev_mo_data["status"] == "VALIDATED":
                     #pass
                
                for activity in ev_mo_data["activities"]:
                    print("Found activity:"+activity["externalId"]+" already done [V]\n")
                    break 
#counter()          
passer()
