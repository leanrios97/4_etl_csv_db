# Proyecto ETL

Este es un pipeline ETL (Extract, Transform, Load) modular diseñado para procesar datos desde archivos CSV y cargarlos en una base de datos. El proyecto sigue buenas prácticas de ingeniería de software, incluyendo una arquitectura limpia y el cumplimiento de los principios SOLID.

## Arquitectura

El proyecto utiliza la **Arquitectura Limpia**, que separa las preocupaciones en capas distintas:
- **Dominio**: Contiene la lógica de negocio central y entidades (e.g., `data_entity.py`), independiente de sistemas externos.
- **Aplicación**: Orquesta el proceso ETL a través de servicios (e.g., `etl_service.py`), coordinando el flujo entre capas.
- **Infraestructura**: Implementa los detalles técnicos, como lectores de archivos (e.g., `csv_reader.py`), transformadores (e.g., `basic_transformer.py`) y escritores de base de datos (e.g., `sql_writer.py`).
- **Configuración**: Gestiona configuraciones y variables de entorno (e.g., `settings.py`).

Esta separación asegura escalabilidad, testabilidad y mantenibilidad.

## Patrones de Diseño

Se implementaron los siguientes patrones de diseño:
- **Patrón Repository**: Abstrae el acceso a datos (e.g., `sql_writer.py` usa una sesión para interactuar con la base de datos).
- **Patrón Factory**: Utilizado en `connection_factory.py` para crear conexiones a la base de datos dinámicamente.
- **Patrón Strategy**: Permite diferentes estrategias de transformación al implementar la interfaz `DataTransformer`.
- **Inyección de Dependencias**: Facilita el desacoplamiento inyectando dependencias (e.g., `ETLService` acepta instancias de `DataReader`, `DataTransformer` y `DataWriter`).

## Principios SOLID

El proyecto adhiere a los principios SOLID:
- **Single Responsibility (Responsabilidad Única)**: Cada clase o módulo tiene una sola responsabilidad (e.g., `CSVReader` solo lee archivos CSV).
- **Open/Closed (Abierto/Cerrado)**: Nuevas transformaciones o lectores se pueden agregar implementando interfaces sin modificar código existente.
- **Liskov Substitution (Sustitución de Liskov)**: Las interfaces permiten intercambiar implementaciones (e.g., cambiar `CSVReader` por un `JSONReader`).
- **Interface Segregation (Segregación de Interfaces)**: Interfaces específicas (e.g., `DataReader`, `DataTransformer`) evitan que las clases dependan de métodos no utilizados.
- **Dependency Inversion (Inversión de Dependencias)**: Los módulos de alto nivel dependen de abstracciones (interfaces) en lugar de implementaciones concretas.

## Tecnologías

- **Lenguaje**: Python 3.9+
- **Bibliotecas**:
  - `pandas` para manipulación de datos
  - `sqlalchemy` para interacciones con bases de datos
  - `pydantic` para validación de datos
  - `pydantic-settings` y `python-dotenv` para gestión de configuraciones
  - `psycopg2-binary` para soporte de PostgreSQL
- **Base de Datos**: Configurable (predeterminada: PostgreSQL, pero soporta otras vía SQLAlchemy)

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd etl_project
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configura las variables de entorno en `.env` (ver sección de Configuración).

## Uso

1. Asegúrate de colocar un archivo CSV de ejemplo en `data/input/sample_data.csv` con columnas `id`, `name` y `value`.
2. Ejecuta el pipeline ETL:
   ```bash
   python scripts/run_etl.py
   ```
3. Verifica los datos en tu base de datos (configurada vía `.env`).

## Configuración (Archivo `.env`)

El archivo `.env` contiene las variables de entorno necesarias para el funcionamiento del proyecto. Un ejemplo típico sería:

```
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/mydb
CSV_FILE_PATH=data/input/sample_data.csv
```

- `DATABASE_URL`: URL de conexión a la base de datos (e.g., `postgresql://usuario:contraseña@host:puerto/base_de_datos` para PostgreSQL).
- `CSV_FILE_PATH`: Ruta al archivo CSV de entrada.

Crea o edita el archivo `.env` en la raíz del proyecto con tus valores específicos.

## Pruebas

Ejecuta las pruebas unitarias e integración:
```bash
python -m unittest discover -s tests
```
- **Pruebas Unitarias**: Ubicadas en `tests/unit/`, prueban componentes individuales.
- **Pruebas de Integración**: Ubicadas en `tests/integration/`, prueban el pipeline completo.

## Estructura del Proyecto

```
etl_project/
├── src/                # Código fuente
│   ├── domain/         # Entidades y interfaces de negocio
│   ├── application/    # Capa de servicios
│   ├── infrastructure/ # Implementaciones técnicas
│   └── config/         # Configuraciones
├── tests/              # Suites de pruebas
├── data/               # Datos de entrada y salida
├── scripts/            # Scripts ejecutables
├── .env                # Variables de entorno
├── requirements.txt    # Dependencias
└── README.md           # Este archivo
```

