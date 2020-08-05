file_name = "auto-csv-to-sql/application_data.csv"

file_data = open(file_name, 'r').readlines()
heading = file_data.pop(0)

col_size_representation = heading.split(",").copy()
varchar_level_exemption_list = []
float_level_exemption_list = []


for line in file_data:
    line_values = line.split(",")
    # print(line_values)

    for index, value in enumerate(line_values):

        if index in varchar_level_exemption_list:
            continue


        if value.isnumeric():

            if index in float_level_exemption_list:
                continue

            # print(index, int(value), "- Integer")
            col_size_representation[index] = "INT"
        
        else:

            try:
                # print(index, float(value), "- Decimal")
                float(value)
                col_size_representation[index] = "FLOAT"
            except:
                # print(index, value, "- Varchar")
                col_size_representation[index] = "VARCHAR"
                varchar_level_exemption_list.append(index)


col_names_list =heading.split(',') 

auto_generated_command = ""

for col_name, col_data_type  in zip(col_names_list, col_size_representation):

    auto_generated_command += f",{col_name} {col_data_type}"

command = f"CREATE TABLE application_data (id INT(3) PRIMARY KEY NOT NULL AUTO_INCREMENT {auto_generated_command});"

print(command)