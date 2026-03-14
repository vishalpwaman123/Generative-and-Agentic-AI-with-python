class ChaiUtils:

    def clean_ingredients(data):
        return [item.strip() for item in data.split(",")]

_data = "name1, name2, name3, name4, name5"

cleaned_data = ChaiUtils.clean_ingredients(_data)
print(cleaned_data)