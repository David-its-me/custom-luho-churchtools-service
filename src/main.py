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
      "Die Announcement Folien werden in 10 Minuten ein zweites Mal automatisch erzeugt. \n"\
      "\n"\
      "Warum ist das notwendig? \n"\
      "Falls du deine vorbereitete Playlist von Zuhause importierst, wird die automatisch\n"\
      "erzeugte Annoucment-Präsentation überschrieben. Damit wir trotzdem sicher stellen könnnen,\n"\
      "dass wir die aktuellsten Announcements haben, läuft dieses Skript gleich einfach nochmal ;=).\n"\
      "\n")

time.sleep(600)

while(not internet_on()):
    print("Konnte nicht mit dem Internet verbinden. Versuche es erneut in einer Minute.")
    print()
    time.sleep(60)
    
create_announcement_presentation()

print("##############")
print("### Fertig ###")
print("##############")
