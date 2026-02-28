import pandas as pd
import codecs

def cargar_y_limpiar():
    # Cargar datos
    df = pd.read_csv('data/personas.csv')

    # =========================
    # 1️⃣ LIMPIAR ESPACIOS
    # =========================
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip()

    # =========================
    # 2️⃣ QUITAR CARACTERES ESPECIALES (excepto necesarios)
    # =========================
    df = df.replace(r'[^a-zA-Z0-9@.\-\s]', '', regex=True)

    # =========================
    # 3️⃣ DESCIFRAR NOMBRES (ROT13)
    # =========================
    df['nombre'] = df['nombre_cifrado'].apply(
        lambda x: codecs.decode(str(x), 'rot_13')
    )

    df['apellido'] = df['apellido_cifrado'].apply(
        lambda x: codecs.decode(str(x), 'rot_13')
    )

    # =========================
    # 4️⃣ NORMALIZAR TEXTO
    # =========================
    df['nombre'] = df['nombre'].str.title()
    df['apellido'] = df['apellido'].str.title()
    df['ciudad'] = df['ciudad'].str.title()
    df['profesion'] = df['profesion'].str.title()
    df['email'] = df['email'].str.lower()

    # =========================
    # 5️⃣ LIMPIAR SALARIO
    # =========================
    df['salario'] = df['salario'].replace(r'[^0-9]', '', regex=True)
    df['salario'] = pd.to_numeric(df['salario'], errors='coerce')

    # =========================
    # 6️⃣ NORMALIZAR ACTIVO
    # =========================
    df['activo'] = df['activo'].astype(str).str.lower()

    df['activo'] = df['activo'].replace({
        'true': True,
        '1': True,
        'si': True,
        'yes': True,
        'false': False,
        '0': False,
        'no': False
    })

    # =========================
    # 7️⃣ CONVERTIR FECHAS
    # =========================
    df['fecha_nacimiento'] = pd.to_datetime(
        df['fecha_nacimiento'],
        errors='coerce'
    )

    return df