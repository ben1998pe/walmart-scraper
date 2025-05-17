"""
Walmart Scraper - Challenge técnico - Oscco Arias Benjamin

Requisitos:
- Python 3.8+
- pip install -r requirements.txt

Este script busca productos desde un archivo Excel y extrae:
- Título
- Precio actual
- Precio anterior (si existe)
- Imagen
- (Nota: la URL está bloqueada por el sitio)

Salida: output.xlsx
"""

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import urllib.parse
import time
import os
import random

def log(mensaje):
    print(f"[INFO] {mensaje}")

def iniciar_navegador():
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
    return uc.Chrome(options=options)

def extraer_datos_producto(item, producto_original):
    try:
        titulo = item.find_element(By.CSS_SELECTOR, 'span[data-automation-id="product-title"]').text
    except:
        titulo = "No disponible"

    try:
        precio = item.find_element(By.CSS_SELECTOR, 'div[aria-hidden="true"]').text
        precio = precio.replace("$", "").replace(",", "").strip()
    except:
        precio = "No disponible"

    try:
        precio_tachado = item.find_element(By.CLASS_NAME, 'strike').text
        precio_tachado = precio_tachado.replace("$", "").replace(",", "").strip()
    except:
        precio_tachado = "No disponible"

    try:
        imagen = item.find_element(By.CSS_SELECTOR, 'img[data-testid="productTileImage"]').get_attribute('src')
    except:
        imagen = "No disponible"

    link = "No disponible"  # Bloqueado por sitio

    return {
        'Producto original': producto_original,
        'Título encontrado': titulo,
        'Precio actual': precio,
        'Precio anterior': precio_tachado,
        'Imagen': imagen,
        'URL': link,
        'Vendedor': 'Walmart'
    }

def guardar_resultados_excel(lista):
    df_resultados = pd.DataFrame(lista)
    df_resultados.to_excel("output.xlsx", index=False)
    log("Exportado exitosamente a output.xlsx")

def main():
    input_file = 'model_file_products.xlsx'
    if not os.path.exists(input_file):
        log(f"Archivo '{input_file}' no encontrado.")
        return

    df = pd.read_excel(input_file)
    productos_encontrados = []
    driver = iniciar_navegador()

    for _, row in df.iterrows():
        producto_original = row['Producto']
        log(f"Buscando: {producto_original}")

        query = urllib.parse.quote_plus(producto_original)
        url = f"https://www.walmart.com.mx/search?q={query}"

        try:
            driver.get(url)

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="list-view"]'))
            )

            items = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="list-view"] > div')
            if not items:
                log("No se encontraron productos.")
                continue

            for item in items:
                data = extraer_datos_producto(item, producto_original)
                if data:
                    productos_encontrados.append(data)

            time.sleep(random.uniform(1, 3))

        except Exception as e:
            log(f"Error general con '{producto_original}': {e}")
            continue

    driver.quit()
    guardar_resultados_excel(productos_encontrados)
    log(f"Se encontraron {len(productos_encontrados)} productos en total.")

if __name__ == "__main__":
    main()
