readme_file = "README.md"

readme_text_list = []
readme_text_list.append("# Vector plots of Earth's gravity\n")

cmaps = ["viridis", "inferno", "plasma", "cividis"]
for cmap in cmaps:
    tags = (f"""## {cmap.title()}\n"""
            "\n"
            f"""<img src="earth_gravity_{cmap}.svg"\n"""
            f"""  alt="Earth Gravity {cmap.title()}" width=24%>\n"""
            f"""<img src="divergence_of_earth_gravity_{cmap}.svg"\n"""
            f"""  alt="Divergence of Earth Gravity {cmap.title()}" width=24%>\n"""
            f"""<img src="earth_orbit_velocity_{cmap}.svg"\n"""
            f"""  alt="Earth Orbital Velocity {cmap.title()}" width=24%>\n"""
            f"""<img src="curl_of_earth_orbit_velocity_{cmap}.svg"\n"""
            f"""  alt="Curl of Earth Orbital Velocity {cmap.title()}" width=24%>\n""")
    
    readme_text_list.append(tags)

readme_text = "\n".join(readme_text_list)

with open(readme_file, "w") as file:
    file.write(readme_text)
    