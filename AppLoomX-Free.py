import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
import pyautogui
import webbrowser

webbrowser.open("https://discord.gg/qA7trgxdVD")

time.sleep(5)

pyautogui.alert("AppLoomX'e hoşgeldiniz!")

uygulamalar = {
    "7-Zip": "7zip.7zip",
    "Adobe Acrobat Reader (64-bit)": "Adobe.Acrobat.Reader.64-bit",
    "Adobe Creative Cloud": "XPDLPKWG9SW2WD",
    "Adobe Express": "9P94LH3Q1CP5",
    "Adobe Photoshop": "XPFD4T9N395QN6",
    "AIMP": "AIMP.AIMP",
    "Android Studio": "Google.AndroidStudio",
    "AnyDesk": "AnyDesk.AnyDesk",
    "Audacity": "Audacity.Audacity",
    "Battle.net": "Blizzard.BattleNet",
    "Bitdefender Total Security": "XP9K931FWBP5V5",
    "Bitwarden": "Bitwarden.Bitwarden",
    "Blender (Önerimdir)": "9PP3C07GTVRH",
    "BlueStacks": "BlueStack.BlueStacks",
    "Brave Browser (Önerimdir)": "Brave.Brave",
    "CCleaner": "Piriform.CCleaner",
    "CPU-Z": "CPUID.CPU-Z",
    "CrystalDiskInfo": "CrystalDiskInfo.CrystalDiskInfo",
    "DaVinci Resolve": "BlackmagicDesign.DaVinciResolve",
    "DBeaver": "DBeaver.DBeaver",
    "DeepL Translator": "XPDNX7G06BLH2G",
    "Discord": "Discord.Discord",
    "Disney+": "9NXQXXLFST89",
    "Docker Desktop": "Docker.DockerDesktop",
    "Dropbox": "Dropbox.Dropbox",
    "EA App": "ElectronicArts.EADesktop",
    "Epic Games Launcher": "EpicGames.EpicGamesLauncher",
    "Everything": "voidtools.Everything",
    "ExpressVPN": "ExpressVPN.ExpressVPN",
    "Figma": "Figma.Figma",
    "FileZilla": "FileZilla.FileZilla",
    "Firefox": "Mozilla.Firefox",
    "GIMP": "GIMP.GIMP",
    "GIMP (Önerimdir)": "9PNSJCLXDZ0V",
    "Git": "Git.Git",
    "GitHub Desktop": "GitHub.GitHubDesktop",
    "GOG Galaxy": "GOG.GOGGalaxy",
    "Google Chrome": "Google.Chrome",
    "Google Drive": "Google.GoogleDrive",
    "Inkscape": "Inkscape.Inkscape",
    "JDownloader": "JDownloader.JDownloader",
    "Java Runtime Environment": "Oracle.JavaRuntimeEnvironment",
    "JetBrains Toolbox": "JetBrains.Toolbox",
    "KeePass": "KeePassXCTeam.KeePassXC",
    "Krita": "Krita.Krita",
    "LibreOffice": "TheDocumentFoundation.LibreOffice",
    "Logitech G HUB": "Logitech.GHUB",
    "Malwarebytes": "Malwarebytes.Malwarebytes",
    "Microsoft Teams": "Microsoft.Teams",
    "Microsoft Visual C++ Redistributable": "Microsoft.VCRedist.2015+.x64",
    "Mozilla Thunderbird": "Mozilla.Thunderbird",
    "MSI Afterburner": "MSI.Afterburner",
    "MySQL": "Oracle.MySQL",
    ".NET Runtime 9.0": "Microsoft.DotNet.Runtime.9",
    ".NET SDK 9": "Microsoft.DotNet.SDK.9",
    "Netflix": "9WZDNCRFJ3TJ",
    "NordVPN": "NordVPN.NordVPN",
    "Notepad++": "Notepad++.Notepad++",
    "Node.js (LTS)": "OpenJS.NodeJS.LTS",
    "NVIDIA GeForce Experience": "NVIDIA.GeForceExperience",
    "OBS Studio": "OBSProject.OBSStudio",
    "Opera Browser": "XP8CF6S8G2D5T6",
    "Opera GX": "XPDBZ4MPRKNN30",
    "Origin": "ElectronicArts.Origin",
    "PatchMyPC": "PatchMyPC.PatchMyPC",
    "Postman": "Postman.Postman",
    "PowerToys": "Microsoft.PowerToys",
    "Proton VPN (Önerimdir)": "Proton.ProtonVPN",
    "PuTTY": "PuTTY.PuTTY",
    "Python (Son Sürüm)": "Python.Python.3.13",
    "PyCharm": "JetBrains.PyCharm",
    "qBittorrent": "qBittorrent.qBittorrent",
    "Revo Uninstaller": "RevoUninstaller.RevoUninstaller",
    "Rufus": "Rufus.Rufus",
    "Slack": "SlackTechnologies.Slack",
    "Snappy Driver Installer Origin (Sürücü Kurma Programı)": "GlennDelahoy.SnappyDriverInstallerOrigin",
    "Spotify": "Spotify.Spotify",
    "Spotify (Önerimdir)": "Spotify.Spotify",
    "Steam": "Valve.Steam",
    "SteamVR": "Valve.SteamVR",
    "Stream Deck": "Elgato.StreamDeck",
    "TeamSpeak": "XPDCJ80KGNRVSS",
    "TeamViewer": "TeamViewer.TeamViewer",
    "Telegram": "Telegram.TelegramDesktop",
    "Trello": "Trello.Trello",
    "Twitch": "Twitch.Twitch",
    "Ubisoft Connect": "Ubisoft.Connect",
    "Unreal Engine": "EpicGames.UnrealEngine",
    "Unity Hub": "UnityTechnologies.UnityHub",
    "uTorrent": "uTorrent.uTorrent",
    "VirtualBox": "Oracle.VirtualBox",
    "Visual Studio": "Microsoft.VisualStudio",
    "Visual Studio Code": "Microsoft.VisualStudioCode",
    "Vivaldi Browser (Özelleştirme delilerine)": "XP99GVQDX7JPR4",
    "VLC Media Player": "VideoLAN.VLC",
    "VLC media player": "VideoLAN.VLC",
    "WhatsApp": "9NKSQGP7F2NH",
    "WinRAR": "RARLab.WinRAR",
    "Wireshark": "WiresharkFoundation.Wireshark",
    "Wondershare PDF Reader": "Wondershare.PDFReader",
    "WPS Office": "Kingsoft.WPSOffice",
    "Zoom": "Zoom.Zoom",
    "Zotero": "Zotero.Zotero",
    "Zen Browser": "Zen-Team.Zen-Browser",
    "Tor Browser (Gizlilik delilerine)": "TorProject.TorBrowser",
    "Acronis True Image": "Acronis.AcronisTrueImage",
    "Driver Booster": "IObit.DriverBooster",
    "iTunes": "Apple.iTunes",
    "Lightshot": "Skillbrains.Lightshot",
    "Paint.NET": "dotPDNLLC.paint.net",
    "ShareX": "ShareX.ShareX",
    "Sumatra PDF": "SumatraPDF.SumatraPDF",
    "WinDirStat": "WinDirStat.WinDirStat",
    "XnView": "XnSoft.XnViewMP",
    "HandBrake": "HandBrake.HandBrake",
    "MPC-HC": "clsid2.mpc-hc",
}

