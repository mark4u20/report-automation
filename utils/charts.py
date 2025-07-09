import pandas as pd

def create_chart(output_file_name, result_array):

    with pd.ExcelWriter(output_file_name, engine='xlsxwriter') as writer:
        for dict_val in result_array:
            dataframe = dict_val['dataframe']
            report_config = dict_val['report_config']
            sheet_name = report_config['sheet_name']
            dataframe.to_excel(writer, index=False, sheet_name=sheet_name)
            data_start_col = report_config.get('data_col_start')
            data_end_col = report_config.get('data_col_end')
            data_start_row = report_config.get('data_row_start')
            data_end_row = report_config.get('data_row_end') or len(dataframe)
            category_start_col = report_config.get('category_col_start')
            category_end_col = report_config.get('category_col_end')
            category_start_row = report_config.get('category_row_start')
            category_end_row = report_config.get('category_row_end') or len(dataframe)
            chart_anchor = report_config.get('chart_anchor') or 'F2'
            chart_type = report_config.get('chart_type')
            x_axis_title = report_config.get('x_axis_title')
            y_axis_title = report_config.get('y_axis_title')
            chart_title = report_config.get('chart_title')
            series_name = report_config.get('series_name')
            sub_type = report_config.get('sub_type')
            chart_width = report_config.get('chart_width') or 800
            chart_height = report_config.get('chart_height') or 400

            # Get workbook and worksheet objects
            workbook = writer.book
            worksheet = writer.sheets[sheet_name]

            # Format
            worksheet.set_column('A:B', 15)  # set column width
            # Step 3: Create chart
            chart = workbook.add_chart({'type': chart_type,
                                        'subtype': sub_type})
            chart.add_series({
                'name': series_name,
                # sheet name, row start, col start, row end, col end
                'categories': [sheet_name, category_start_row, category_start_col, category_end_row, category_end_col],
                'values': [sheet_name, data_start_row, data_start_col, data_end_row, data_end_col],
                'data_labels': {'value': True}
            })

            chart.set_size({
                'width': chart_width,
                'height': chart_height
            })
            chart.set_title({'name': chart_title})

            chart.set_x_axis({
                'name': x_axis_title,
                'major_gridlines': {'visible': False},  # to remove gridlines
                'data_labels': {'value': True}
            })
            chart.set_y_axis({
                'name': y_axis_title,
                'major_gridlines': {'visible': False},  # to remove gridlines
                'data_labels': {'value': True}
            })
            chart.set_style(10)

            # Insert chart
            worksheet.insert_chart(chart_anchor, chart)
