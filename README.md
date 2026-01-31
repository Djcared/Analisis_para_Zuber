# Analisis_para_Zuber
el proyecto consiste en un análisis de datos para una nueva empresa de taxis llamada Zuber, que opera en Chicago.  El objetivo principal es entender las preferencias de los pasajeros y el impacto de factores externos (como el clima) en los viajes.

Análisis de Datos: Estrategia de Lanzamiento para Zuber en Chicago
1. Descripción del Proyecto
Este proyecto analiza el mercado de taxis en Chicago para apoyar el lanzamiento de Zuber, una nueva empresa de viajes compartidos. El objetivo es identificar patrones en las preferencias de los pasajeros y evaluar cómo factores externos (como el clima) impactan la duración de los viajes, permitiendo decisiones basadas en datos para la planeación logística.

2. Metodología y Herramientas
- Lenguaje: Python

- Librerías: Pandas, Matplotlib, Scipy (Stats), BeautifulSoup4 (Web Scraping).

Proceso:

- Recolección: Scraping de datos meteorológicos para correlacionar eventos climáticos con registros de viajes.

- Procesamiento: Limpieza de datos, manejo de tipos datetime y unión de bases de datos mediante SQL.

- Análisis: Visualización de la cuota de mercado por empresa y distribución geográfica de la demanda.

- Estadística: Prueba de hipótesis para medir el impacto de la lluvia en la logística.

  3. Hallazgos.
     Concentración de Mercado y DemandaEl análisis reveló que la demanda en Chicago está extremadamente centralizada.
     Puntos Críticos: Barrios como Loop, River North y Streeterville concentran la mayor cantidad de finalizaciones de viajes.
     Competencia: Identificamos que el mercado tiene líderes claros, lo que sugiere que Zuber debe enfocarse en la eficiencia en zonas de alta densidad.
     
     Análisis de Factores Externos (Clima)
     
     Utilizamos una prueba de hipótesis estadística para determinar si el clima afectaba la duración de los viajes desde el centro (Loop) hasta el aeropuerto (O'Hare).
     Hipótesis Nula ($H_0$): La duración promedio de los viajes los sábados lluviosos no varía frente a los sábados soleados.
     Hipótesis Alternativa ($H_1$): La duración promedio de los viajes cambia significativamente bajo condiciones climáticas adversas.
     Resultado: Con un p-value < 0.05, rechazamos la hipótesis nula, existe evidencia estadística suficiente para afirmar que el clima afecta la duración del viaje, lo que implica la necesidad de ajustar estimaciones de tiempo y tarifas en días lluviosos.

4. Conclusiones y Recomendaciones.
   Optimización de Flota: Zuber debe priorizar la disponibilidad de conductores en los 10 barrios principales identificados para maximizar la ocupación.
   Modelo de Predicción: La variabilidad confirmada por la prueba estadística justifica la implementación de un modelo de "Precios Dinámicos" o "Tiempos Estimados" sensibles al clima.
   Ventaja Competitiva: Ofrecer una mayor fiabilidad de llegada al aeropuerto durante condiciones climáticas adversas podría ser el diferenciador clave para captar clientes de la competencia establecida.
