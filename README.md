[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=DrPaulValle/NOMBRE_DEL_REPOSITORIO)

# Práctica 2: Modelado y control del sistema cardiovascular mediante el modelo Windkessel

## Información de la estudiante
Garcia Grijalva Armando [23212195]; L23212195@tijuana.tecnm.mx

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente
Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivos

1. Identificar las variables y los parámetros del modelo Windkessel de cuatro elementos y relacionarlos con las propiedades hemodinámicas que representan.
2. Formular el sistema de ecuaciones diferenciales ordinarias lineales de primer orden en variables de estado.
3. Obtener las funciones de transferencia $G_{hipo}(s)$, $G_{normo}(s)$ y $G_{hiper}(s)$.
4. Analizar el error en estado estacionario y la estabilidad (polos) de los tres modelos.
5. Implementar el modelo en MATLAB/Simulink mediante ecuaciones de estado, función de transferencia y circuito equivalente en Simscape Electrical.
6. Simular la respuesta en lazo abierto de los tres modelos ante la misma señal aleatoria de excitación.
7. Sintonizar con la herramienta Tune de Simulink un controlador PID independiente para el caso hipotenso y otro para el caso hipertenso, con el fin de reducir el error respecto a la respuesta normotensa.
8. Obtener las respuestas en lazo abierto y en lazo cerrado en Python con las funciones de transferencia y verificar de forma cruzada los resultados contra MATLAB/Simulink.
9. Elaborar un diagrama biológico del sistema cardiovascular que relacione los elementos del modelo con las estructuras fisiológicas que representan.

## Descripción detallada del sistema

El modelo Windkessel de cuatro elementos representa, de manera simplificada, la dinámica del sistema arterial mediante un circuito eléctrico equivalente. Su formulación original se atribuye a Otto Frank, quien propuso representar el sistema arterial mediante una sección distensible y una resistencia periférica concentrada (modelo de dos elementos). Posteriormente se incorporó una impedancia característica asociada con la región proximal del lecho vascular y, finalmente, una inertancia que representa los efectos de la masa de la sangre en movimiento.

Palabras clave: Modelo Windkessel; Sistema cardiovascular; Circuito RLC; Controlador PID; Modelo matemático; Simulaciones numéricas.

## Lista de archivos incluidos en el repositorio
1. Cuaderno computacional de MATLAB [.mlx] y [.pdf].
2. Modelo de Simulink [.slx].
3. Archivo de Python [.py].
4. Archivo signal con 15,000 datos [.xlsx].
5. Imagen con los parámetros de ambos controladores, hipotenso e hipertenso respectivamente [.pdf].
6. Imágenes de las simulaciones en Matlab (4 en total) [.pdf].
7. Imágenes de las simulaciones en Python (3 en total) [.pdf].
8. Diagrama de Biorender [.png].
9. Análisis matemático: Función de transferencia, modelo de ecuaciones integro-diferenciales, estabilidad y error en estado estacionario [.pdf].

## Referencias
\[1] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2026. Permalink: https://biomath.xyz/course/

\[2] M. C. Khoo, Physiological Control Systems: Analysis, Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018.

\[3] F. C. Hoppensteadt and C. S. Peskin, Modeling and Simulation in Medicine and the Life Sciences. New York, USA: Springer.

\[4] J. E. Hall, Guyton and Hall Textbook of Medical Physiology, 14th ed. Philadelphia, USA: Elsevier, 2021.

\[5] K. Ogata, Ingeniería de Control Moderna, 5a ed. Madrid, España: Pearson Educación, 2010.

\[6] N. S. Nise, Control Systems Engineering, 8th ed. Hoboken, New Jersey, USA: John Wiley & Sons, 2020.

\[7] Tecnológico Nacional de México, Programa de estudio de la asignatura Modelado de Sistemas Fisiológicos, IBF-1020.
