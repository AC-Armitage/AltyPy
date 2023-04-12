import requests
import json
import sys
import time
import webbrowser
import customtkinter as ctk
import tkinter as tk 
import threading
import random



class Altypasser: 
    def __init__(self):
        self.godres = random.randint(70, 100)
        self.gui = ctk.CTk()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.gui.geometry("800x600")
        self.gui.title("AltyPy")
        self.infoframe = ctk.CTkFrame(master=self.gui)
        self.infoframe.pack(side="left", padx=5, fill="y")
        Image = tk.PhotoImage(file="/home/lolmeh/Downloads/images.png")
        Image_label = tk.Label(master=self.infoframe, image=Image).pack(pady=10, padx=10, anchor="n")
        Title = ctk.CTkLabel(master=self.infoframe, text="AltyPy", font=("Ariel", 30)).pack(pady=10, padx=10, anchor="n")
        Creds = ctk.CTkLabel(master=self.infoframe, text="By: AC-Armitage", font=("Ariel", 10)).pack(pady=10, padx=10, anchor="n")
        self.credframe = ctk.CTkFrame(master=self.gui)
        self.credframe.pack(pady=10, padx=15, fill="x")
        self.lice = ""

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
            self.main_url = "https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/user-learning-paths/language/"+self.language
            self.main_headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Cookie": "deviceuuid="+self.cookie+"; NG_TRANSLATE_LANG_KEY=%22"+self.language+"%22",
            "Host": "app.ofppt-langues.ma",
            "Origin": "https://app.ofppt-langues.ma",
            "Referer": "https://app.ofppt-langues.ma/platform/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0",
            "x-altissia-token": self.altoken,
            "x-device-uuid": self.cookie
            }
            self.payload_header = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0",
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate, br",
                    "x-device-uuid": self.cookie,
                    "x-altissia-token": self.altoken,
                    "Content-Type": "application/json",
                    "Origin": "https://app.ofppt-langues.ma",
                    "Connection": "keep-alive",
                    "Content-Length": "289",
                    "Host": "app.ofppt-langues.ma",
                    "Referer": "https://app.ofppt-langues.ma/platform/",
                    "Cookie": "deviceuuid="+self.cookie+"; NG_TRANSLATE_LANG_KEY=%22"+self.language+"%22",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "TE": "trailers",
                    "Authorization": self.altoken
                    }
            self.cockie_jar = {
                    "deviceuuid": self.cookie,
                    "NG_TRANSLATE_LANG_KEY": self.language
                    }
            if not self.cookie or not self.language or not self.obj:
                tk.messagebox.showwarning("Missing values", "Please fill in all fields.")
                return
            else:
                if self.obj == "Exercise":
                    print("exer")
                    self.passer()
                elif self.obj == "Time":
                    print("time")
                    self.timeadd()





        #credentials input 
        self.cookie = ctk.StringVar()
        self.altoken = ctk.StringVar()

        credtitle = ctk.CTkLabel(master=self.credframe, text="Credentials")
        credtitle.pack(pady=12, padx=1)
        uuidentry = ctk.CTkEntry(master=self.credframe, placeholder_text="Enter device-uuid: ")
        uuidentry.pack(pady=20, padx=60, fill="x", expand=True, )
        tokenentry = ctk.CTkEntry(master=self.credframe, placeholder_text="Enter Altisia-token: ")
        tokenentry.pack(pady=20, padx=60, fill="x", expand=True, )

        #langueage input
        lang = ctk.StringVar()
        
        langtitle = ctk.CTkLabel(master=self.credframe, text="Select language:")
        langtitle.pack(side="left", pady=8, padx=6)
        langfr = ctk.CTkRadioButton(master=self.credframe, value="fr_FR", text="Français", variable=lang)
        langen = ctk.CTkRadioButton(master=self.credframe, value="en_GB", text="English", variable=lang)
        langes = ctk.CTkRadioButton(master=self.credframe, value="es_ES", text="Español", variable=lang)
        langfr.pack(side="left", pady=20, padx=20)
        langen.pack(side="left", pady=20, padx=20)
        langes.pack(side="left", pady=20, padx=20)       
            
        #objective selection
        obj = ctk.StringVar()

        self.objframe = ctk.CTkFrame(master=self.gui)
        self.objframe.pack(fill="x", pady=5, padx=15)
        objtitle = ctk.CTkLabel(master=self.objframe, text="Select task:         ")
        objtitle.pack(side="left", pady=8, padx=6)
        ob_exerpass = ctk.CTkRadioButton(master=self.objframe, value="Exercise", text="Do exercises", variable=obj)
        ob_timepass = ctk.CTkRadioButton(master=self.objframe, value="Time", text="Add time", variable=obj)
        ob_exerpass.pack(side="left", pady=20, padx=20)
        ob_timepass.pack(side="left", pady=20, padx=20)

        def godeteleg():
            webbrowser.open("telegram.com")
        def godehub():
            webbrowser.open("https://github.com/AC-Armitage")
        self.submitbutton = ctk.CTkButton(master=self.gui, text="Submit", command=submit)
        self.submitbutton.pack(pady=15)
        telegbtn = ctk.CTkButton(master=self.infoframe, text="Telegram: @AC-Armitage", command=godeteleg).pack(side="bottom", anchor="s", padx=15, pady=10)
       # telegbtn.grid(row=1, column=0)
        githubtn = ctk.CTkButton(master=self.infoframe, text="     Github: AC-Armitage    ", command=godehub).pack(side="bottom", pady=10, padx=15)
        version = ctk.CTkLabel(master=self.infoframe, text="V0.45")
        version.pack(pady=5, padx=5, anchor="s",side="bottom")
        #githubtn.grid(row=0, column=0)
        def update_label():
            self.gui.after(20, update_label)
        update_label()
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
            self.credframe.pack_forget()
            self.objframe.pack_forget()
            self.submitbutton.pack_forget()
            def returnmain():
                pasframe.destroy()
                startbtn.destroy()
                self.credframe.pack()
                self.objframe.pack()
                self.submitbutton.pack()
                #confram.destroy()
                mainmenu.destroy()
                eventcon.destroy()
            pasframe = ctk.CTkFrame(master=self.gui)
            pasframe.pack(pady=15, padx=15, fill="both")
            exernumlabel = ctk.CTkLabel(master=pasframe, text="How many Lessons do you want to do:")
            exernumlabel.pack(side="left")
            exernumtry = ctk.CTkEntry(master=pasframe, placeholder_text="Exercise number")
            exernumtry.pack(pady=10, padx=10, side="right")
            def start():
                global eventcon
                #confram = ctk.CTkFrame(master=self.gui)
                #confram.pack(pady=20, padx=2, side="bottom", fill="x", expand=True, anchor="se")
                eventcon = tk.Text(master= self.gui, fg="#60b389",bg="#16181c", highlightthickness=0,)
                eventcon.pack(pady=20, padx=2, side="bottom", fill="x", anchor="s")
                target = int(exernumtry.get())
                exernumtry.configure(state="disabled")
                startbtn.configure(state="disabled")
                # Sets up requests session so i wont have to rewrite the header and other details
                session = requests.Session()
                session.headers.update(self.payload_header)
                session.cookies.update(self.cockie_jar)
                try:
                    print("\nSelecting target...\n")
                    eventcon.insert('end',"Selecting targets...\n")
                    response = requests.get(self.main_url, headers=self.main_headers)
                    data = response.json()
                    print("Targets aquired [Ok]\n")
                    eventcon.insert('end',"Target aquired [Ok]\n")
                    stupid_target = data["externalId"]
                except requests.exceptions.ConnectionError:
                    print("Could not establish connection retying...")
                    eventcon.insert('end',"Could not establish connection retying...\n")
                    time.sleep(5)
                    pass
                except:
                    print("Could not establish connection!\nPlease check your network connectivity")
                    eventcon.insert('end',"Could not establish connection!\nPlease check your network connectivity or the credentials!!\n")
                    sys.exit()

                for mission in data["missions"]: 
                    missionid = mission["externalId"]
                    for lesson in mission["lessons"]:
                        det_url = "https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/lessons/"+lesson["externalId"]+"?learningPathExternalId="+stupid_target

                        try:
                            det_response = requests.get(det_url, headers=self.main_headers)
                        except requests.exceptions.ConnectionError:
                            print("Could not establish data connection retying ")
                            eventcon.see("end")
                            eventcon.insert('end',"Could not grab data retying...\n")
                            time.sleep(5)
                            pass

                        ev_mo_data = det_response.json()

                        print("==============> "+ev_mo_data["externalId"])
                        eventcon.see("end")
                        eventcon.insert('end',"Found: "+ev_mo_data["externalId"]+"\n")
                        lessonid = lesson["externalId"]
                        vfin_url = "https://app.ofppt-langues.ma/gw//lcapi/main/api/lc/lessons/"+lessonid+"/activities?interfaceLanguage=fr_FR"
                        
                        if ev_mo_data["status"] != "VALIDATED":
                                
                                dones = 0
                                while dones < target:

                                        for activity in ev_mo_data["activities"]:
                                                print(ev_mo_data["status"])
                                                eventcon.see("end")
                                                eventcon.insert('end', ev_mo_data["status"]+"\n")
                                                activityid = activity["externalId"]
                                                failsafe_url = "https://app.ofppt-langues.ma/platform/#/learning-path/mission/"+missionid+"/lesson/"+lessonid+"/activity/"+activityid+"/exercise/item/0"
                                                ex_payload = {
                                                        "externalActivityId": activity["externalId"],
                                                        "externalLessonId": lessonid,
                                                        "externalMissionId": missionid,
                                                        "externalLearningPathId": stupid_target,
                                                        "score": self.godres,
                                                        "status": "SUCCESS"
                                                    }


                                                print("Found activity: "+activity["externalId"]+" undone [X]")
                                                eventcon.see("end")
                                                eventcon.insert('end',"Found activity: "+activity["externalId"]+" undone [X]\n")

                                                if activity["activityType"] == "EXERCISE" or activity["activityType"] == "SUMMARY_TEST" or activity["activityType"] == "WRITTEN_PRODUCTION":
                                                    print("bypassing this exercise!")
                                                    eventcon.see("end")
                                                    eventcon.insert('end',"bypassing this exercise...\n")
                                                    try:
                                                        retries = 3
                                                        while retries > 0:
                                                            exfire = session.put(vfin_url, json=ex_payload)
                                                            print("exercise payload up ")
                                                            if exfire.status_code == 200:
                                                                dones += 1
                                                                print('[OK]\nEx successfully terminated [+]')
                                                                eventcon.see("end")
                                                                eventcon.insert('end',"[OK]\nEx successfully terminated [+]\n")
                                                                break
                                                            else:
                                                                print("Error")
                                                                eventcon.see("end")
                                                                eventcon.insert('end',"Error\n")
                                                                webbrowser.open(failsafe_url, new=0)
                                                                time.sleep(10)
                                                                print("Retrying...")
                                                                eventcon.see("end")
                                                                eventcon.insert('end',"Retrying...\n")
                                                                retries -= 1
                                                        if retries == 0:
                                                            print("Request failed after multiple retries.")
                                                            eventcon.see("end")
                                                            eventcon.insert('end',"Request failed after multiple retries!\n")
                                                            sys.exit() 
                                                    except requests.exceptions.ConnectionError:
                                                        print("Connection refused retrying...")
                                                        eventcon.see("end")
                                                        eventcon.insert('end',"Connection refused retrying...\n")
                                                        time.sleep(5)
                                                        pass
                                                else:
                                                    print("> Bypassing this video")
                                                    eventcon.see("end")
                                                    eventcon.insert('end',"bypassing this video...\n")
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
                                                            eventcon.see("end")
                                                            eventcon.insert('end',"Video payload up\n")                                
                                                            if vfire.status_code == 200:
                                                                dones +1
                                                                print('[OK]\nVideo successfully terminated [+]')
                                                                eventcon.see("end")
                                                                eventcon.insert('end',"[OK]\nVideo successfully terminated [+]\n")   

                                                                break
                                                            else:
                                                                print("Error")
                                                                eventcon.see("end")
                                                                eventcon.insert('end',"[Error\n")  
                                                                webbrowser.open(failsafe_url, new=0)
                                                                time.sleep(10)
                                                                print("Retrying...")
                                                                eventcon.see("end")
                                                                eventcon.insert('end',"Retrying...\n")
                                                                retries -= 1
                                                        if retries == 0:
                                                            print("Request failed after multiple retries.")
                                                            eventcon.see("end")
                                                            eventcon.insert('end',"Request failed after multiple retries!\n")
                                                            sys.exit() 
                                                    except requests.exceptions.ConnectionError:
                                                        print("Connection refused retrying...")
                                                        eventcon.see("end")
                                                        eventcon.insert('end',"Connection refused retrying...\n")
                                                        time.sleep(5)
                                                        pass  
                                else:
                                    print("X+X+X+X+X+X+ I guess thats it +X+X+X+X+X+X\nAdios\nExiting program...")
                                    eventcon.see("end")
                                    eventcon.insert('end',"X+X+X+X+X+X+ I guess thats it +X+X+X+X+X+X\nAdios\nExiting program...\n")

                                    sys.exit()

                                                       

                        elif ev_mo_data["status"] == "VALIDATED":
                            print("Already validated skipping ")
                            eventcon.see("end")
                            eventcon.insert('end',"Already validated skipping \n")
                            break
            def starthh():
                threading.Thread(target=start).start()
                return
            startbtn = ctk.CTkButton(master=self.gui, text="Start", command=starthh)
            startbtn.pack(pady=15, padx=25, anchor="ne")
            mainmenu = ctk.CTkButton(master=self.infoframe, text="< Main menu", command=returnmain)
            mainmenu.pack(pady=10, padx=10)
            self.gui.mainloop()

    def timeadd(self):
            self.credframe.pack_forget()
            self.objframe.pack_forget()
            self.submitbutton.pack_forget()
            #self.gui.withdraw()
            #timegui = ctk.CTkToplevel(self.gui)
            #timegui.geometry("820x500")
            #timegui.title("AltyPy/Timeadd")
            #opframe = ctk.CTkFrame(master=self.gui)
            #opframe.pack(side="left", fill="y")
            #go_back_button = ctk.CTkButton(master=self.infoframe, text="< Main page", command=lambda: [timegui.destroy(), self.gui.deiconify()])
           #go_back_button.pack(pady=15, padx=20)
            optfr = ctk.CTkFrame(master=self.gui)
            #optfr.pack()
            #licence = input("Enter your licenceid: ")
            def returnmain():
                timeadentry.destroy()
                startbutt.destroy()
                mainmenu.destroy()
                self.credframe.pack()
                self.objframe.pack()
                self.submitbutton.pack()
                timeaframe.destroy()
                return
