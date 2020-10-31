/*
 * kalman.c - Firmware de PIC18 para executar um filtro de Kalman.
 * 
 * Entrada: dois vetores do tipo 'float const' presentes no arquivo in.h
 * Saída: índice (para facilitar testes), valor com ruído e valor filtrado.
 *        Os dois últimos são arredondados com duas casas decimais.
 *
 * Modo de uso: os valores dos vetores existentes em in.h (com ruído) são
 *              utilizados para calcular a iteração futura, de forma que a saída
 *              seja o mais próximo possível do valor real.
 *              O valor real é gerado pelo arquivo valores.py.
 *              Os dados são obtidos através do arquivo grafico.py, que lê os
 *              dados da serial e armazena valores de entrada e saída em 
 *              arquivos diferentes.
 *              Os gráficos são gerados pelo arquivo gera_grafico.py, com
 *              parâmetros exemplificados no README.
 *              Todos os arquivos com exceção do in.h (que é gerado pelo arquivo
 *              valores.py) estão presentes no link abaixo.
 *              https://github.com/alynnefs/kalman_filter_pic
 *              OBS: in.h e kalman.c devem estar no mesmo nível de diretório.
 *                   MPLABX e XC8 foram utilizados para desenvolvimento e compilação.
 * 
 * Algoritmo desenvolvido para a cadeira de Sistemas Embarcados do curso de
 * Engenharia de Computação do IFCE
 * 
 * Copyright (C) 2017 Alynne Ferreira <alynneferreiras@gmail.com>
 * Copyright (C) 2017 Mateus Rodrigues <mateus.fr26@gmail.com>
 *
 * This program is free software: you can redistribute it and/or
 * modify it under the terms of the GNU Affero General Public
 * License version 3 as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License version 3 for more details.
 *
 * You should have received a copy of the GNU Affero General Public
 * License version 3 along with this program. If not, see
 * <http://www.gnu.org/licenses/>.
 */


// As configurações abaixo foram geradas pela IDE ao setar alguns registradores.
// Os registradores que não foram setados possuem valores default
//// CLOCK DE 8MHz, CLOCK INTERNO
#pragma config PLLDIV = 1       // PLL Prescaler Selection bits (No prescale (4 MHz oscillator input drives PLL directly))
#pragma config CPUDIV = OSC1_PLL2// System Clock Postscaler Selection bits ([Primary Oscillator Src: /1][96 MHz PLL Src: /2])
#pragma config USBDIV = 1       // USB Clock Selection bit (used in Full-Speed USB mode only; UCFG:FSEN = 1) (USB clock source comes directly from the primary oscillator block with no postscale)
#pragma config FOSC = INTOSC_XT // Oscillator Selection bits (Internal oscillator, XT used by USB (INTXT))
#pragma config FCMEN = OFF      // Fail-Safe Clock Monitor Enable bit (Fail-Safe Clock Monitor disabled)
#pragma config IESO = OFF       // Internal/External Oscillator Switchover bit (Oscillator Switchover mode disabled)

//------------------------------------------------------------------------------
// CONFIG2L
#pragma config PWRT = OFF       // Power-up Timer Enable bit (PWRT disabled)
#pragma config BOR = OFF        // Brown-out Reset Enable bits (Brown-out Reset disabled in hardware and software)
#pragma config BORV = 3         // Brown-out Reset Voltage bits (Minimum setting)
#pragma config VREGEN = OFF     // USB Voltage Regulator Enable bit (USB voltage regulator disabled)

// CONFIG2H
#pragma config WDT = OFF        // Watchdog Timer Enable bit (WDT disabled (control is placed on the SWDTEN bit))
#pragma config WDTPS = 32768    // Watchdog Timer Postscale Select bits (1:32768)

