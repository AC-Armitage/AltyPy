import requests
import json
import sys
import time
import webbrowser


class Altypasser: 
	def __init__(self, target, main_url, main_headers, payload_header, cockie_jar, language):
		
		self.target = target
		self.main_url = main_url
		self.main_headers = main_headers
		self.payload_header = payload_header
		self.cockie_jar = cockie_jar
		self.language = language

	def counter(self):
	# Grabs info from the site and tries to sort it 
			try:
				print("Establishing connection...\n")
				response = requests.get(self.main_url, headers=self.main_headers)
				data = response.json()
				print("Connection established [Ok]\n\n")

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
			except requests.exceptions.ConnectionError:
				print ("Could not establish connection retying...")
				time.sleep(5)
				pass
			except:
				print("Could not establish connection!\nPlease check your network connectivity")

	def passer(self):
		# Sets up requests session so i wont have to rewrite the header and other details
			session = requests.Session()
			session.headers.update(self.payload_header)
			session.cookies.update(self.cockie_jar)
			try:
				print("\nSelecting target...\n")
				response = requests.get(self.main_url, headers=self.main_headers)
				data = response.json()
				print("Targets aquired [Ok]\n")
				stupid_target = data["externalId"]
			except requests.exceptions.ConnectionError:
				print("Could not establish connection retying...")
				time.sleep(5)
				pass
			except:
				print("Could not establish connection!\nPlease check your network connectivity")

			for mission in data["missions"]: 
				missionid = mission["externalId"]
				for lesson in mission["lessons"]:
					det_url = "https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/lessons/"+lesson["externalId"]+"?learningPathExternalId="+stupid_target

					try:
						det_response = requests.get(det_url, headers=self.main_headers)
					except requests.exceptions.ConnectionError:
						print("Could not establish data connection retying ")
						time.sleep(5)
						pass

					ev_mo_data = det_response.json()

					print("==============> "+ev_mo_data["externalId"])
					lessonid = lesson["externalId"]
					vfin_url = "https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/lessons/"+lessonid+"/activities?interfaceLanguage=fr_FR"
					
					if ev_mo_data["status"] != "VALIDATED":
							
							dones = 0
							while dones < target:

									for activity in ev_mo_data["activities"]:
											print(ev_mo_data["status"])
											activityid = activity["externalId"]
											failsafe_url = "https://app.ofppt-langues.ma/platform/#/learning-path/mission/"+missionid+"/lesson/"+lessonid+"/activity/"+activityid+"/exercise/item/0"
											ex_payload = {
													"externalActivityId": activity["externalId"],
													"externalLessonId": lessonid,
													"externalMissionId": missionid,
													"externalLearningPathId": stupid_target,
													"score": "100",
													"status": "SUCCESS"
												}


											print("Found activity: "+activity["externalId"]+" undone [X]")
											if activity["activityType"] == "EXERCISE" or activity["activityType"] == "SUMMARY_TEST" or activity["activityType"] == "WRITTEN_PRODUCTION":
												print("bypassing this exercise!")
												try:
													retries = 3
													while retries > 0:
														exfire = session.put(vfin_url, json=ex_payload)
														print("exercise payload up ")
														if exfire.status_code == 200:
															dones += 1
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
														sys.exit() 
												except requests.exceptions.ConnectionError:
													print("Connection refused retrying...")
													time.sleep(5)
													pass
											else:
												print("> Bypassing this video")
												try:
													vid_payload = {

														"externalActivityId": activityid,
														"externalLessonId": lessonid,
														"externalMissionId": missionid,
														"externalLearningPathId": stupid_target,
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
															dones +1
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
														sys.exit() 
												except requests.exceptions.ConnectionError:
													print("COnnection refused retrying...")
													time.sleep(5)
													pass  
							else:
								print("X+X+X+X+X+X+ I guess thats it +X+X+X+X+X+X\nAdios\nExiting program...")
								sys.exit()

												   

					elif ev_mo_data["status"] == "VALIDATED":
						print("Already validated skipping ")
						break

	def timeadd(self):
			licence = input("Enter your licenceid: ")
			info_url = "https://app.ofppt-langues.ma/gw//followupapi/main/followup/information/study-language/"+self.language
			live_url = "https://app.ofppt-langues.ma/gw//eventapi/main/api/event/internal/events"
			live_payload = {
				"action": "lc.application.alive",
				"licenseId": licence,
				"studyLg": self.language
				}
			dead_payload = {
				"action": "lc.application.dead",
				"licenseId": licence,
				"studyLg": self.language
			}

			timedemand = requests.get(info_url, headers=self.main_headers)
			timeinfo = timedemand.json()
			timespent = timeinfo["timespent"]["timespent"]
			try:
				timelimit = int(input("Aproximatly how much time do you want to add in seconds!!\nSkip if you dont want to set up a limit:"))
			except ValueError:
				timelimit = 999999999
				pass
			oldtime = timespent
			hours = timespent // 3600
			timespent  %= 3600
			minutes = timespent // 60
			print(f"You Have: {hours} hours, {minutes} minutes")
			timesession = requests.Session()
			timesession.headers.update(self.payload_header)
			start_time = time.time()
			
			while True:
				try:
					elapsed_time = time.time() - start_time
					live_payload['elapsed_time'] = elapsed_time
					keeper = timesession.post(live_url, json=live_payload)
					if keeper.status_code == 200:
						time.sleep(59)
						killer = timesession.post(live_url, json=dead_payload)
						if killer.status_code == 200:
							newtimedem = requests.get(info_url, headers=self.main_headers)
							if newtimedem.status_code == 200:
								newtime = newtimedem.json()
								newtimespent = newtime["timespent"]["timespent"]
								timeadded = newtimespent - oldtime 
								newhours = newtimespent // 3600
								print(f"[+] Total time added: {timeadded}s")
								if timeadded >= timelimit:
									print("X+X+X+X+X+X+ I guess thats it +X+X+X+X+X+X\nAdios\nExiting program...")
									sys.exit()
								else:	
									newtimespent %= 3600
									newmin = newtimespent // 60
									print(f"You now have: {newhours} hours, {newmin} minutes")
									pass
							else:
								print("Error fetching time ignoring")
								pass
							pass
						else:
							print("Dead Error")
						pass
					else:
						print("Error: maybe you entered some wrong information! ")
						pass
				except requests.exceptions.ConnectionError:
					print("Slow or no connection")
					continue
if __name__ == "__main__":
	print("Welcome\n!!!! Make sure that all the Inputs are correct and that the webpage language is set to french \n!!!! Before you start this program you must first have the main page open\n!!!! and  pass at least one task in the site manualy to be safe ")
	obj = input("What do you need!!\nby_pass\nadd_time\nEnter you objective here: ")
	cookie = input("input deviceuuid here: ")
	altoken = input("input x-altissia-token here: ")	
	try:
		target = int(input("How many lessons do you want to do? Skip if you only want to add time: "))
	except ValueError:
		target = 0
		pass
	language = input("Chose from the following:\nfr_FR\nen_GB\nes_ES\nThe language you wish to pass: ")
	main_url = "https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/user-learning-paths/language/"+language
	main_headers = {
			"Accept": "application/json, text/plain, */*",
			"Accept-Encoding": "gzip, deflate, br",
			"Accept-Language": "en-US,en;q=0.5",
			"Connection": "keep-alive",
			"Cookie": "deviceuuid="+cookie+"; NG_TRANSLATE_LANG_KEY=%22"+language+"%22",
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
			"Cookie": "deviceuuid="+cookie+"; NG_TRANSLATE_LANG_KEY=%22"+language+"%22",
			"Sec-Fetch-Dest": "empty",
			"Sec-Fetch-Mode": "cors",
			"Sec-Fetch-Site": "same-origin",
			"TE": "trailers",
			"Authorization": altoken
			}
	cockie_jar = {
			"deviceuuid": cookie,
			"NG_TRANSLATE_LANG_KEY": language
			}


	try:
		runny = Altypasser(target, main_url, main_headers, payload_header, cockie_jar, language)
		if obj == "by_pass":
			runny.counter()
			runny.passer()
		elif obj == "add_time":
			runny.timeadd()
		else:
			print("use a valid objective!!!")
	except KeyboardInterrupt:
		print("\n\nAdios\nExiting...")
		sys.exit()