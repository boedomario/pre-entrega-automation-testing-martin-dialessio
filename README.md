# Pre-Entrega: Automatizacion QA con Selenium y Pytest

Proyecto de automatizacion de pruebas web en SauceDemo usando Selenium WebDriver y Pytest.

## Objetivo
Automatizar los flujos basicos:
1. Login con credenciales validas
2. Verificacion del catalogo
3. Agregar un producto al carrito y validarlo

## Tecnologias
- Python 3.x
- Selenium WebDriver
- Pytest
- Pytest-HTML
- Git / GitHub

## Instalacion
git clone https://github.com/boedomario/pre-entrega-automation-testing-martin-dialessio.git
cd pre-entrega-automation-testing-martin-dialessio
python -m venv venv
source venv/bin/activate # o .\venv\Scripts\activate en Windows
pip install -r requirements.txt

## Ejecucion de pruebas
pytest -v --html=reports/reporte.html --self-contained-html

Para ejecutar por grupo:
pytest -m login
pytest -m catalogo
pytest -m carrito

## Estructura
pre-entrega-automation-testing-martin-dialessio/
├── tests/
│ └── test_saucedemo.py
├── utils/
│ ├── driver_helper.py
│ └── locators.py
├── reports/
├── pytest.ini
├── .gitignore
├── requirements.txt
└── README.md\

## Autor
Martin Dialessio
