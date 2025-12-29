# FUNDAMENTOS DE PROGRAMACIÓN

## PORTFOLIO – ACTIVIDAD 01

---

### Documento de uso de herramientas

---

**Asignatura:**  
Fundamentos de Programación

**Alumno:**  
Romina Jorgelina Antonarakis

---

**Año:**  
2025

## Creación del fichero de ejercicios y grupos musculares
Para crear el fichero de ejercicios y grupos musculares utilicé dos herramientas de inteligencia artificial como apoyo, Gemini y Chat GPT con las indicaciones solicitadas en la actividad fui comparando que se cumplieran: 
Primero definí los grupos musculares solicitados en la consigna: hombro, bíceps, tríceps, pecho, espalda, pierna y abdominales.  
Luego, para cada grupo muscular, incluí entre 3 y 5 ejercicios, respetando el mínimo y máximo pedido por el profesor.

El fichero se creó en formato CSV con dos columnas:  
- nombre del ejercicio  
- grupo muscular al que pertenece  

Este archivo se guarda junto al script de Python y es leído por el programa para generar las rutinas de entrenamiento.

## Creación del script de Python (uso de herramientas)

Para desarrollar el script en Python utilicé Visual Studio Code como editor principal y me apoyé en herramientas de inteligencia artificial para guiarme durante la construcción del programa.

En primer lugar, utilicé la IA integrada en Visual Studio Code como lo es GitHub Copilot para obtener sugerencias mientras escribía el código. Para que esas sugerencias fueran útiles, redacté un prompt inicial con el objetivo del programa y los requisitos obligatorios de la consigna (menú con 3 opciones, lectura del CSV, creación de rutina con días y minutos dentro de rango, guardado en carpeta “rutinas” en formato .txt y carga de rutinas guardadas).

A medida que avanzaba, trabajé por partes: escribía un bloque pequeño (por ejemplo, menú, lectura del CSV, generación de rutina, guardado o carga) y luego verifiqué ese bloque consultando a dos modelos externos (Gemini y ChatGPT). El objetivo de esta comparación fue confirmar que lo implementado cumplía literalmente la consigna y, cuando había diferencias, elegir la opción más simple y clara para poder comprenderla como estudiante principiante.

Finalmente, en cada ajuste que se realizaba, se revisó que el programa siguiera siendo modular (con funciones), que el flujo por consola coincidiera con lo solicitado y que el código quedara entendible mediante comentarios.

Modelos empleados:  GitHub Copilot (IA integrada de Visual Studio Code), Gemini y ChatGPT.

## Creación del programa en C (uso de herramientas)

Para el desarrollo del programa en C utilicé Visual Studio Code como entorno de trabajo y la terminal integrada para compilar y ejecutar el código.

Durante la escritura del código usé la IA integrada en Visual Studio Code (GitHub Copilot) para ayudarme con la sintaxis del lenguaje C, sobre todo en la estructura de funciones, condicionales y bucles. Para guiar esas sugerencias, escribí comentarios iniciales indicando el objetivo del programa y las reglas del juego (turnos, puntuación inicial de 100, dado de 6 caras, reglas para 1 y 6, acumulado por turno y condición de victoria).

Para asegurarme de cumplir la consigna al pie de la letra, trabajé por partes y fui verificando cada bloque: primero las funciones básicas (tiradas aleatorias), luego el turno del jugador con la pregunta de “seguir tirando”, y después el turno de la máquina con una estrategia simple (permitida por la consigna). En paralelo, consulté a Gemini y a ChatGPT para comparar interpretaciones de las reglas y confirmar que lo implementado coincidiera con lo solicitado.

Finalmente, utilicé los mensajes del compilador (errores y advertencias) como guía para corregir nombres de funciones, llaves y detalles de sintaxis, hasta lograr que el programa compilara y se ejecutara correctamente.

Herramientas usadas: Visual Studio Code, terminal integrada, compilador GCC y GitHub Copilot. Modelos de apoyo: Gemini y ChatGPT.

## Desarrollo del script en Python

