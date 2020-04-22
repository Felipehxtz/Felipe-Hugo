/*
 * GccApplication1.c
 *
 * Created: 15/04/2020 13:48:37
 * Author : Felipextz
 */ 

// FREQUÊNCIA
#define F_CPU 16000000 // FREQUÊNCIA DO CRISTAL 

// BIBLIOTECAS AUXILIARES
#include <avr/io.h>
#include <util/delay.h>

// REGISTRADOR = REGISTRADOR OR FLAG(1)[LIGANDO UM DETERMINADO BIT]
//REGISTRADOR = REGISTRADOR AND (NOT FLAG(1))[DESLIGANDO UM DETERMINADO BIT]
int main(void) 
{
    DDRB |= (1<<4); 
			
	/* Replace with your application code */
    while (1) 
    {
		PORTB |= (1<<4);
		_delay_ms(100);
		PORTB &= ~(1<<4);
		_delay_ms(100);
	}
}

