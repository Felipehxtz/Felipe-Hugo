/*
 * GccApplication3.c
 *
 * Created: 16/04/2020 15:08:50
 * Author : Felipextz
 */ 

#include <avr/io.h>
#define reset (1<<0)
#define start (1<<1)
#define clock (1<<2)
#define data (1<<3)
#define latch (1<<4)

void StandByte (unsigned char b);				   // Função que vai o conjunto de bits em data. b será a variável que armazenará esse conjunto.

int main(void)
{
    DDRD |= reset | start | clock | data | latch;
	PORTD |= reset;
	PORTD &= ~start;
	StandByte(0b10100111);
	return 0;
	
	
}

void StandByte (unsigned char b)
{
	PORTD &= ~latch;										// Desligando latch para primeiramente mandar o conjunto de bits
	unsigned char i = (1<<7);								// Variável auxiliar que vai fazer operação bit a bit com b 
															// Colocando bit mais significativo em 1
	while(i)												// Enquando i for verdadeiro:
	{
		PORTD &= ~clock;									// Clock em zero para não registrar nad
		PORTD = (b & i)?(PORTD | data):(PORTD & ~data);		// Se b e i forem verdadeiros, data vai a 1, se não, data vai a zero 
		PORTD |= clock;										// Liga o clock para registrar a operação
		i >>= 1;										    // Desloca um bit para a direita no i. No final i= 0b00000000 => Falso, logo, sai do loop
			
	}
	PORTD |= latch;
	
}
	
	
	
	
