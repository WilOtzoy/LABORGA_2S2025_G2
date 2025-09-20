// Practica 3, Grupo #3

// PINES
const int PSW_CORRECTO    = 2,
          CLK_ASCENDENTE  = 3,
          CLK_DESCENDENTE = 4,
          MOTOR_VELOCIDAD = 9,
          MOTOR_IN1       = 6,
          MOTOR_IN2       = 7;

// PROTOTIPO DE FUNCIONES
void girarMotorIzqierda();
void girarMotorDerecha();
void apagarMotor();
void trenPulsos(int pin, int repeticiones);
void reiniciarContadores();


void setup() {
  // put your setup code here, to run once:
  pinMode(PSW_CORRECTO, INPUT);
  pinMode(CLK_ASCENDENTE, OUTPUT);
  pinMode(CLK_DESCENDENTE, OUTPUT);
  pinMode(MOTOR_VELOCIDAD, OUTPUT);
  pinMode(MOTOR_IN1, OUTPUT);
  pinMode(MOTOR_IN2, OUTPUT);

  

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(PSW_CORRECTO) == HIGH) {
    analogWrite(MOTOR_VELOCIDAD, 255); // Lanza aprox. 3.3V
    //digitalWrite(MOTOR_VELOCIDAD, HIGH); // Lanza aprox. 3.3V
    girarMotorIzqierda();
    trenPulsos(CLK_ASCENDENTE, 15);
    apagarMotor();
    delay(500);
    girarMotorDerecha();
    trenPulsos(CLK_DESCENDENTE, 10);
    apagarMotor();
    reiniciarContadores();
  }
  delay(17);
}


void girarMotorIzqierda() {
  digitalWrite(MOTOR_IN1, HIGH);
  digitalWrite(MOTOR_IN2, LOW);
}

void girarMotorDerecha() {
  digitalWrite(MOTOR_IN1, LOW);
  digitalWrite(MOTOR_IN2, HIGH);
}

void apagarMotor() {
  digitalWrite(MOTOR_IN1, LOW);
  digitalWrite(MOTOR_IN2, LOW);
}

void trenPulsos(int pin, int repeticiones) {
  for (int i = 0; i < repeticiones; i++) {
    digitalWrite(pin, HIGH);
    delay(1);
    digitalWrite(pin, LOW);
    delay(999);
  }
}

void reiniciarContadores() {
  digitalWrite(CLK_ASCENDENTE, HIGH);
  delay(1);
  digitalWrite(CLK_ASCENDENTE, LOW);
  
  digitalWrite(CLK_DESCENDENTE, HIGH);
  delay(1);
  digitalWrite(CLK_DESCENDENTE, LOW);
}