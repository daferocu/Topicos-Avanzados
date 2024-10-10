# Taller 2 

Class: Topicos avanzados de Analitíca <br>
Code:  <br>
Professor:  <br>
Members:
    - Diana Katherin Ibáñez
    - Daniel Felipe Rodríguez
    - Paola Andrea Castro
    - Oscar Correcha
    - Erika Cárdenas

Notas para ejecutar la Api en FastAPi

## Table of Contents

- <a href='#1'>1. Despliegue de API </a>
- <a href='#2'>2. Uso local de la API </a>
- <a href='#3'>3. Uso de ejemplos </a>

<hr>

### <a id='1'> Despliegue de API </a>

1. "Crear un entorno virtual de Python (compatible con Windows)

```bash
python -m venv env
```

![crear_ambiente](images/img1.png)

2. Activar el entorno virtual

```bash
source env/Scripts/activate
```

![levantar_ambiente](images/img2.png)

3. Instalar los requisitos del sistema especificados en el archivo requirements.txt

```bash
pip install -r requirements.txt
python -m pip install --upgrade pip
```

![instalar](images/img3.png)

4. Para ejecutar la API, utiliza el siguiente comando:

```bash
python -m uvicorn main:app --reload
```

![comando](images/img4.png)

A continuación, se procederá a abrir un navegador web e ingresar a la siguiente página:

```bash
http://127.0.0.1:8000/docs
```

![visual](images/img5.png)

### <a id='2'> Uso local de la API </a>

Al acceder a la API, se debe seleccionar el módulo 'predict'.

![predict](images/img6.png)

 Para activar las funciones de predicción, por favor, haga clic en el botón 'Try it out'.

![inicio_funcion](images/img7.png)


### <a id='3'> Uso de ejemplos </a>

La carpeta 'examples' contiene ejemplos en formato JSON que pueden utilizarse como entrada para la API.

![ejemplos_uso](images/img8.png)

Se selecciona uno de los ejemplos, concretamente example1.json, y se introduce en el campo de la API siguiendo el mismo formato.

![ejemplos_uso2](images/img9.png)

Se pone en marcha al hacer clic en 'Execute'.

![ejemplos_uso3](images/img10.png)

En la parte inferior se presenta el resultado obtenido por el modelo en pantalla.

![ejemplos_resultado](images/img11.png)

<hr>

[Go to Top](#Table-of-Contents)