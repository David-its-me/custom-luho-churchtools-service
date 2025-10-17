from custom_luho_presentation_builder.announcement.announcement_presentation import (
    create_announcement_presentation,
)
from urllib import request
import time

def internet_on():
    try:
        request.urlopen('https://luho.church.tools/', timeout=1)
        return True
    except request.URLError as err: 
        return False

while(not internet_on()):
    print("Konnte nicht mit dem Internet verbinden. Versuche es erneut in einer Minute.")
    print()
    time.sleep(60)
    
create_announcement_presentation()

print("#####################################################")
print("### Fertig - du kannst jetzt Propresenter öffnen. ###")
print("#####################################################")
print()
print("Bitte lass dieses Fenster weiterhin geöffnet! \n"\
      "Die Announcement Folien werden in 10 Minuten ein zweites Mal automatisch generiert. \n"\
      "\n"\
      "Warum ist das notwendig? \n"\
      "Falls du deine selbst erstellte ein Playlist von Zuause importierst, könnte der Fall auftreteten \n"\
      "dass du damit die automatisch generierte Annoucment Präsentation überschreibst. Damit wir sicher stellen\n" \
      "könnnen, dass wir die aktuellen Announcements haben, läuft dieses Skript noch einmal in 10 Minuten. \n")

time.sleep(600)
create_announcement_presentation()

print("##############")
print("### Fertig ###")
print("##############")
