readme_file = "README.md"

readme_text_list = []
readme_text_list.append("# Slope Fields\n")

cmaps = ["viridis", "inferno", "plasma", "cividis"]
plots = [
    ("constant", "Constant Slope"),
    ("parabola", "Slope Equals x"),
    ("exp_x", "Slope Equals y"),
    ("sin_x", "Slope Equals Cosine of x"),
    ("cos_x", "Slope Equals Negative Sine of x"),
    ("log_x", "Slope Equals Exp of Negative y"),
    ("sinc_x", "Slope Equals the Derivative of Sinc of x"),
    ("sinc_x_2", "Slope Equals Cosine of Pi Times x Minus y All Divided by x"),
    ("circle", "Slope Equals Negative x over y"),
    ("hyperbola", "Slope Equals x over y"),
    ("one_over_x", "Slope Equals Negative y over x"),
    ("one_over_x_squared", "Slope Equals Negative Two y over x"),
    ("gaussian", "Slope Equals Negative Two x y"),
    ("line", "Slope Equals y over x"),
    ("slope_arctan2", "Slope Equals Arctan2 of y, x"),
    ("slope_arctan_y", "Slope Equals the Arctangent of y"),
]

for cmap in cmaps:
    readme_text_list.append(f"## {cmap.title()}\n")
    number_of_tags = 0
    for plot in plots:
        tag = (
            f"""<img src="svg/{plot[0]}_slope_field_{cmap}.svg"\n"""
            f"""  alt="{plot[1]} {cmap.title()}" width=24%>"""
        )
        readme_text_list.append(tag)
        
        number_of_tags += 1
        number_of_tags %= 4
        if not number_of_tags:
            readme_text_list.append("")

readme_text = "\n".join(readme_text_list)

with open(readme_file, "w") as file:
    file.write(readme_text)
