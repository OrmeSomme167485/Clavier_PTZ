const int SW1 = 36;
const int SW2 = 39;
const int SW3 = 34;
const int SW4 = 35;
const int SW5 = 32;
const int SW6 = 33;
const int SW7 = 25;
const int SW8 = 26;
const int SW9 = 27;
const int SWTR = 14;
const int SWFD = 0;
const int SWFG = 2;
const int SWFH = 15;
const int SWFB = 4;
const int SWZP = 13;
const int SWZM = 12;

int dernierEtat = LOW;

void setup() {
  Serial.begin(115200);
  pinMode(SW1, INPUT);
  pinMode(SW2, INPUT);
  pinMode(SW3, INPUT);
  pinMode(SW4, INPUT);
  pinMode(SW5, INPUT);
  pinMode(SW6, INPUT);
  pinMode(SW7, INPUT);
  pinMode(SW8, INPUT);
  pinMode(SW9, INPUT);
  pinMode(SWTR, INPUT);
  pinMode(SWFB, INPUT);
  pinMode(SWFD, INPUT);
  pinMode(SWFG, INPUT);
  pinMode(SWFH, INPUT);
  pinMode(SWZM, INPUT);
  pinMode(SWZP, INPUT);

}

void loop() {
  int etat = digitalRead(pinSignal);
  if (etat == HIGH && dernierEtat == LOW) {
    Serial.println("TRIGGER_A");
    delay(100);
  }
  dernierEtat = etat;

}