// CONFIG3H
#pragma config CCP2MX = OFF     // CCP2 MUX bit (CCP2 input/output is multiplexed with RB3)
#pragma config PBADEN = OFF     // PORTB A/D Enable bit (PORTB<4:0> pins are configured as digital I/O on Reset)
#pragma config LPT1OSC = OFF    // Low-Power Timer 1 Oscillator Enable bit (Timer1 configured for higher power operation)
#pragma config MCLRE = ON       // MCLR Pin Enable bit (MCLR pin enabled; RE3 input pin disabled)

// CONFIG4L
#pragma config STVREN = OFF     // Stack Full/Underflow Reset Enable bit (Stack full/underflow will not cause Reset)
#pragma config LVP = OFF        // Single-Supply ICSP Enable bit (Single-Supply ICSP disabled)
#pragma config XINST = OFF      // Extended Instruction Set Enable bit (Instruction set extension and Indexed Addressing mode disabled (Legacy mode))

// CONFIG5L
#pragma config CP0 = OFF        // Code Protection bit (Block 0 (000800-001FFFh) is not code-protected)
#pragma config CP1 = OFF        // Code Protection bit (Block 1 (002000-003FFFh) is not code-protected)
#pragma config CP2 = OFF        // Code Protection bit (Block 2 (004000-005FFFh) is not code-protected)
#pragma config CP3 = OFF        // Code Protection bit (Block 3 (006000-007FFFh) is not code-protected)

// CONFIG5H
#pragma config CPB = OFF        // Boot Block Code Protection bit (Boot block (000000-0007FFh) is not code-protected)
#pragma config CPD = OFF        // Data EEPROM Code Protection bit (Data EEPROM is not code-protected)

// CONFIG6L
#pragma config WRT0 = OFF       // Write Protection bit (Block 0 (000800-001FFFh) is not write-protected)
#pragma config WRT1 = OFF       // Write Protection bit (Block 1 (002000-003FFFh) is not write-protected)
#pragma config WRT2 = OFF       // Write Protection bit (Block 2 (004000-005FFFh) is not write-protected)
#pragma config WRT3 = OFF       // Write Protection bit (Block 3 (006000-007FFFh) is not write-protected)

// CONFIG6H
#pragma config WRTC = OFF       // Configuration Register Write Protection bit (Configuration registers (300000-3000FFh) are not write-protected)
#pragma config WRTB = OFF       // Boot Block Write Protection bit (Boot block (000000-0007FFh) is not write-protected)
#pragma config WRTD = OFF       // Data EEPROM Write Protection bit (Data EEPROM is not write-protected)

// CONFIG7L
#pragma config EBTR0 = OFF      // Table Read Protection bit (Block 0 (000800-001FFFh) is not protected from table reads executed in other blocks)
#pragma config EBTR1 = OFF      // Table Read Protection bit (Block 1 (002000-003FFFh) is not protected from table reads executed in other blocks)
#pragma config EBTR2 = OFF      // Table Read Protection bit (Block 2 (004000-005FFFh) is not protected from table reads executed in other blocks)
#pragma config EBTR3 = OFF      // Table Read Protection bit (Block 3 (006000-007FFFh) is not protected from table reads executed in other blocks)

// CONFIG7H
#pragma config EBTRB = OFF      // Boot Block Table Read Protection bit (Boot block (000000-0007FFh) is not protected from table reads executed in other blocks)//
//// #pragma config statements should precede project file includes.
//// Use project enums instead of #define for ON and OFF.

// fim das configurações geradas pela IDE

#define _XTAL_FREQ 8000000 // clock interno
#include <xc.h>
#include <stdio.h>
#include <stdlib.h>   
#include <string.h>
#include "in.h" // entrada de dados


// Valores usados pra cálculo. Foram obtidos com testes.
double Q = 0.0; // erro estimado no processo
double R = 0.2; // erro estimado nas medidas
double P = 1.0, X = 0.0, K;
// P: estimativa de covariância inicial, X: estimativa inicial do estado, K: variavel auxiliar
double result;

