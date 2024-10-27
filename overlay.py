import PyPDF2, os, re

def overlayArchivos(basePDF,overPDF,outputPDF=None):
    basePDFReader = PyPDF2.PdfReader(open(basePDF,'rb'))
    overPDFReader = PyPDF2.PdfReader(open(overPDF,'rb'))
    overPDFPage = overPDFReader.pages[0]

    pdfWriter = PyPDF2.PdfWriter() if outputPDF else None

    for page_num in range(len(basePDFReader.pages)):
        page = basePDFReader.pages[page_num]
        page.merge_page(overPDFPage)
        if pdfWriter:
            pdfWriter.add_page(page)
        else:
            basePDFReader.pages[page_num] = page
    
    if pdfWriter:
        # Crear el subdirectorio si no existe
        subdirectorio = "output"  # Puedes cambiar el nombre del subdirectorio
        os.makedirs(subdirectorio, exist_ok=True)

        # Crear la ruta completa al archivo de salida
        output_path = os.path.join(subdirectorio, outputPDF)
        with open(output_path,'wb') as outputFile:
            pdfWriter.write(outputFile)
    else:
        with open(basePDF,'wb') as outputFile:
            basePDFReader.write(outputFile)

def superPonerArchivos(directorio, archivoBase, fecha):
    """
    Superpone un archivo PDF base sobre todos los archivos PDF en un directorio que coincidan con un patrón de fecha.

    Args:
        directorio: Ruta al directorio donde buscar los archivos PDF.
        archivoBase: Ruta al archivo PDF base.
        fecha: Patrón de búsqueda para la fecha en los nombres de archivo.

    Returns:
        Una lista con los nombres de los archivos procesados o una lista vacía si ocurre un error.
    """
    patron = fecha
    try:
        # Verificar existencia del directorio y del archivo base
        if not os.path.exists(directorio):
            raise FileNotFoundError(f"El directorio '{directorio}' no existe.")
        if not os.path.isfile(archivoBase):
            raise FileNotFoundError(f"El archivo base '{archivoBase}' no existe.")

        # Utilizar una expresión generadora para mejorar la eficiencia
        listado = (archivo for archivo in os.listdir(directorio)
        if archivo.endswith('.pdf') and re.search(patron, archivo, re.IGNORECASE))

        if(listado):
            for archivo in listado:
                overlayArchivos(os.path.join(directorio, archivo),archivoBase,archivo)
        else:
            print("No se encontraron archivos para esa fecha")
            return False
    except (FileNotFoundError, PermissionError, OSError) as e:
        print(f"Error al procesar el directorio: {e}")
        return []
    except Exception as e:  # Capturar otras excepciones inesperadas
        print(f"Error inesperado: {e}")
        return []
