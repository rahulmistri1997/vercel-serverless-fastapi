import re

def parse_value_string(value_string):
    result_values = []
    pattern = r"\[\s*(var|metric)='([^']+)'\s+(var|metric)='([^']+)'\s+labels={([^}]*)}\s+value=([^\s]+)\s*\]"
    matches = re.findall(pattern, value_string)
    print(value_string)
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
    return result_values
