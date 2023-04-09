import requests
import json
import sys
import time
import webbrowser
import customtkinter as ctk
import tkinter as tk 



class Altypasser: 
    def __init__(self):
        self.gui = ctk.CTk()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.gui.geometry("820x500")
        self.gui.title("AltyPy")
        credframe = ctk.CTkFrame(master=self.gui)
        credframe.pack(pady=10, padx=15, fill="x")

        def get_creds():
            self.cookie = uuidentry.get()
            self.altoken = tokenentry.get()
            print(f"Deviceuuid: {self.cookie}")
            print(f"Altisia-token: {self.altoken}")
            return self.cookie
            return self.altoken 
        def set_lang():
            self.language = lang.get()
            print(f"Language: {self.language}")
            return self.language
        def set_obj():
            self.obj = obj.get()
            print(f"Objective: {self.obj}")
            return self.obj
        def submit():
            get_creds()
            set_lang()
            set_obj()
            if not self.cookie or not self.language or not self.obj:
                logbar.insert("end", "Please fill in all fields.\n")
                tk.messagebox.showwarning("Missing values", "Please fill in all fields.")
                return
            else:
                logbar.insert("end", f"Deviceuuid: {self.cookie}\n")
                logbar.insert("end", f"Altisia-token: {self.altoken}\n")
                logbar.insert("end", f"Language: {self.language}\n")
                logbar.insert("end", f"Objective: {self.obj}\n")
                if self.obj == "Exercise":
                    print("exer")
                elif self.obj == "Time":
                    print("time")
                    self.timeadd()





        #credentials input 
        self.cookie = ctk.StringVar()
        self.altoken = ctk.StringVar()

        credtitle = ctk.CTkLabel(master=credframe, text="Credentials")
        credtitle.pack(pady=12, padx=1)
        uuidentry = ctk.CTkEntry(master=credframe, placeholder_text="Enter device-uuid: ")
        uuidentry.pack(pady=20, padx=60, fill="x", expand=True, )
        tokenentry = ctk.CTkEntry(master=credframe, placeholder_text="Enter Altisia-token: ")
        tokenentry.pack(pady=20, padx=60, fill="x", expand=True, )

        #langueage input
        lang = ctk.StringVar()
        
        langtitle = ctk.CTkLabel(master=credframe, text="Select language:")
        langtitle.pack(side="left", pady=8, padx=6)
        langfr = ctk.CTkRadioButton(master=credframe, value="fr_FR", text="Français", variable=lang)
        langen = ctk.CTkRadioButton(master=credframe, value="en_GB", text="English", variable=lang)
        langes = ctk.CTkRadioButton(master=credframe, value="es_ES", text="Español", variable=lang)
        langfr.pack(side="left", pady=20, padx=20)
        langen.pack(side="left", pady=20, padx=20)
        langes.pack(side="left", pady=20, padx=20)       
            
        #objective selection
        obj = ctk.StringVar()

        objframe = ctk.CTkFrame(master=self.gui)
        objframe.pack(fill="x", pady=5, padx=15)
        objtitle = ctk.CTkLabel(master=objframe, text="Select task:         ")
        objtitle.pack(side="left", pady=8, padx=6)
        ob_exerpass = ctk.CTkRadioButton(master=objframe, value="Exercise", text="Do exercises", variable=obj)
        ob_timepass = ctk.CTkRadioButton(master=objframe, value="Time", text="Add time", variable=obj)
        ob_exerpass.pack(side="left", pady=20, padx=20)
        ob_timepass.pack(side="left", pady=20, padx=20)

        submitbutton = ctk.CTkButton(master=self.gui, text="Submit", command=submit).pack(pady=15)
        
        logtitle = ctk.CTkLabel(master=self.gui, text="Logs: ").pack(side="left", pady=1, padx=1)
        logframe = ctk.CTkFrame(master=self.gui)
        #logframe.pack(fill="both", expand=True)
        logbar = ctk.CTkTextbox(master=self.gui)
        logbar.pack(fill="x", padx=10, pady=5, expand=True)
        self.gui.mainloop()

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
            self.gui.withdraw()
            timegui = ctk.CTkToplevel(self.gui)
            timegui.geometry("820x500")
            timegui.title("AltyPy/Timeadd")
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
            timegui.focus_set()
            timegui.mainloop()
if __name__ == "__main__":
    Altypasser = Altypasser()