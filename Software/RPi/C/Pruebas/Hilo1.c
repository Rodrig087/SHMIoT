//Compilar:
//gcc /home/pi/Pruebas/Hilo1.c -o /home/pi/Pruebas/hilo1 -lbcm2835 -lwiringPi -lm
//gcc /home/pi/Programas/Pruebas/Hilo1.c -o /home/pi/Programas/Pruebas/hilo1 -lbcm2835 -lwiringPi -lm

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

unsigned int contador2;


int main(void) {
	
	contador2 = 0;

	while(1){	
		
		    printf("Contador 2: %d\n", contador2); 
			//system("sudo ./inspeccionarevento 1 1768190");
			system("python3 /home/pi/Programas/Pruebas/publicarevento.py 86400 100");
			
			delay(5000);
			
			if (contador2==5){
				exit(-1);
			}
			
			
			contador2++;
			printf("\n");
			//delay (1000);
	
	}

}

