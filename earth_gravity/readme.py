readme_file = "README.md"

readme_text_list = []
readme_text_list.append("# Vector plots of Earth's gravity\n")

cmaps = ["viridis", "inferno", "plasma", "cividis"]
plots = [
    ("earth_gravity", "Earth Gravity"),
    ("earth_gravity_dynamic", "Earth Gravity Dynamic"),
    ("divergence_of_earth_gravity", "Divergence of Earth Gravity"),
    ("earth_orbit_velocity", "Earth Orbital Velocity"),
    ("earth_orbit_velocity_dynamic", "Earth Orbital Velocity Dynamic"),
    ("curl_of_earth_orbit_velocity", "Curl of Earth Orbital Velocity"),
    ("curl_of_earth_orbit_velocity_dynamic", "Curl of Earth Orbital Velocity Dynamic"),
]

for cmap in cmaps:
    readme_text_list.append(f"## {cmap.title()}\n")
    for plot in plots:
        tags = (
            f"""<img src="svg/{plot[0]}_{cmap}.svg"\n"""
            f"""  alt="{plot[1]} {cmap.title()}" width=80%>\n"""
        )

        readme_text_list.append(tags)

readme_text = "\n".join(readme_text_list)

with open(readme_file, "w") as file:
    file.write(readme_text)
