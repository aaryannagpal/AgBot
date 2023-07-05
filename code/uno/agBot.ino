// Pins for the Left Motor, according to the ciruit diagram made
#define lft_R_IS 4
#define lft_R_EN 2
#define lft_R_PWM 5
#define lft_L_IS 7
#define lft_L_EN 1
#define lft_L_PWM 3

// Pins for the Right Motor, according to the ciruit diagram made
#define rgt_R_IS 13
#define rgt_R_EN 12 
#define rgt_R_PWM 6
#define rgt_L_IS 8
#define rgt_L_EN 11
#define rgt_L_PWM 10

char fromPi;

void setup() {

  
 // LEFT MOTOR DRIVER
 pinMode(lft_R_IS, OUTPUT);
 pinMode(lft_R_EN, OUTPUT);
 pinMode(lft_R_PWM, OUTPUT);
 pinMode(lft_L_IS, OUTPUT);
 pinMode(lft_L_EN, OUTPUT);
 pinMode(lft_L_PWM, OUTPUT);
 digitalWrite(lft_R_IS, LOW);
 digitalWrite(lft_L_IS, LOW);
 digitalWrite(lft_R_EN, HIGH);
 digitalWrite(lft_L_EN, HIGH);

   // RIGHT MOTOR DRIVER
 pinMode(rgt_R_IS, OUTPUT);
 pinMode(rgt_R_EN, OUTPUT);
 pinMode(rgt_R_PWM, OUTPUT);
 pinMode(rgt_L_IS, OUTPUT);
 pinMode(rgt_L_EN, OUTPUT);
 pinMode(rgt_L_PWM, OUTPUT);
 digitalWrite(rgt_R_IS, LOW);
 digitalWrite(rgt_L_IS, LOW);
 digitalWrite(rgt_R_EN, HIGH);
 digitalWrite(rgt_L_EN, HIGH);

 Serial.begin(9600);
}

void right(int pwmcycle) {
   analogWrite(rgt_R_PWM, pwmcycle);
   analogWrite(rgt_L_PWM, 0); 
   analogWrite(lft_R_PWM, pwmcycle);
   analogWrite(lft_L_PWM, 0);                 
}



void left(int pwmcycle) {
   analogWrite(rgt_R_PWM, 0);
   analogWrite(rgt_L_PWM, pwmcycle); 
   analogWrite(lft_R_PWM, 0);
   analogWrite(lft_L_PWM, pwmcycle);

   
}
void forward(int pwmcycle) {
   analogWrite(rgt_R_PWM, pwmcycle);
   analogWrite(rgt_L_PWM, 0); 
   analogWrite(lft_R_PWM, 0);
   analogWrite(lft_L_PWM, pwmcycle);
}
void backward(int pwmcycle) {
   analogWrite(rgt_R_PWM, 0);
   analogWrite(rgt_L_PWM, pwmcycle); 
   analogWrite(lft_R_PWM, pwmcycle);
   analogWrite(lft_L_PWM, 0);
}
void stopmotors(){
   analogWrite(rgt_R_PWM, 0);
   analogWrite(rgt_L_PWM, 0); 
   analogWrite(lft_R_PWM, 0);
   analogWrite(lft_L_PWM, 0);  
}
void loop() {
  delay(15);
  if (Serial.available() > 0) {
    fromPi = Serial.read();
    
    if  (fromPi == 'F') {
      forward(255);
    }
    else if (fromPi== 'B') {
      backward(255);
    }
    else if (fromPi== 'R') {
      right(255);
    }
    else if (fromPi== 'L') {
      left(255);
    }
    else if (fromPi== 'S') {
      stopmotors();
    }
    else{
      stopmotors();
    }
  }

//  else{
//    stopmotors();
//  }
  Serial.flush();

}
