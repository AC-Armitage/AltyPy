import requests
import json
import sys
import time
import webbrowser


class Altypasser: 
	def __init__(self, goal, target, main_url, main_headers, payload_header):
		
		self.goal = goal
		self.target = target
		self.main_url = main_url
		self.main_headers = main_headers
		self.payload_header = payload_header

	def counter(self):

		    response = requests.get(self.main_url, headers=self.main_headers)
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


	def passer(self):
		    session = requests.Session()
		    session.headers.update(self.payload_header)
		    session.cookies.update({
		        "deviceuuid": "765ac311-899e-41ca-8e4a-b671470c5cc7",
		        "NG_TRANSLATE_LANG_KEY": "fr-FR"
		        })

		    response = requests.get(self.main_url, headers=self.main_headers)
		    data = response.json()
		    for mission in data["missions"]: 
		        missionid = mission["externalId"]
		        for lesson in mission["lessons"]:
		            det_url = "https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/lessons/"+lesson["externalId"]+"?learningPathExternalId=PROGRESS_IN_THE_LANGUAGE_FR_FR"
		            det_response = requests.get(det_url, headers=self.main_headers)
		            ev_mo_data = det_response.json()
		            print("============== Working on lesson: "+ev_mo_data["externalId"]+" ==============")
		            lessonid = lesson["externalId"]
		            vfin_url = "https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/lessons/"+lessonid+"/activities?interfaceLanguage=fr_FR"
		            
		            get_url = "https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/lessons/"+lessonid+"?learningPathExternalId=PROGRESS_IN_THE_LANGUAGE_FR_FR"


		            if ev_mo_data["level"] == target and ev_mo_data["status"] != "VALIDATED": 
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


		                        print("Found activity: "+activity["externalId"]+" undone [X]")
		                        if activity["activityType"] == "EXERCISE" or activity["activityType"] == "SUMMARY_TEST" or activity["activityType"] == "WRITTEN_PRODUCTION":
		                            print("bypassing this exercise!")
		                            retries = 3
		                            while retries > 0:
		                                exfire = session.put(vfin_url, json=ex_payload)
		                                print("exercise payload up")
		                                if exfire.status_code == 200:
		                                    print('[OK]\nEx successfully terminated [+]')
		                                    break
		                                else:
		                                    print("Error")
		                                    webbrowser.open(failsafe_url, new=0)
		                                    time.sleep(10)
		                                    print("Retrying...")
		                                    retries -= 1
		                            if retries == 0:
		                                print("Request failed after multiple retries.")
		                                sys.close() 
		                        else:
		                            print("> Bypassing this video")
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
		                            retries = 3
		                            while retries > 0:
		                                vfire = session.put(vfin_url, json=vid_payload)
		                                print("Video payload up")                                
		                                if vfire.status_code == 200:
		                                    print('[OK]\nVideo successfully terminated [+]')
		                                    break
		                                else:
		                                    print("Error")
		                                    webbrowser.open(failsafe_url, new=0)
		                                    time.sleep(10)
		                                    print("Retrying...")
		                                    retries -= 1
		                            if retries == 0:
		                                print("Request failed after multiple retries.")
		                                sys.close()   
		                            
		                                       

		            elif ev_mo_data["status"] == "VALIDATED":
		                print("Already validated [V]")
		                break
	def timeadd(self):
		live_url = "https://app.ofppt-langues.ma/gw//eventapi/main/api/event/internal/events"
		time_payload = {
			"action": "lc.application.alive",
			"licenseId": "4449570",
			"studyLg": "fr_FR"
		}
		timesession = requests.Session()
		timesession.headers.update(self.payload_header)
		start_time = time.time()

		while True:
		    elapsed_time = time.time() - start_time
		    time_payload['elapsed_time'] = elapsed_time
		    keeper = timesession.post(live_url, json=time_payload)
		   
		    if keeper.status_code == 200:
		    	print("[OK]\n[T] 15 seconds have been added")
		    else:
		    	print("Error")
		    	pass

		    time.sleep(15)

if __name__ == "__main__":
	cookie = input("input deviceuuid here: ")
	altoken = input("input x-altissia-token here: ")
	while True:
	        try:
	            #goal = every hole lmao
	            goal = int(input("What level are you Aiming for! \n[1]==A1\n[2]==A2\n[3]==B1\n[4]==B2\n[5]==C1\n[6]==C2\n(To avoid being sussy dont go past B2)\nplease select a valid number: "))
	            if goal < 1 or goal > 6:
	                raise ValueError("Please enter a number between 1 and 6.")
	            break
	        except ValueError as e:
	            print("Please eneter a valid number!!") 
	goal_to_target = {
    1: "A1_MINUS",
    2: "A1",
    3: "A2",
    4: "B1",
    5: "B2",
    6: "C1"
	}

	target = goal_to_target[goal]
	#target = input("eneter a valid goal A1-/A1/A2/B1/B2/C1/C2: ")

	main_url = "https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/user-learning-paths/language/fr_FR"

	main_headers = {
		"Accept": "application/json, text/plain, */*",
	    "Accept-Encoding": "gzip, deflate, br",
	    "Accept-Language": "en-US,en;q=0.5",
	    "Connection": "keep-alive",
	    "Cookie": "deviceuuid="+cookie+"; NG_TRANSLATE_LANG_KEY=%22fr-FR%22",
	    "Host": "app.ofppt-langues.ma",
	    "Origin": "https://app.ofppt-langues.ma",
	    "Referer": "https://app.ofppt-langues.ma/platform/",
	    "Sec-Fetch-Dest": "empty",
	    "Sec-Fetch-Mode": "cors",
	    "Sec-Fetch-Site": "same-origin",
	    "TE": "trailers",
	    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0",
	    "x-altissia-token": altoken,
	    "x-device-uuid": cookie
			}
	payload_header = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0",
			"Accept": "application/json, text/plain, */*",
			"Accept-Language": "en-US,en;q=0.5",
			"Accept-Encoding": "gzip, deflate, br",
			"x-device-uuid": cookie,
			"x-altissia-token": altoken,
			"Content-Type": "application/json",
			"Origin": "https://app.ofppt-langues.ma",
			"Connection": "keep-alive",
			"Content-Length": "289",
			"Host": "app.ofppt-langues.ma",
			"Referer": "https://app.ofppt-langues.ma/platform/",
			"Cookie": "deviceuuid="+cookie+"; NG_TRANSLATE_LANG_KEY=%22fr-FR%22",
			"Sec-Fetch-Dest": "empty",
			"Sec-Fetch-Mode": "cors",
			"Sec-Fetch-Site": "same-origin",
			"TE": "trailers",
			"Authorization": altoken
			}


	runny = Altypasser(target, goal, main_url, main_headers, payload_header)
	#runny.counter()
	#runny.passer()
	runny.timeadd()