// variáveis auxiliares
unsigned int i = 0; // índice do vetor
unsigned int aux = 0; // variável que ajuda a definir qual laço será executado

/* Atualização de medidas com base no filtro de kalman
 * Origem da função:
 * http://www.dyadica.co.uk/very-simple-kalman-in-c/
 * acesso em janeiro de 2017
 * Obs: modificada de C# para C
 */
void measurementUpdate() {
    K = (P + Q) / (P + Q + R);
    P = R * (P + Q) / (R + P + Q);
}


/* Soma com k anterior
 * Origem da função:
 * http://www.dyadica.co.uk/very-simple-kalman-in-c/
 * acesso em janeiro de 2017
 * Obs: modificada de C# para C
 */
double update(double measurement) {
    result = X + (measurement - X) * K;
    measurementUpdate(); //atualizacao de medidas
    X = result;
    return result;
}

/* Inicialização da UART.
 * Origem da função:
 * https://electrosome.com/uart-pic-microcontroller-mplab-xc8/
 * acesso em fevereiro de 2017
 * Obs: modificado para tornar mais específico
 */
void UART_Init(const long int baudrate) {
    unsigned int y; // 
    y = (_XTAL_FREQ / baudrate / 4) - 1; //SPBRG for Low Baud Rate
    // obs sobre y: equação modificada de acordo com o datasheet, de forma que possa funcionar com baud rate de 115200
    SPBRG = y; //Writing SPBRG Register
    SYNC = 0; //Setting Asynchronous Mode, ie UART
    SPEN = 1; //Enables Serial Port
    TRISC7 = 1; //As Prescribed in Datasheet
    TRISC6 = 1; //As Prescribed in Datasheet
    CREN = 1; //Enables Continuous Reception
    TXEN = 1; //Enables Transmission
    
    // configuração pra aumentar o baud rate 
    BRGH = 1;
    BRG16 = 1;
}

/* Envio pela serial
 * Origem da função:
 * https://electrosome.com/uart-pic-microcontroller-mplab-xc8/
 * acesso em fevereiro de 2017
 */

void putch(unsigned char data) {
    while (!PIR1bits.TXIF); // wait until the transmitter is ready
    TXREG = data; // send one character
}

void main(void) {
    UART_Init(115200); // inicialização da UART
    //// CLOCK DE 8MHz, CLOCK INTERNO
    OSCCONbits.IRCF = 7; // escolhe oscilador interno a 8MHz
    OSCCONbits.SCS = 2; // 'ativa' oscilador interno

    while(1){
       // todas as variáveis abaixo são globais, com exceção de NUM_ANS, DATA1 e DATA2
        
        //voltage
        if(i<NUM_AMS && aux == 0){ // aux == 0 executa o DATA[]
            result = update(DATA1[i]); // executa o filtro de acordo com o valor atual
            printf("%d\t%.2f\t%.2f\n\r", i, DATA1[i], result); // envia índice, valor atual e valor depois do filtro
            i++; // muda o próximo índice
            
            if(i == NUM_AMS){ // reinicia as variáveis se o índice for 800 
                P = 1.0;
                X = 0.0;
                K = 0.0;
                i = 0;
                aux = 1; // faz com que a próxima iteração ocorra apenas na condição seguinte
                result = 0;
            }
        }
        
        //cannon
        if(i<NUM_AMS && aux == 1){ // aux == 1 executa o DATA2[]
            result = update(DATA2[i]); // executa o filtro de acordo com o valor atual
            printf("%d\t%.2f\t%.2f\n\r", i, DATA2[i], result); // envia índice, valor atual e valor depois do filtro
            i++; // muda o próximo índice
            
            if(i == NUM_AMS){ // se o índice for 800 reinicia as variáveis
                aux = 2; // aux == 2 para os cálulos relacionados ao filtro de Kalman. O programa permanece em while(1),
                         // verificando as condições, mas sem executá-las, pois nenhuma será satisfeita
            }
        }
    }
}