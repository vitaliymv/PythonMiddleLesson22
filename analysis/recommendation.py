def generate_recommendation(cluster_label, score):
    if cluster_label == "High":
        if score < 8:
            return "Maintain hours, focus on efficiency to improve score"
        else:
            return "Excellent! Try advanced projects & leadership tasks"
    elif cluster_label == "Medium":
        if score < 6:
            return "Increase study hours and focus on fundamentals"
        else:
            return "Good, focus on efficiency and advanced projects"
    else:
        return "Increase study hours and practice basics"
