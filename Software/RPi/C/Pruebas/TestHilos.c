//Compilar:
//gcc /home/pi/Pruebas/TestHilos.c -o /home/pi/Pruebas/testhilos -lbcm2835 -lwiringPi -lm
//gcc /home/pi/Programas/Pruebas/TestHilos.c -o /home/pi/Programas/Pruebas/testhilos -lbcm2835 -lwiringPi -lm

#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
//#include <bcm2835.h>
#include <time.h>
#include <string.h>
#include <unistd.h>


//Declaracion de constantes
#define P1 0																	//Pin 11 GPIO
#define MCLR 28																	//Pin 38 GPIO
#define TEST 29 																//Pin 40 GPIO																						
#define TIEMPO_SPI 10
#define FreqSPI 2000000

unsigned int contador1;


int main(void) {
	
	contador1 = 0;

	system("sudo ./hilo1&");
	
	while(1){	
		
		    printf("Contador 1: %d\n", contador1); 
			//system("sudo ./hilo1 &");
			
			delay(500);
			
			
			
			contador1++;
			printf("\n");
			//delay (1000);
	
	}

}

