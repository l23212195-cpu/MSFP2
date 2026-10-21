[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=DrPaulValle/NOMBRE_DEL_REPOSITORIO)

# Práctica 5.4: Modelado y control del sistema cardiovascular mediante el modelo Windkessel

## Información de la estudiante
Nombre completo [correo@tijuana.tecnm.mx]

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente
Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Competencia a desarrollar

Modeliza sistemas fisiológicos mediante circuitos eléctricos equivalentes, ecuaciones diferenciales y funciones de transferencia para analizar su comportamiento dinámico y diseña estrategias de control mediante técnicas de control clásico. En particular, durante la práctica se analiza el modelo Windkessel de cuatro elementos, se compara la dinámica cardiovascular de un individuo normotenso (control) con dos casos simulados, hipotenso e hipertenso, y se diseñan estrategias de control *in silico* orientadas a reducir las diferencias entre las respuestas de los casos y la respuesta de referencia.

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

La analogía entre las variables hemodinámicas y las eléctricas es:

| Variable hemodinámica | Variable eléctrica |
|---|---|
| Presión | Voltaje |
| Flujo sanguíneo | Corriente |

Los elementos del modelo son:

| Elemento | Significado hemodinámico | Analogía eléctrica |
|---|---|---|
| $Z$ | Impedancia característica de la región proximal del sistema arterial (aorta proximal) | Resistor |
| $C$ | Distensibilidad arterial total (capacidad de almacenar volumen mediante distensión) | Capacitor |
| $R$ | Resistencia periférica | Resistor |
| $L$ | Inertancia arterial (efectos inerciales por aceleración y desaceleración de la sangre) | Inductor |

Las variables del modelo son $P_a(t)$ (presión arterial de entrada), $P_p(t)$ (presión sobre la distensibilidad arterial), $F_a(t)$ (flujo dirigido hacia la aorta o arteria pulmonar) y $F_L(t)$ (flujo a través de la inertancia arterial).

A pesar de estar constituido por cuatro elementos, el modelo contiene solamente dos elementos independientes de almacenamiento de energía ($C$ y $L$), por lo que es un **sistema de segundo orden** descrito por dos variables de estado.

> **Nota:** la práctica se desarrolla exclusivamente mediante experimentación *in silico*. Las estrategias de control desarrolladas tienen propósitos exclusivamente académicos y de simulación, y no constituyen una estrategia terapéutica ni una recomendación para el tratamiento de alteraciones de la presión arterial.

Palabras clave: Modelo Windkessel; Sistema cardiovascular; Circuito RLC; Controlador PID; Modelo matemático; Simulaciones numéricas.

## Desarrollo matemático

### Ecuaciones del circuito

Se seleccionan como variables de estado $x_1(t)=F_L(t)$ y $x_2(t)=P_p(t)$, y como entrada $u(t)=P_a(t)$. Como $Z$ y $L$ están en paralelo entre los nodos $P_a(t)$ y $P_p(t)$, ambos presentan la misma diferencia de presión.

Para la inertancia:

$$P_a(t)-P_p(t)=L\frac{dF_L(t)}{dt}\quad\Rightarrow\quad \frac{dF_L(t)}{dt}=-\frac{1}{L}P_p(t)+\frac{1}{L}P_a(t)$$

Para la impedancia característica:

$$F_Z(t)=\frac{P_a(t)-P_p(t)}{Z}$$

Conservación del flujo en el nodo de $P_p(t)$:

$$F_Z(t)+F_L(t)=F_C(t)+F_R(t),\qquad F_C(t)=C\frac{dP_p(t)}{dt},\qquad F_R(t)=\frac{P_p(t)}{R}$$

De donde:

$$\frac{dP_p(t)}{dt}=\frac{1}{C}F_L(t)-\left(\frac{1}{ZC}+\frac{1}{RC}\right)P_p(t)+\frac{1}{ZC}P_a(t)$$

### Ecuaciones de estado

$$\dot{\mathbf{x}}(t)=\begin{bmatrix}0 & -\dfrac{1}{L}\\[2mm] \dfrac{1}{C} & -\left(\dfrac{1}{ZC}+\dfrac{1}{RC}\right)\end{bmatrix}\mathbf{x}(t)+\begin{bmatrix}\dfrac{1}{L}\\[2mm] \dfrac{1}{ZC}\end{bmatrix}P_a(t),\qquad \mathbf{x}(t)=\begin{bmatrix}F_L(t)\\P_p(t)\end{bmatrix}$$

$$y(t)=P_p(t)=\begin{bmatrix}0 & 1\end{bmatrix}\mathbf{x}(t)$$

### Función de transferencia

Aplicando la transformada de Laplace con condiciones iniciales nulas:

$$F_L(s)=\frac{P_a(s)-P_p(s)}{Ls},\qquad Cs\,P_p(s)=F_L(s)+\frac{P_a(s)-P_p(s)}{Z}-\frac{P_p(s)}{R}$$

Despejando y multiplicando por $LsZR$:

