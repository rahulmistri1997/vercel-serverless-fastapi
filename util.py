import re

def parse_value_string(value_string):
    print(value_string)
    result_values = []
    pattern = r"\[\s*(var|metric)='([^']+)'\s+(var|metric)='([^']+)'\s+labels={([^}]*)}\s+value=([^\s]+)\s*\]"
    matches = re.findall(pattern, value_string)

    metric_field_flag = True

    if not matches:
        pattern = r"\[\s*(var|metric)='([^']+)'\s+labels={([^}]*)}\s+value=([^\s]+)\s*\]"
        matches = re.findall(pattern, value_string)
        print("new-matches", matches)
        metric_field_flag = False

    if metric_field_flag:

        for match in matches:
            print(match)
            value = {
                "var": match[1],
                "metric": match[3],
                "labels": {},
                "value": float(match[5])
            }
            if len(match[4]) > 0:
                for label_pair in match[4].split(","):
                    label_parts = label_pair.split("=")
                    if len(label_parts) == 2:
                        value["labels"][label_parts[0].strip()] = label_parts[1].strip()
            result_values.append(value)

    else:
        for match in matches:
            print(match)
            value = {
                "var": match[1],
                "metric": "age_in_seconds",
                "labels": {},
                "value": float(match[3])
            }
            if len(match[2]) > 0:
                for label_pair in match[2].split(","):
                    label_parts = label_pair.split("=")
                    if len(label_parts) == 2:
                        value["labels"][label_parts[0].strip()] = label_parts[1].strip()
            result_values.append(value)
    return result_values
