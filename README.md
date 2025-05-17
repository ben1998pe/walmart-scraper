# 🛒 Walmart Scraper

Scraper de precios desarrollado en Python para buscar productos en Walmart México, extraer su información y exportarla a Excel.

---

## 🚀 Características

- Automatización con Selenium y undetected-chromedriver  
- Limpieza de precios y texto  
- Resultados exportados a Excel (`output.xlsx`)  
- Fácil de ejecutar y mantener  

---

## 🧱 Requisitos

- Python 3.8 o superior  
- Google Chrome instalado  

Instalación de dependencias:

`pip install -r requirements.txt`

---

## 🧩 Cómo usar

1. Asegúrate de tener el archivo `model_file_products.xlsx` en la misma carpeta.  
2. Agrega los productos en la columna `Producto` de ese Excel.  
3. Ejecuta el script:

`python scraper.py`

4. Al finalizar, revisa el archivo `output.xlsx` generado con los resultados.

---

## 📁 Estructura del proyecto

- scraper.py  
- model_file_products.xlsx  
- requirements.txt  
- .gitignore  
- README.md  

---

## ⚠️ Notas técnicas

- La URL de los productos no se obtiene por bloqueo de Walmart.  
- No se incluye `chromedriver.exe` en este repositorio. Puedes descargarlo desde:  
  https://sites.google.com/chromium.org/driver

---

## 📄 Licencia

MIT

---

## 👨‍💻 Autor

Desarrollado por [@ben1998pe](https://github.com/ben1998pe)  
Challenge técnico de scraping con Selenium y pandas.
