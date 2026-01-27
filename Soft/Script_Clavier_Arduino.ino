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

  int  VSW1 = 0;
  int  VSW2 = 0;
  int  VSW3 = 0;
  int  VSW4 = 0;
  int  VSW5 = 0;
  int  VSW6 = 0;
  int  VSW7 = 0;
  int  VSW8 = 0;
  int  VSW9 = 0;
  int  VSWTR = 0;
  int  VSWFB = 0;
  int  VSWFD = 0;
  int  VSWFG = 0;
  int  VSWFH = 0;
  int  VSWZM = 0;
  int  VSWZP = 0;


void setup() {
  Serial.begin(9600);
  
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

    VSW1 = analogRead(SW1);
    VSW2 = analogRead(SW2);
    VSW3 = analogRead(SW3);
    VSW4 = analogRead(SW4);
    VSW5 = analogRead(SW5);
    VSW6 = analogRead(SW6);
    VSW7 = analogRead(SW7);
    VSW8 = analogRead(SW8);
    VSW9 = analogRead(SW9);
    VSWTR = analogRead(SWTR);
    VSWFB = analogRead(SWFB);
    VSWFD = analogRead(SWFD);
    VSWFG = analogRead(SWFG);
    VSWFH = analogRead(SWFH);
    VSWZM = analogRead(SWZM);
    VSWZP = analogRead(SWZP);


  if (VSW1 >= 3500 ) {
    Serial.println("TRIGGER_F13");
    delay(100);
  }
    if (VSW2 >= 3500 ) {
      Serial.println("TRIGGER_F14");
      delay(100);
    }
    if (VSW3 >= 3500 ) {
      Serial.println("TRIGGER_F15");
      delay(100);
    }
    if (VSW4 >= 3500 ) {
      Serial.println("TRIGGER_F16");
      delay(100);
    }
    if (VSW5 >= 3500 ) {
      Serial.println("TRIGGER_F17");
      delay(100);
    }
    if (VSW6 >= 3500 ) {
      Serial.println("TRIGGER_F18");
      delay(100);
    }
    if (VSW7 >= 3500 ) {
      Serial.println("TRIGGER_F19");
      delay(100);
    }
    if (VSW8 >= 3500 ) {
      Serial.println("TRIGGER_F20");
      delay(100);
    }
    if (VSW9 >= 3500 ) {
      Serial.println("TRIGGER_F21");
      delay(100);
    }
      if (VSWTR >= 3500 ) {
      Serial.println("TRIGGER_F22");
      delay(100);
    }
    if (VSWFD >= 3500 ) {
      Serial.println("TRIGGER_F23"); 
      delay(100);
    }
    if (VSWFG >= 3500 ) {
      Serial.println("TRIGGER_F24");
      delay(100);
    }
    if (VSWFH >= 3500 ) {
      Serial.println("TRIGGER_F25");
      delay(100);
    }
    if (VSWFB >= 3500 ) {
      Serial.println("TRIGGER_F26");
      delay(100);
    }
    if (VSWZP >= 3500 ) {
      Serial.println("TRIGGER_F27");
      delay(100);
    }
    if (VSWZM >= 3500 ) {
      Serial.println("TRIGGER_F28");
      delay(100);
    }


}
