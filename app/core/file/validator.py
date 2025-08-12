import pandas as pd

# exemplo
df = pd.DataFrame({"a": ["10", "3.5", "x", None, ""],
                   "b": ["2025-08-04", "2025/08/04", "04/08/2025", None, "2025-12-01"],
                   "c": ["a_is_number", "b_is_valid_date", "c_is_valid_date", "d_is_valid_date", "c_is_valid_date"],
                   "d": ["#123", "@test", "valid", "invalid&", None]})


a_num = pd.to_numeric(df["a"], errors="coerce")  # vira NaN se não for número
df["a_is_number"] = a_num.notna()


b_date = pd.to_datetime(df["b"], format="%Y-%m-%d", errors="coerce")
df["b_is_valid_date"] = b_date.notna()

allowed_c = {"a_is_number", "b_is_valid_date", "c_is_valid_date", "d_is_valid_date"}
df["c_is_valid_value"] = df["c"].isin(allowed_c)

d_has_forbidden = df["d"].str.contains(r"[#@&]", regex=True, na=False)
df["d_is_valid_value"] = ~d_has_forbidden & df["d"].notna() | df["c"].isna()

#add | df["c"].isna() nulos são validos

#Validando se a coluna "b" não é nula
df["b_not_null"] = df["b"].notna()

# Linhas com erro em qualquer regra
invalid = df[
    (~df["a_is_number"]) |
    (~df["b_is_valid_date"]) |
    (~df["c_is_valid_value"]) |
    (~df["d_is_valid_value"]) |
    (~df["b_not_null"])
]

invalid.to_csv("app/data/output/invalid_rows.csv", index=False)