import pandas as pd
with open("v4test.csv", 'r') as csvfile:
    df = pd.read_csv(csvfile)
    print(df)
    df = df.drop(['DESCRIPCION_CIC', 'CODIGO_VST','FECHA_PLANIFICADA_VST', 'FECHA_CREACION_USW'], axis=1)

     # Escenario 1 Numero de visitas anual por empleado
    df_new1=df.groupby(['PRIMERAPELLIDO_US','SEGUNDOAPELLIDO_US','PRIMERNOMBRE_US','SEGUNDONOMBRE_US'])['NUMEROCONTACTO_VST'].max()
    print(df_new1)


    def add_numbers(x, y, z=None):
        if (z == None):
            return x + y
        else:
            return x + y + z


    print(add_numbers(1, 2))
    print(add_numbers(1, 2, 3))
    df_new1.to_csv('Escenario1.csv')



