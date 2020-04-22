/*
 * GccApplication2.c
 *
 * Created: 16/04/2020 01:22:55
 * Author : Felipextz
 */ 

#include <avr/io.h>
#define LED (1<<7)	//Representa o led
#define BOT (1<<6)	//Representa o Bot�o

int main(void)
{
    DDRD |= LED;	//Define a porta 7 do conjunto D de portas como uma sa�da
	DDRD &= ~BOT;	//Define a porta 6 do conjunto D de portas como uma entrada
	
	//PIND = 0b00000000 => esse registrador armazena os valores das entradas(se a entrada estiver em 0 ser� 0, se for 1 ser� 1) 
	
    while (1) 
    {
		if(PIND & BOT) // Se PIND estiver recebendo 1 no bit 6 e o bot�o estiver apertado ent�o:
		{
			PORTD |= LED; //Liga LED
		}
		else
		{
			PORTD &= ~LED; //Desliga LED
		}
			//Maneira 2
		//PORTD = (PIND & BOT)?(PORTD | LED):(PORTD & ~LED)
	}
}

