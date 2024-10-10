import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score

def highlight_min_max(s, color_min='crimson', color_max='cornflowerblue'):
    """
    Applies conditional formatting to highlight minimum and maximum values in a Series.

    Args:
        s (pd.Series): The Series to format.
        color_min (str, optional): The background color for minimum values. Defaults to 'red'.
        color_max (str, optional): The background color for maximum values. Defaults to 'blue'.

    Returns:
        list: A list of CSS styles to apply to each element in the Series,
              with background colors indicating minimum, maximum, or no specific value.
    """

    is_min = s == s.min()
    is_max = s == s.max()

    return [
        f'background-color: {color_min}' if v else (f'background-color: {color_max}' if w else '')
        for v, w in zip(is_min, is_max)
    ]


def print_metrics(modelo, pred_train, pred_test, origin_train, origin_test):
    """
    Prints classification metrics.

    Args:
        pred_train: The predicted labels training.
        pred_test: The predicted labels testing.
        origin_training: The true labels.
        origin_test: The true labels.
    Returns:
        DataFrame con las métricas.
    """

    metrics = {
        'AUC entrenamiento': roc_auc_score(origin_train, pred_train, average='macro'),
        'AUC testeo' : roc_auc_score(origin_test, pred_test, average='macro')
    }

    print('')
    print(f'The results of the adjustment metrics - {modelo}:')
    print('')
    
    for metric, value in metrics.items():
        print(f"      {metric}: {value:.3f}")

    metrics['Modelo'] = modelo

    return metrics


def comparar_metricas(*args, **kwargs):
    """
    Compara múltiples diccionarios de métricas y devuelve un DataFrame.

    Args:
        *args: Diccionarios de métricas.
        **kwargs:
            index_name: Nombre de la columna del índice (por defecto 'metrica').

    Returns:
        DataFrame con las métricas comparadas.
    """

    dfs = []
    index_name = kwargs.get('index_name', 'metrica')

    for i, metric_dict in enumerate(args):
        df = pd.DataFrame.from_dict(metric_dict, orient='index', columns=[f'Modelo_{i+1}'])
        dfs.append(df)

    df_comparacion = pd.concat(dfs, axis=1)
    df_comparacion = df_comparacion.T
    df_comparacion.index = df_comparacion.index.str.replace('_', ' ')
    df_comparacion = df_comparacion.set_index('Modelo').reset_index()

    styled_df = df_comparacion.style.apply(highlight_min_max)
    return styled_df


def grafico_metricas(dataframe):
    """
    Generates a scatter plot comparing AUC training and testing values across models.

    Args:
        dataframe (pandas.DataFrame): DataFrame containing model names and AUC metrics.

    Returns:
        None (the function displays the plot directly).
    """
    
    df = dataframe.data

    # Crear el scatter plot y lineas punteadas
    plt.figure(figsize=(15, 6))
    plt.scatter(df['Modelo'], df['AUC entrenamiento'], color='blue', label='AUC entrenamiento')
    plt.scatter(df['Modelo'], df['AUC testeo'], color='red', label='AUC testeo')

    plt.axhline(y=0.89, color='orange', linestyle='dashed', linewidth=2, label='Umbral de desempeño')

    plt.axhline(y=max(df['AUC testeo']), color='green', linestyle='dashed', linewidth=2)
    plt.axvline(x=df['Modelo'][df['AUC testeo'].idxmax()], color='green', linestyle='dashed', linewidth=2, label=f'Modelo: {df['Modelo'][df['AUC testeo'].idxmax()]} \n AUC: {round(max(df['AUC testeo']),3)}')

    # Personalizar el gráfico
    plt.xlabel('Modelo')
    plt.ylabel('AUC')
    plt.title('Comparación de AUC para diferentes modelos')
    plt.xticks(rotation=75) 
    plt.legend(loc='lower left')
    plt.grid(True)

    # Mostrar el gráfico
    plt.show()