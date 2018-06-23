import pandas as pd
import numpy as np



def main():
    with open('../resources/v4test.csv') as csvfile:

        df = pd.read_csv(csvfile)
        df = df.drop(['DESCRIPCION_CIC', 'CODIGO_VST','FECHA_PLANIFICADA_VST', 'FECHA_CREACION_USW'], axis=1)

        # Escenario 1 Numero de visitas anual por empleado
        df_new1=df.groupby(['PRIMERAPELLIDO_US','SEGUNDOAPELLIDO_US','PRIMERNOMBRE_US','SEGUNDONOMBRE_US'])['NUMEROCONTACTO_VST'].sum()
        print(df_new1)
        df_new1.to_csv('Escenario1.csv')

        # Escenario 2 Empresa numero de visitas
        df_new2 = df.groupby(['NOMBRE_EMP','FECHA_VST'])['NUMEROCONTACTO_VST'].sum()
        df_new2.to_csv('Escenario2.csv')
        print(df_new2)


if __name__ == "__main__":
    main()