#           def stoptimedef():
#                   global stoptimebtn
#                   self.stop_time = True
#                   mainmenu.configure(state="enabled")
#                   stoptimebtn.destroy()
            def start():
#               while not self.stop_time
                    global stoptimebtn
                    reqi = requests.get("https://app.ofppt-langues.ma/gw//followupapi/main/followup/information/study-language/"+self.language, headers=self.main_headers )
                    licdata = reqi.json()
                    licence = licdata["languageAssessmentLicenseId"]
                    mainmenu.configure(state="enabled")
                    stoptimebtn = ctk.CTkButton(master=self.infoframe, text="Stop", command=stoptimedef)
                    stoptimebtn.pack(pady=15, padx=15)
                    mainmenu.configure(state="disabled")
                    timelimit = int(timeadentry.get())
                    print(licence)
                    print(timelimit)
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
                    oldtime = timespent
                    hours = timespent // 3600
                    timespent  %= 3600
                    minutes = timespent // 60
                    print(f"You Have: {hours} hours, {minutes} minutes")
                    clockframe = ctk.CTkFrame(master=self.gui)
                    clockframe.pack(pady=20, padx=20)
                    newclockframe = ctk.CTkFrame(master=self.gui)
                    newclockframe.pack(pady=20, padx=20)
                    youhade = ctk.CTkLabel(master=clockframe, text="You had: ")
                    youhade.pack(side="left", pady=10, padx=10)
                    newtimeptxt = tk.Text(master=newclockframe, fg="#60b389",bg="#16181c", highlightthickness=0, font=("Ariel", 50))
                    newtimeptxt.pack(pady=2, padx=2, fill="x", expand=True)
                    clock_label = ctk.CTkLabel(master=clockframe, text=f"{hours}:{minutes}", font=("Ariel", 80))
                    clock_label.pack(pady=10)
                    self.gui.update()
                    timesession = requests.Session()
                    timesession.headers.update(self.payload_header)
                    start_time = time.time()
            
                    while True:
                        try:
                            self.gui.update()
                            elapsed_time = time.time() - start_time
                            live_payload['elapsed_time'] = elapsed_time
                            keeper = timesession.post(live_url, json=live_payload)
                            if keeper.status_code == 200:
                                time.sleep(62)
                                #self.gui.after()
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
                                            newtimeptxt.delete("1.0",tk.END)
                                            newtimeptxt.insert('end', f'You now have: {newhours}:{newmin}\n')
                                            newclockframe.update()
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

                #else:
                #   print("Time terminated")
            def stoptimedef():
                global stoptimebtn
                self.stop_time = True
                mainmenu.configure(state="enabled")
                startbutt.configure(state="enabled")
                stoptimebtn.destroy()
                clockframe.destroy()
                newclockframe.destroy()
            def starthh():
                threading.Thread(target=start).start()
                return
            stop_time = False 
            #optfr = ctk.CTkFrame(master=timegui).pack(side="left", fill="x", pady=10)
            timeaframe = ctk.CTkFrame(master=self.gui)
            timeaframe.pack(padx=10, pady=2, fill="x", expand=True, anchor="ne")
            timetrylabel = ctk.CTkLabel(master=timeaframe, text="How much time you want to add: ")
            timetrylabel.pack(side="left", pady=10, padx=10)
            timeadentry = ctk.CTkEntry(master=timeaframe, placeholder_text="in seconds")
            timeadentry.pack(padx=15, pady=10, side="right")
            startbutt = ctk.CTkButton(master=self.gui, text="Start", command=starthh)
            startbutt.pack(pady=15, padx=25, anchor="ne")
            #def update_self.gui():
           #     self.gui.update()
          #  self.gui.after(200, update_self.gui)
            mainmenu = ctk.CTkButton(master=self.infoframe, text="< Main menu", command=returnmain)
            mainmenu.pack(pady=10, padx=10)
            self.gui.mainloop()
if __name__ == "__main__":
    Altypasser = Altypasser()