$$G(s)=\frac{P_p(s)}{P_a(s)}=\frac{LR\,s+ZR}{LZRC\,s^2+(LR+LZ)\,s+ZR}$$

El orden de la función de transferencia (2) coincide con el número de elementos independientes de almacenamiento de energía ($L$ y $C$). Presenta un cero real en $s=-Z/L$.

## Parámetros de los tres casos

Las diferencias entre los casos se establecen modificando únicamente la distensibilidad arterial $C$; $Z$, $L$ y $R$ se mantienen constantes.

| Parámetro | Hipotenso | Normotenso (control) | Hipertenso | Unidades |
|---|---|---|---|---|
| $Z$ | 0.010 | 0.010 | 0.010 | mmHg·s·ml⁻¹ |
| $L$ | 0.001 | 0.001 | 0.001 | mmHg·s²·ml⁻¹ |
| $R$ | 1.000 | 1.000 | 1.000 | mmHg·s·ml⁻¹ |
| $C$ | 3.500 | 1.500 | 1.000 | ml·mmHg⁻¹ |

Un aumento de $C$ (hipotenso) representa un sistema arterial con mayor capacidad de distenderse y almacenar volumen, lo que tiende a atenuar los incrementos de presión. Una disminución de $C$ (hipertenso) representa menor distensibilidad y mayor rigidez arterial, de modo que una variación de volumen produce cambios de presión más pronunciados.

### Funciones de transferencia resultantes

Con $Z=0.01$, $L=0.001$ y $R=1$:

$$G(s)=\frac{0.001\,s+0.01}{10^{-5}C\,s^2+0.00101\,s+0.01}$$

| Caso | $C$ | $G(s)$ |
|---|---|---|
| Hipotenso | 3.5 | $\dfrac{0.001\,s+0.01}{3.5\times10^{-5}s^2+0.00101\,s+0.01}$ |
| Normotenso | 1.5 | $\dfrac{0.001\,s+0.01}{1.5\times10^{-5}s^2+0.00101\,s+0.01}$ |
| Hipertenso | 1.0 | $\dfrac{0.001\,s+0.01}{1.0\times10^{-5}s^2+0.00101\,s+0.01}$ |

### Error en estado estacionario

Para una entrada escalón unitario, por el teorema del valor final:

$$P_p(\infty)=\lim_{s\to0}s\,G(s)\frac{1}{s}=G(0)=\frac{ZR}{ZR}=1$$

Los tres modelos tienen ganancia en estado estacionario unitaria, independiente de $C$, por lo que el error en estado estacionario ante un escalón es cero en los tres casos y la diferencia entre el caso y la referencia normotensa también tiende a cero. Las diferencias entre los casos se manifiestan en el comportamiento **transitorio**.

### Análisis de estabilidad (polos)

| Caso | Polos | $\omega_n$ (rad/s) | $\zeta$ | Tipo de respuesta |
|---|---|---|---|---|
| Hipotenso | $-14.43 \pm 8.81j$ | 16.90 | 0.854 | Subamortiguada |
| Normotenso | $-55.27$, $-12.06$ | 25.82 | 1.304 | Sobreamortiguada |
| Hipertenso | $-89.87$, $-11.13$ | 31.62 | 1.597 | Sobreamortiguada |

Los polos de los tres modelos se encuentran en el semiplano izquierdo, por lo que los tres sistemas son estables. Al disminuir $C$ aumenta $\omega_n=\sqrt{1/(LC)}$ y el sistema pasa de subamortiguado a sobreamortiguado.

> Valores calculados analíticamente; verifica que coincidan con los obtenidos en MATLAB (`pole`, `pzmap`) y Python.

![Mapa de polos y ceros](figuras/polos_ceros.png)

## Metodología

### Señal de excitación

Se utiliza en Simulink el bloque *Uniform Random Number* con la misma realización para los tres modelos, de modo que las diferencias en las respuestas se deban exclusivamente a los parámetros:

| Parámetro | Valor |
|---|---|
| Mínimo (`min`) | −0.2 |
| Máximo (`max`) | 1 |
| Semilla (`seed`) | 106 |
| Tiempo de muestreo (`Ts`) | 0.1 s |
| Intervalo de simulación | $t\in[0,15]$ s |

### Esquema de control

Cada caso se analiza de manera independiente con el esquema de la Figura 5.2 de la guía, utilizando la respuesta del individuo normotenso como referencia:

$$e_{hipo}(t)=P_{p,normo}(t)-P_{p,hipo}(t),\qquad e_{hiper}(t)=P_{p,normo}(t)-P_{p,hiper}(t)$$

Se construyen dos sistemas de retroalimentación: normotenso–hipotenso y normotenso–hipertenso, cada uno con un bloque *PID Controller* sintonizado mediante la herramienta *Tune* de Simulink.

### Plataformas de implementación

| Plataforma | Implementación |
|---|---|
| MATLAB/Simulink | Ecuaciones de estado, función de transferencia y sistemas de control con PID |
| Simscape Electrical | Circuito equivalente Windkessel |
| MATLAB (cuaderno computacional) | Ejecución de los modelos, almacenamiento en el Workspace y función de graficación (guarda figuras en PDF) |
| Python (Visual Studio Code) | Funciones de transferencia en lazo abierto y lazo cerrado con las ganancias obtenidas en *Tune* |

