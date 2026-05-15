# PPS05 - Proyecto Python de Análisis de Cadenas

## Información general

### Nombre del proyecto

Aplicación para obtener la cadena de mayor longitud

### Descripción del software

Este proyecto desarrolla una aplicación sencilla en Python cuyo objetivo es analizar una lista de cadenas de texto y determinar cuál de ellas tiene mayor longitud.

El programa trabaja a partir de una lista de palabras introducidas por el usuario. Posteriormente, procesa esos valores y muestra por pantalla la cadena que cumple el criterio establecido.

La lógica principal se encuentra en la función `cadena_mas_larga`, que aplica las siguientes validaciones y reglas de funcionamiento:

- La entrada debe ser obligatoriamente una lista.
- Todos los elementos recibidos deben ser cadenas de texto.
- Si la lista está vacía, el programa devuelve una cadena vacía.
- Si existen varias cadenas con la misma longitud máxima, se selecciona la primera según el orden alfabético.

El proyecto también incorpora un conjunto de pruebas automatizadas para comprobar el comportamiento del programa ante entradas correctas, casos límite y datos no válidos.

---

## Tecnologías utilizadas

- Python 3.11.9
- Librería estándar `unittest` para pruebas automatizadas
- Librerías estándar `random` y `string` para generación de datos de prueba
- Git para control de versiones
- GitHub como repositorio remoto
- Visual Studio Code como entorno de apoyo para edición y revisión del proyecto

---

## Guía de despliegue

### Requisitos previos

Para ejecutar el proyecto correctamente se necesita:

- Tener instalado Python 3.
- Tener instalado Git.
- Disponer de acceso al repositorio remoto del proyecto en GitHub.

---

### Instalación y ejecución

1. Clonar el repositorio desde GitHub:

```bash
git clone https://github.com/abragal571pps/ceti-pps5.git
```

2. Acceder a la carpeta del proyecto:

```bash
cd ceti-pps5
```

3. Crear un entorno virtual de Python. Este paso es opcional, pero recomendable para aislar el entorno de ejecución:

```bash
python -m venv .venv
```

4. Activar el entorno virtual en Windows:

```bash
.venv\Scripts\activate
```

5. Ejecutar el programa principal:

```bash
python mychar.py
```

6. Ejecutar las pruebas automatizadas:

```bash
python test_mychar.py
```

---

## Estructura del proyecto

```text
ceti-pps5/
├── mychar.py
├── test_mychar.py
├── tester.py
├── README.md
└── .gitignore
```

### Descripción de archivos principales

| Archivo | Descripción |
|---|---|
| `mychar.py` | Contiene la lógica principal del programa y la función `cadena_mas_larga`. |
| `test_mychar.py` | Incluye pruebas automatizadas para validar el comportamiento del programa. |
| `tester.py` | Archivo auxiliar incluido en el proyecto. |
| `README.md` | Documento técnico con información del proyecto, despliegue y seguridad. |
| `.gitignore` | Archivo de configuración para evitar subir elementos innecesarios o sensibles al repositorio. |

---

## Tabla de trazabilidad

| Fecha | Versión | Cambios realizados |
|---|---:|---|
| 2026-05-15 | 1.0 | Creación del repositorio local del proyecto. |
| 2026-05-15 | 1.1 | Configuración inicial de Git y preparación de la rama `desarrollo-seguro`. |
| 2026-05-15 | 1.2 | Incorporación del proyecto Python al repositorio. |
| 2026-05-15 | 1.3 | Configuración del archivo `.gitignore` para proteger archivos generados, temporales o sensibles. |
| 2026-05-15 | 1.4 | Eliminación del seguimiento de archivos generados automáticamente por Python. |
| 2026-05-15 | 1.5 | Creación de la documentación técnica del proyecto mediante `README.md`. |
| 2026-05-15 | 1.6 | Integración de los cambios de `desarrollo-seguro` en la rama `main`. |

---

## Checklist de seguridad

El repositorio incluye un archivo `.gitignore` para evitar la subida de archivos que no deben formar parte del control de versiones. Esta medida reduce el riesgo de exposición de información interna, archivos temporales o elementos dependientes del entorno local.

