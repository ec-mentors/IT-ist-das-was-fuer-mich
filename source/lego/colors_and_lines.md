# Farben und Linien

```{exercise} Ev3 Farbsensor kalibrieren ⭐
:label: exercise-ev3-calibrate-sensor

Wir werden hier den Farbsensor verwenden um zwischen hell und dunkel zu unterscheiden.

Dazu müssen wir den Farbsensor zuerst kalibrieren, d.h. wir müssen ihm zeigen, was hell und dunkel ist. Dazu stellen wir ihn so hin, dass er über etwas hellem steht, messen die Menge des reflektierten Lichts, und speichern diesen Wert als hell. Dann machen wir dasselbe mit dunkel.

Hier wird hell ein weißes oder gelbes Klebeband sein, dunkel ist der Boden.

Im Bild ist ein Beispielcode, wie du den Sensor kalibrieren kannst.

![code sample](./sensor-kalibrieren.png)
```

```{exercise} Ev3 Fahren bis zur Linie ⭐⭐
:label: exercise-ev3-go-to-line

Wenn der Farbsensor zwischen hell und dunkel unterscheiden kann, können wir das verwenden, um ihn an einer hellen Linie stoppen zu lassen.

Wie geht das? Der Roboter fährt vorwärts. Er wartet, bis das die Menge an reflektiertem Licht einen Grenzwert überschreitet. Dann stoppt er.

Wo liegt dieser Grenzwert? Das musst du ausprobieren.
```

```{exercise} Ev3 Pendeln ⭐⭐⭐
:label: exercise-ev3-back-and-forth

Der Roboter fährt vorwärts bis zur hellen Linie. Dann fährt er rückwärts bis zur anderen hellen Linie. Das wiederholt er 5 mal.

```

```{exercise} Ev3 Der Linie folgen ⭐⭐⭐
:label: exercise-ev3-follow-line

Der Roboter soll der hellen Linie folgen. Wenn die Linie gerade ist, ist das nicht schwer - er muss nur geradeaus fahren. Wenn die Linie aber Kurven enthält, ist das ein bisschen schwieriger. 

Es gibt verschiedene Algorithmen, um das Problem zu lösen. Der einfachste geht so:

Der Roboter misst das reflektierte Licht. Wenn der Wert eine bestimmt Schwelle unterschreitet, bewegt er sich ein bisschen zur Linie hin, sonst bewegt er sich ein bisschen in die andere Richtung. Er fährt also mal ein bisschen nach links, dann ein bisschen nach rechts. Das schaut nicht sehr elegant aus, aber es funktioniert.

**Bonusfragen**

Was passiert, wenn die Linie einen rechten Winkel enthält?

Was passiert, wenn die Linie einen spitzen Winkel enthält?

Macht es einen Unterschied, in welche Richtung der Roboter der Linie folgt, also an welchem Ende er beginnt?

Findest du einen besseren Algorithmus? Also einen, bei dem der Roboter nicht so stark ruckelt? 

```
