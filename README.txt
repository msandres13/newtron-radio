Additional changes:
- port to python3 and uptodate modules
- use systemd --user for mpc (not complete yet)
- add rpm/deb build so newtron-radio can be installed easily


python3 ./setup.py clean
python3 ./setup.py bdist_rpm --requires mpd mpc

# check
rpm -qp dist/newtron-radio-1.0-1.noarch.rpm --requires

# install
sudo rpm -ihv dist/newtron-radio-1.0-1.noarch.rpm

# run
python3 /usr/lib/python3.8/site-packages/newtron-radio.py

Dies ist eine stark modifizierte Version des Ursprünglich von 5Volt-Junkie
auf https://github.com/5Volt-Junkie/RPi-Tron-Radio veröffentlichen Projektes.

Folgendes ist anders:
1. Unabhängig von der Bildschirmauflösung (automatisch)
2. Überlange Titel- und Sendertexte werden gescrollt
3. Hintergrundbilder sind möglich
4. Statt pngs für jede Farbe und Auflösung wird nur ein Satz
   kleiner svg-Dateien (für das Anzeigefenster und für 
   die Touchbuttons) benötigt
5. Jede Menge Geschwindigkeits- und Lastoptimierungen
   (leider ist das der Übersichtlichkeit etwas abträglich...)
6. Touchbuttons ändern sich bei Aktion 
   ("Pause" drücken - "Play" erscheint)
7. Uhr als Screensaver (falls sich die Hintergrundbeleuchtung
   nicht abschalten lässt)
8. ...usw...

Bitte beachten Sie die Hinweise in INSTALL.txt