| Elemento protegido | Estado | Justificación técnica |
|---|---|---|
| `__pycache__/` | Ignorado | Directorio creado automáticamente por Python. Contiene archivos compilados que dependen del entorno de ejecución local. |
| `*.pyc` | Ignorado | Archivos binarios generados por Python. No son necesarios para revisar, ejecutar o mantener el código fuente. |
| `*.log` | Ignorado | Los archivos de registro pueden incluir errores, rutas internas, trazas de ejecución o información sensible. |
| `.venv/` | Ignorado | Entorno virtual local. Puede contener paquetes instalados, rutas del equipo y archivos no necesarios para el repositorio. |
| `env/` | Ignorado | Nombre común alternativo para entornos virtuales de Python. Se excluye por las mismas razones que `.venv/`. |
| `*.sqlite3` | Ignorado | Bases de datos locales o temporales. Pueden contener datos de prueba, información privada o estados no reproducibles. |
| `.env` | Ignorado | Archivo habitual para variables de entorno. Puede almacenar credenciales, claves API o configuración sensible. |
| `.vscode/` | Ignorado | Configuración específica del editor. Puede variar entre usuarios y no es necesaria para ejecutar el proyecto. |

---

## Medidas aplicadas en el repositorio

Durante la preparación del proyecto se han aplicado las siguientes medidas:

- Uso de una rama de trabajo llamada `desarrollo-seguro`.
- Separación entre la rama principal `main` y la rama utilizada para cambios.
- Documentación técnica del proyecto mediante `README.md`.
- Exclusión de archivos generados automáticamente por Python.
- Exclusión de logs, bases de datos locales, entornos virtuales y archivos de configuración sensible.
- Uso de GitHub como repositorio remoto.
- Revisión del estado del repositorio mediante comandos de Git.
- Verificación de archivos ignorados a través de `.gitignore`.

---

## Pruebas del proyecto

El proyecto incluye pruebas automatizadas desarrolladas con `unittest`.

Para ejecutar la batería de pruebas:

```bash
python test_mychar.py
```

Las pruebas contemplan diferentes escenarios:

- Listas de cadenas válidas.
- Listas vacías.
- Cadenas de igual longitud.
- Cadenas con símbolos, números o mayúsculas.
- Entradas no válidas.
- Elementos que no son cadenas de texto.
- Casos generados de forma aleatoria.

Estas pruebas permiten comprobar que la función principal mantiene un comportamiento estable ante diferentes tipos de entrada.

---

## Gestión de ramas

La práctica se desarrolla siguiendo una estrategia básica de ramas.

La rama principal del proyecto es:

```text
main
```

La rama utilizada para realizar cambios de forma segura es:

```text
desarrollo-seguro
```

El objetivo de esta separación es evitar trabajar directamente sobre la rama principal. De esta forma, los cambios se preparan primero en una rama de desarrollo y posteriormente se integran en `main` mediante una operación de fusión.

---

## Fusión de cambios

Una vez finalizada la configuración inicial, los cambios realizados en `desarrollo-seguro` se integran en `main`.

En este proyecto, la fusión se realiza mediante un Merge Commit, ya que el repositorio local y la rama remota `main` presentan historiales no relacionados. Esto ocurre porque el repositorio remoto ya contenía commits propios, mientras que el repositorio local también tenía commits creados durante la práctica.

Al no existir un historial común directo, Git no puede aplicar una fusión Fast-forward. Por ese motivo, es necesario crear un commit de fusión que una ambos historiales.

El comando utilizado para permitir esta operación es:

```bash
git merge desarrollo-seguro --allow-unrelated-histories
```

---

## Conclusión

Este documento resume la estructura técnica del proyecto, las instrucciones necesarias para su ejecución y las decisiones de seguridad aplicadas durante la preparación del repositorio.

El uso de ramas, la configuración de `.gitignore` y la documentación del proceso permiten mantener un repositorio más ordenado, seguro y fácil de revisar.


- (GPG)
