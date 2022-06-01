readme_file = "README.md"

readme_text_list = []
readme_text_list.append("# Vector plots of Earth's gravity\n")

cmaps = ["viridis", "inferno", "plasma", "cividis"]
plots = [
    ("constant", "Constant Slope"),
    ("parabola", "Slope Equals x"),
    ("exp_x", "Slope Equals y"),
    ("sin_x", "Slope Equals Cosine of x"),
    ("cos_x", "Slope Equals Negative Sine of x"),
    ("log_x", "Slope Equals Exp of Negative y"),
    ("sinc_x", "Slope Equals the Derivative of Sinc of x"),
    ("gaussian", "Slope Equals Negative Two x y"),
    ("line", "Slope Equals y over x"),
    ("slope_arctan2", "Slope Equals Arctan2 of y, x"),
    ("slope_arctan_y", "Slope Equals the Arctangent of y"),
]

for cmap in cmaps:
    readme_text_list.append(f"## {cmap.title()}\n")
    for plot in plots:
        tag = (
            f"""<img src="svg/{plot[0]}_slope_field_{cmap}.svg"\n"""
            f"""  alt="{plot[1]} {cmap.title()}" width=80%>\n"""
        )

        readme_text_list.append(tag)

readme_text = "\n".join(readme_text_list)

with open(readme_file, "w") as file:
    file.write(readme_text)
