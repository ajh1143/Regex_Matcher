# def pattern_finder(dataFrame_columns_list):
#     """
#     :param DataFrame_Columns_List: Header Values
#     :return Correct RegEx Pattern for Case
#     """
#     #Extract Case to check pattern in
#     column_case = dataFrame_columns_list[0]
#
#     #Define Possible Patterns
#     pattern_1 = '\\\\+[0-9]+\.+[0-9]+\.+[0-9]+\.+[0-9]{3}\\+'
#     pattern_2 = ''
#     pattern_3 = ''
#     pattern_4 = ''
#
#     #Check if patterns match patterns
#     type_1 = re.findall(pattern_1, column_case)
#     type_2 = re.findall(pattern_2, column_case)
#     type_3 = re.findall(pattern_3, column_case)
#     type_4 = re.findall(pattern_4, column_case)
#
#     #Return pattern_i with true type_i
#     if type_1:
#         return pattern_1
#     elif type_2:
#         return pattern_2
#     elif type_3:
#         return pattern_3
#     elif type_4:
#         return pattern_4
