/*
Juego de dados en C por turnos contra la maquina.
El jugador y la maquina comienzan con 100 puntos.
En cada turno se lanza un dado de 6 caras:
- Si sale 2 a 5, se suman puntos al acumulado del turno( para restarselo al rival al final del turno).
- Si sale 1, se pierde el turno y el acumulado.
- Si sale 6, se aplica multiplicador o divisor con moneda 2 o 3 al acumulado
Despues de cada tirada se pregunta si se quiere seguir.
Gana quien logra que el rival llegue primero a 0 puntos.
*/
#include <stdio.h>
#include <stdlib.h> 
#include <time.h>
// Aca creo FUNCIÓN TIRAR_DADO
// Esta funcion simula tirar un dado de 6 caras
// La uso muchas veces durante el juego y también aca utilizo mi primera modularización
// Devuelve un numero entre 1 y 6, aplicando la lógica de un dado
int tirar_dado() {
    return rand() % 6 + 1;
}
/*
FUNCION QUE SIMULA UNA MONEDA QUE DA 2 O 3.
*/
int tirar_moneda_2_3() {
    if (rand() % 2 == 0) {
        return 2;
    }
    return 3;
}
/*
ESTA FUNCION DECIDE SI ES DIVISOR O MULTIPLICADOR:
Yo lo represento con un tiro hipotetico simple de 2 opciones:
- 0 = divisor
- 1 = multiplicador
*/
int tirar_modo() {
    return rand() % 2;
}

/*
FUNCION PARA LA REGLA CUANDO SALE 6:
- Se decide multiplicador o divisor
- Se tira moneda 2 o 3
- Se modifica el acumulado del turno
*/
int aplicar_regla_del_6(int acumulado) {
    int modo = tirar_modo();         /* 0 divisor, 1 multiplicador */
    int moneda = tirar_moneda_2_3(); /* 2 o 3 */

    if (modo == 1) {
        acumulado = acumulado * moneda;
        printf("Salio 6: MULTIPLICADOR x%d -> acumulado ahora: %d\n", moneda, acumulado);
    } else {
        /* Division entera en C ya redondea hacia abajo (entero) */
        acumulado = acumulado / moneda;
        printf("Salio 6: DIVISOR /%d -> acumulado ahora: %d\n", moneda, acumulado);
    }

    return acumulado;
}

/*
TURNO DEL JUGADOR:
- Va tirando mientras el usuario diga "s"
- Devuelve el acumulado final del turno (que luego se le resta al rival)
*/
int turno_jugador() {
    int acumulado = 0;
    char seguir = 's';

    printf("\n=== TURNO DEL JUGADOR ===\n");

    while (seguir == 's') {
        int dado = tirar_dado();
        printf("Dado: %d\n", dado);

        if (dado >= 2 && dado <= 5) {
            /* Se acumula para restarselo al rival al final del turno */
            acumulado += dado;
            printf("Acumulado del turno: %d\n", acumulado);

        } else if (dado == 1) {
            /* Si sale 1: se pierde el turno y todos los puntos acumulados */
            acumulado = 0;
            printf("Salio 1: pierdes el turno y el acumulado se pierde.\n");
            break;

        } else { /* dado == 6 */
            /* Si sale 6: regla especial con multiplicador/divisor y moneda 2 o 3 */
            acumulado = aplicar_regla_del_6(acumulado);
        }

        /* La consigna pide preguntar despues de cada tirada */
        printf("Quieres seguir tirando? (s/n): ");
        scanf(" %c", &seguir);
    }

    return acumulado;
}

/*
Turno de la maquina (LIBRE):
- Para que sea simple, la maquina tira hasta 3 veces, o corta si sale 1.
- Devuelve el acumulado final del turno (que luego se le resta al jugador)
*/
int turno_maquina() {
    int acumulado = 0;
    int tiradas = 0;

    printf("\n=== TURNO DE LA MAQUINA ===\n");

    while (tiradas < 3) {
        int dado = tirar_dado();
        printf("La maquina tiro: %d\n", dado);

        if (dado >= 2 && dado <= 5) {
            acumulado += dado;
            printf("Acumulado de la maquina: %d\n", acumulado);

        } else if (dado == 1) {
            acumulado = 0;
            printf("A la maquina le salio 1: pierde el turno y el acumulado.\n");
            break;

        } else { /* dado == 6 */
            acumulado = aplicar_regla_del_6(acumulado);
        }

        tiradas++;
    }

    return acumulado;
}

int main() {
    /* Esto inicializa el azar para que los resultados no sean siempre iguales */
    srand((unsigned int)time(NULL));

    /* Cada jugador comienza con 100 puntos (como dice la consigna) */
    int puntos_jugador = 100;
    int puntos_maquina = 100;

    /* El juego sigue mientras ambos tengan mas de 0 puntos */
    while (puntos_jugador > 0 && puntos_maquina > 0) {
        int acumulado;

        /* Turno del jugador */
        acumulado = turno_jugador();

        /* Al final del turno del jugador se le quitan puntos al contrincante */
        puntos_maquina -= acumulado;
        printf("\nSe le restan %d puntos a la maquina.\n", acumulado);
        printf("Puntos -> Jugador: %d | Maquina: %d\n", puntos_jugador, puntos_maquina);

        /* Gana quien hace que el contrario llegue primero a 0 puntos */
        if (puntos_maquina <= 0) {
            printf("\nGANASTE: la maquina llego primero a 0 puntos.\n");
            break;
        }

        /* Turno de la maquina */
        acumulado = turno_maquina();

        /* Al final del turno de la maquina se le quitan puntos al jugador */
        puntos_jugador -= acumulado;
        printf("\nLa maquina te resta %d puntos.\n", acumulado);
        printf("Puntos -> Jugador: %d | Maquina: %d\n", puntos_jugador, puntos_maquina);

        if (puntos_jugador <= 0) {
            printf("\nGANA LA MAQUINA: el jugador llego primero a 0 puntos.\n");
            break;
        }
    }

    return 0;
}