## Resultados

### Respuesta en lazo abierto

[Insertar figura y describir la comparación de $P_{p,hipo}(t)$, $P_{p,normo}(t)$ y $P_{p,hiper}(t)$.]

![Respuesta en lazo abierto](figuras/lazo_abierto.png)

### Ganancias de los controladores PID

| Caso | $k_P$ | $k_I$ | $k_D$ |
|---|---|---|---|
| Hipotenso | [valor] | [valor] | [valor] |
| Hipertenso | [valor] | [valor] | [valor] |

![Configuración de la sintonización con Tune](figuras/tune_parametros.png)

### Respuesta en lazo cerrado

**Caso hipotenso:** comparación de $P_{p,normo}(t)$, $P_{p,hipo}(t)$ y $P_{p,hipo,PID}(t)$.

![Lazo cerrado hipotenso](figuras/lazo_cerrado_hipotenso.png)

**Caso hipertenso:** comparación de $P_{p,normo}(t)$, $P_{p,hiper}(t)$ y $P_{p,hiper,PID}(t)$.

![Lazo cerrado hipertenso](figuras/lazo_cerrado_hipertenso.png)

[Analizar el efecto de cada controlador sobre el seguimiento de la referencia, el error y el comportamiento transitorio.]

### Verificación entre plataformas

Se comparan las respuestas obtenidas con: (a) ecuaciones de estado en Simulink, (b) funciones de transferencia en Simulink, (c) circuito en Simscape Electrical, (d) cuaderno computacional de MATLAB y (e) código en Python.

| Comparación | Máxima diferencia absoluta | Observaciones |
|---|---|---|
| Estado vs. función de transferencia | [valor] | [comentario] |
| Simulink vs. Simscape | [valor] | [comentario] |
| MATLAB vs. Python | [valor] | [comentario] |

[Analizar diferencias asociadas con el método numérico, la discretización de la señal aleatoria o la implementación de los modelos.]

### Diagrama biológico

Diagrama elaborado en BioRender que relaciona los elementos del modelo con las estructuras fisiológicas: corazón, aorta, grandes arterias, vasos periféricos, flujo sanguíneo, presión arterial, distensibilidad arterial y resistencia periférica.

![Diagrama biológico](figuras/diagrama_biologico.png)

| Elemento del modelo | Estructura / propiedad fisiológica |
|---|---|
| $Z$ | Aorta proximal (impedancia característica) |
| $C$ | Distensibilidad de la aorta y grandes arterias |
| $R$ | Vasos periféricos (resistencia periférica) |
| $L$ | Inercia de la columna de sangre en movimiento |

## Discusión

[Discutir el efecto de $C$ sobre la dinámica, la diferencia entre respuestas subamortiguada y sobreamortiguada, el desempeño de cada controlador, las limitaciones del modelo lineal de parámetros concentrados y la consistencia entre plataformas.]

## Conclusiones

[Redactar las conclusiones de la práctica.]

## Lista de archivos incluidos en el repositorio
1. Desarrollo matemático del modelo Windkessel, ecuaciones de estado y funciones de transferencia (este README).
2. Tabla de parámetros de los modelos hipotenso, normotenso e hipertenso.
3. Cuaderno computacional de MATLAB [.mlx y .pdf].
4. Modelos de Simulink [.slx] (ecuaciones de estado, función de transferencia y lazo cerrado con PID).
5. Modelo del circuito en Simscape Electrical [.slx].
6. Archivo de Python [.py].
7. Señal de entrada utilizada en las simulaciones.
8. Imagen con los parámetros y la configuración de la sintonización de los controladores.
9. Figuras de las simulaciones en MATLAB y Python [.pdf].
10. Resultados de los sistemas en lazo abierto y en lazo cerrado.
11. Ganancias obtenidas para los dos controladores PID.
12. Diagrama biológico (BioRender).
13. Capturas de las simulaciones.
14. Archivos complementarios utilizados durante la práctica.
15. Archivo CITATION.cff con la información de la estudiante y del repositorio.

## Referencias
\[1] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2026. Permalink: https://biomath.xyz/course/

\[2] M. C. Khoo, Physiological Control Systems: Analysis, Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018.

\[3] F. C. Hoppensteadt and C. S. Peskin, Modeling and Simulation in Medicine and the Life Sciences. New York, USA: Springer.

\[4] J. E. Hall, Guyton and Hall Textbook of Medical Physiology, 14th ed. Philadelphia, USA: Elsevier, 2021.

\[5] K. Ogata, Ingeniería de Control Moderna, 5a ed. Madrid, España: Pearson Educación, 2010.

\[6] N. S. Nise, Control Systems Engineering, 8th ed. Hoboken, New Jersey, USA: John Wiley & Sons, 2020.

\[7] Tecnológico Nacional de México, Programa de estudio de la asignatura Modelado de Sistemas Fisiológicos, IBF-1020.
