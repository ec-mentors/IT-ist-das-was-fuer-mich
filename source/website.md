# Website

Auch wenn die Entwicklung von Webseiten über den Kurs hinaus geht,
wollen wir uns doch anschauen, wie man einfach Webseiten erstellt
und verstehen, welche Überlegungen und Technologien dabei zur
Anwendung kommen.

Wir befassen uns unter anderem mit diesen Fragen:
- Was ist eine Website?
- Wie erstellt man eine Website?
- Wie ist die Website für den Kurs aufgebaut?

Werkzeuge:
- Browser wie [Firefox](https://www.mozilla.org/en-US/firefox/new/) oder [Chrome](https://www.google.com/chrome/index.html)
- Text Editor oder eine Entwicklungsumgebung wie [Visual Studio Code](https://code.visualstudio.com/) (VS Code)

(web_tutorials_target)=
Tutorials:
- [Mozilla's "Learn web development"](https://developer.mozilla.org/en-US/docs/Learn)
- [Django Girls "Start your journey with programming"](https://djangogirls.org/en/resources/)
- [W3 Schools: HTML](https://www.w3schools.com/html/default.asp)
- [W3 Schools: CSS](https://www.w3schools.com/Css/)
- [Markdown](https://commonmark.org/)

(markdown_target)=
## Markdown als Vorstufe zu HTML

```{exercise} Markdown kennen lernen (15 Minuten)
:label: exercise-markdown

Was ist Markdown?

Wirf zuerst einen Blick auf die [Wikipedia Seite](https://de.wikipedia.org/wiki/Markdown).

Hat dir das geholfen?

Oft ist es gut, Dinge einfach auszuprobieren.

Schau' dir folgende Seiten an:
- https://markdown-editor.github.io/
  Schreibe auf der linken Seite und formatiere den
  Text mit Hilfe der Buttons. Was passiert?
- https://www.markdownguide.org/basic-syntax/
  Was bedeuten sie Spalten?

Diese Aufgabe bearbeitet jede für sich.

PS: Siehe Kommentar in Nachricht auf GitHub.
```

Um in VS Code ein Markdown Dokument zu erstellen und zu bearbeiten mache folgendes:
* Erstelle eine neue Datei (oder öffne eine existierende)
* Speichere die Datei als Markdown Datei mit der Dateiendung `.md` ab
* Editiere die Datei wie eine gewöhnlich Textdatei, verwende dabei [Markdown-Syntax](https://commonmark.org/help/) wie beispielsweise `#` für Überschriften oder `*` für Aufzählungen
* Betrachte die Vorschau für das Dokument in dem du `Strg+Shift+P` drückst und dann
  im Dialog `Markdown: Open Preview to the Side` auswählst

Den Inhalt einer Markdown Datei können wir eins zu eins als Inhalt für unsere Homepage
verwenden! 🤸

Es ist auch möglich, eine Markdown Datei mit Hilfe eines Programms direkt als HTML zu
exportieren. Dazu `Strg+Shift+P` und `Markdown All in One: Print current document to HTML`,
wobei wir die Erweiterung (das Programm) `Markdown All in One` verwenden.

(website_update_target)=
## Kursseite aktualisieren

Die Inhalte der Kursseite werden mit Markdown erstellt.
Die einzelnen Bestandteile und die Übersetzung in Markdown verwaltet ein eigenes Programm.
Es heißt [Sphinx](https://www.sphinx-doc.org/en/master/) und ist in der Programmiersprache
Python geschrieben.
Die Daten der Website liegen auf einem Server und jedes Mal, wenn wir den Inhalt ändern, wird
die Seite neu zusammen gebaut und aktualisiert.

Da wir Markdown verwenden, ist es ein Leichtes, Inhalte der Website zu ändern - man muss gar nicht
wissen, wie die Website im Detail funktioniert.


```{exercise} User Account für GitHub.com
:label: exercise-github-user-account

Nicht jede Person kann die Inhalte der Website ändern.
Dazu braucht es bestimmte Berechtigungen.

Gehe auf https://github.com/ und lege dort einen User Account an.

Du bekommst dann Zugriff auf unsere Kursseite.

Wenn das geklappt hat, hast du ein Mail von GitLab bekommen.
```

Die Kursseite kann man sich als Ordner mit vielen Dateien vorstellen.
Für jede Seite auf unserer Website gibt es auch eine Datei in diesem Ordner.

Wenn du **https://github.com/ec-mentors/it-ist-das-was-fuer-mich** öffnest,
kannst du einen Blick hinter die Kulissen werfen.


```{exercise} Update der persönlichen Kursseite
:label: exercise-update-personal-page

Sobald du Zugriff auf die Website hast, kannst du Änderungen
an den Dateien vornehmen.

Jede von euch hat eine Datei in diesem Ordner: https://github.com/ec-mentors/IT-ist-das-was-fuer-mich/tree/main/source/participants, das ist eure persönliche Seite im
Rahmen unseres Kurses. Genau dort, wollen wir ein paar Updates machen.

Nutze deinen Eintrag auf der Kursseite um dich kurz vorzustellen:
* Wie heißt du?
* Was machst du gerne?
* Wofür interessierst du dich?

*Damit wir nicht durcheinander kommen, mache bitte keine Änderungen in anderen
Dateien, nur in eurer eigenen.*
```

Es gibt sehr viele Möglichkeiten Webseiten und erstellen und zu verwalten.
Es gibt Baukastensysteme, mit denen man ganz ohne Programmierkenntnisse Webseiten
bauen kann.
Unsere Kursseite ist nur eine Möglichkeit und wir wollen euch die Gelegenheit
geben, hier einen Blick hinein zu werfen.


```{exercise} Persönliche Kursseite als Mini-Lebenslauf
:label: exercise-update-personal-page-properly

Wir werden die Kursseite nutzen, um einen stichwortartigen Lebenslauf
von euch anzulegen.

Gehe auf https://github.com/ec-mentors/IT-ist-das-was-fuer-mich/tree/main/source/participants
und schau dir die Vorlage an.
Passe dann deinen persönlichen Eintrag an,
in dem du dem Vorschlag entsprechend Änderungen an deiner Seite vornimmst.

Du kannst die Inhalte auch gerne anders strukturieren und gestalten.
Wichtig ist nur, dass genannten Informationen in übersichtlicher Art und Weise
zu finden sind.

Wenn du Hilft brauchst, wende dich an eine Kollegin.

*Damit wir nicht durcheinander kommen, mache bitte keine Änderungen in anderen
Dateien, nur in eurer eigenen.*
```


## Entwicklungswerkzeuge

Sobald man beginnt lokal (auf dem eigenen Computer) Webseiten zu entwickeln,
d.h. zumindest HTML-Dateien zu editieren, ist es sehr hilfreich,
dazu geeignete Texteditoren zu verwenden.

Es gibt eine Vielzahl von Systemen um die Entwicklung zu erleichtern,
ein weit verbreitetes Werkzeug ist [Visual Studio Code (VSCode)](https://code.visualstudio.com/).

VSCode gibt es auch [online](https://vscode.dev/).


## Minimales Beispiel für HTML und CSS

Es ist oft gut, möglichst klein zu beginnen.

Zwei sehr minimal gehaltene Beispiele für eine HTML und eine CSS Datei
findest du hier.

**mini_index.html**

```{literalinclude} ./_static/mini_index.html
:language: html
```

**mini_style.css**

```{literalinclude} ./_static/mini_style.css
:language: css
```

```{exercise} Minimale Webseite erstellen
:label: exercise-create-minimal-website

Speichere die oben gezeigten Texte jeweils als eigene Datei
in einem gemeinsamen Ordner und öffne die HTML-Datei in einem Browser.

Was siehst du?

Fragen:
* Wie hängen die Dateien zusammen?
* Wieso ist es wichtig, dass sie im gleichen Ordner liegen?
* Welche Fragen hast du jetzt?
```