El script en Python fue desarrollado de manera progresiva, priorizando la claridad del código y el uso de comentarios para facilitar su comprensión. Desde el inicio se trabajó con una estructura modular, separando el programa en funciones, tal como se vio durante la cursada.

En primer lugar, se creó un fichero CSV que contiene los ejercicios y su grupo muscular correspondiente. Este archivo es leído por el script al inicio de la ejecución, permitiendo cargar los datos de forma externa al programa. Esto facilita la organización y evita tener la información de los ejercicios escrita directamente en el código.

Luego se implementó un menú principal por consola con tres opciones obligatorias: crear una nueva rutina, cargar una rutina guardada y salir del programa. Este menú se repite hasta que el usuario decide finalizar la ejecución, permitiendo una interacción clara y controlada.

Para la creación de una nueva rutina, el programa solicita al usuario la cantidad de días de entrenamiento por semana (entre 3 y 5) y los minutos por entrenamiento (entre 45 y 90), respetando los rangos indicados en la consigna. A partir de estos datos, el script distribuye los grupos musculares asegurando que todos aparezcan al menos una vez en la rutina y que cada día tenga al menos un grupo muscular asignado.

Durante el desarrollo se incorporaron comentarios en cada bloque del código explicando qué hace cada parte y por qué se implementó de esa manera. Esto permitió comprender mejor el funcionamiento del programa y facilitar futuras modificaciones o revisiones.

Finalmente, la rutina generada se guarda en un archivo de texto dentro de un directorio denominado “rutinas”. Cada rutina se almacena con el nombre elegido por el usuario y puede ser cargada posteriormente desde el menú principal, mostrando su contenido por pantalla.

## Desarrollo del programa en C

El programa en C se desarrolló siguiendo estrictamente la consigna del juego de dados por turnos contra la máquina. Desde el inicio se priorizó un diseño simple, con funciones bien definidas y comentarios explicativos, acordes a un nivel principiante.

El programa comienza inicializando el generador de números aleatorios, necesario para simular las tiradas de los dados. Tanto el jugador como la máquina comienzan con 100 puntos, tal como indica la consigna, y el juego se desarrolla por turnos hasta que uno de los dos llega primero a 0 puntos.

Se implementaron funciones específicas para simular el lanzamiento del dado de seis caras, la elección entre multiplicador o divisor y la moneda que devuelve 2 o 3. Estas funciones permiten reutilizar código y mantener el programa ordenado.

Durante el turno del jugador, el programa permite lanzar el dado tantas veces como el usuario desee, preguntando después de cada tirada si quiere continuar. Se aplican las reglas indicadas: los valores entre 2 y 5 se acumulan, el valor 1 provoca la pérdida del turno y del acumulado, y el valor 6 activa la regla especial de multiplicación o división del acumulado.

El turno de la máquina se implementó con un comportamiento simple, permitido por la consigna, donde realiza un número limitado de tiradas. Al finalizar cada turno, el acumulado se resta a los puntos del contrincante.

A lo largo del código se incluyeron comentarios que explican el propósito de cada función, el uso de variables y la lógica de control de turnos. Esto permitió comprender el funcionamiento general del programa y facilitar la detección y corrección de errores durante la compilación y ejecución.

## Entorno de desarrollo y control de versiones

Para el desarrollo de todos los ejercicios se utilizó Visual Studio Code como entorno de programación, tanto para el script en Python como para el programa en C, aprovechando su terminal integrada para ejecutar y probar los códigos.

Todo el trabajo fue organizado en un repositorio Git, lo que permitió llevar un control de versiones mediante commits y subir la entrega completa a GitHub, tal como se solicita en la modalidad de entrega de la actividad.

Por último, se optó por presentar este documento en formato Markdown. Esta elección se realizó porque ya había utilizado este formato anteriormente (de forma breve) y me resultó una forma clara y ordenada de estructurar la información. Además, Markdown permite una correcta visualización del contenido dentro del repositorio de GitHub, facilitando la lectura y revisión del trabajo.
