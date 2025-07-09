import  pandas as pd

def generate_pivot_table(dataframe, report_config):
    index_column = report_config['group_by']
    value_column = report_config['aggregate_column']
    aggregate_function = report_config['aggregate']
    sheet_name = report_config['sheet_name']
    summary = pd.pivot_table(dataframe,
                             index=index_column,
                             values=value_column,
                             aggfunc=aggregate_function).reset_index()
    if report_config.get('rename_aggregate_column'):
        summary.rename(columns={value_column: report_config.get('rename_aggregate_column')}, inplace=True)
    if report_config.get('rename_group_by_column'):
        summary.index.name = report_config.get('rename_group_by_column')


    return summary
