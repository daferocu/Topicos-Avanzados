import pandas as pd
from sklearn.metrics import accuracy_score, recall_score, f1_score, matthews_corrcoef
from prettytable import PrettyTable


def print_metrics(origin_test, pred_test):
    """
    Prints classification metrics.

    Args:
        origin_test: The true labels.
        pred_test: The predicted labels.
    """

    metrics = {
        'Accuracy': accuracy_score(origin_test, pred_test),
        'Recall': recall_score(origin_test, pred_test, average='macro'),
        'F1-score': f1_score(origin_test, pred_test, average='macro'),
        'Phi coefficient': matthews_corrcoef(origin_test, pred_test)
    }

    print('')
    print('The results of the adjustment metrics:')
    print('')
    
    for metric, value in metrics.items():
        print(f"      {metric}: {value:.3f}")

    return metrics


def comparar_tamaños_vocabularios(*tamaños):
    """
    Compara los tamaños de múltiples vocabularios y devuelve un DataFrame.

    Args:
        *tamaños: Tamaños de los vocabularios.

    Returns:
        DataFrame con los tamaños comparados.
    """

    data = {'Diccionario': [f'Diccionario {i+1}' for i in range(len(tamaños))],
            'Tamaño': tamaños}
    df = pd.DataFrame(data)

    table = PrettyTable()
    table.field_names = df.columns.tolist()
    for index, row in df.iterrows():
        table.add_row(row.values.tolist())

    return table


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
        df[f'Modelo_{i+1}'] = round(df[f'Modelo_{i+1}'], 3)
        df.index.name = index_name
        dfs.append(df)

    df_comparacion = pd.concat(dfs, axis=1)
    df_comparacion = df_comparacion.T
    df_comparacion.index = df_comparacion.index.str.replace('_', ' ')

    table = PrettyTable()
    table.field_names = df_comparacion.columns.tolist()
    for index, row in df_comparacion.iterrows():
        table.add_row(row.values.tolist())

    styled_df = df_comparacion.style.apply(highlight_min_max)
    return styled_df