secili_uygulamalar = {}

def kur():
    secilenler = [ad for ad, var in secili_uygulamalar.items() if var.get()]
    if not secilenler:
        messagebox.showwarning("Uyarı", "Lütfen en az bir uygulama seçiniz!")
        return

    ilerleme_penceresi = tk.Toplevel(pencere)
    ilerleme_penceresi.title("Kurulum Devam Ediyor")
    tk.Label(ilerleme_penceresi, text="Kurulum başlatıldı...", font=("Arial", 12)).pack(pady=10)
    progress = ttk.Progressbar(ilerleme_penceresi, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=10)
    progress["maximum"] = len(secilenler)

    pencere.update()

    for i, ad in enumerate(secilenler):
        app_id = uygulamalar[ad]
        try:
            subprocess.run(["powershell", "winget", "install", "--id", app_id, "-e", "--accept-source-agreements", "--accept-package-agreements"], check=True)
        except subprocess.CalledProcessError:
            messagebox.showerror("Hata", f"{ad} kurulurken hata oluştu.")
        progress["value"] = i + 1
        pencere.update()

    messagebox.showinfo("Tamamlandı", "Tüm seçilen uygulamalar kuruldu!")
    ilerleme_penceresi.destroy()

pencere = tk.Tk()
pencere.title("AppLoomX")
pencere.geometry("500x700")
pencere.configure(bg="#1e1e1e")

tk.Label(pencere, text="Kurmak istediğiniz uygulamaları seçin:", bg="#1e1e1e", fg="white", font=("Arial", 12)).pack(pady=10)

search_var = tk.StringVar()

def arama_filtresi(event=None):
    arama = search_var.get().lower()
    canvas.yview_moveto(0)  
    for cb in checkbuttons:
        text = cb.cget("text").lower()
        if arama in text:
            cb.pack(anchor="w", padx=10)
        else:
            cb.pack_forget()
    if not arama:  
        for cb in checkbuttons:
            cb.pack(anchor="w", padx=10)

search_box = tk.Entry(pencere, textvariable=search_var, font=("Arial", 12), width=40)
search_box.pack(pady=10)
search_box.bind("<KeyRelease>", arama_filtresi)

canvas = tk.Canvas(pencere, bg="#1e1e1e", bd=0, highlightthickness=0)
canvas.pack(pady=10, expand=True, fill="both")

scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

scrollable_frame = tk.Frame(canvas, bg="#1e1e1e")
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", on_mouse_wheel)

checkbuttons = []
for ad in sorted(uygulamalar.keys()): 
    var = tk.BooleanVar()
    secili_uygulamalar[ad] = var
    cb = tk.Checkbutton(scrollable_frame, text=ad, variable=var, bg="#1e1e1e", fg="white", font=("Arial", 12), selectcolor="blue")
    checkbuttons.append(cb)

arama_filtresi()

kur_button = tk.Button(pencere, text="Kurulum Başlat", command=kur, font=("Arial", 14), bg="#4CAF50", fg="white", relief="flat")
kur_button.pack(pady=20)

pencere.mainloop()
