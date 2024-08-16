from create_map import CreateMap

class UpdateLetterboxMap:
    def __init__(self, base_places, gpx_folder, output_html):
        self.base_places = base_places
        self.gpx_folder = gpx_folder
        self.output_html = output_html
        self.map_creator = None

    def create_map(self):
        # Initialize CreateMap which handles the complete setup of the map
        self.map_creator = CreateMap(self.base_places, self.gpx_folder)
        self.map_creator.setup_map()

    def save_map(self):
        self.map_creator.save_map(self.output_html)

    def run(self):
        self.create_map()
        self.save_map()


if __name__ == "__main__":
    base_places = [
        # ["Birmingham Gardens", "Shortland", "Jesmond", "North Lambton", "Waratah West", "Waratah", "Georgetown", "Hamilton North"],
        # ["Carrington", "Islington", "Maryville", "Mayfield", "Mayfield East", "Mayfield West", "Tighes Hill", "Warabrook", "Wickham"],
        ["Broadmeadow", "Lambton", "New Lambton"],
        ["Elermore Vale", "Wallsend", "Maryland", "Fletcher", "Minmi"],
        # ["Barnsley", "Cameron Park", "Edgeworth", "Killingworth", "West Wallsend", "Holmesville"],
        # ["Argenton",  "Cardiff Heights", "Glendale", "New Lambton Heights", "Rankin Park"],
        # ["Adamstown", "Adamstown Heights", "Garden Suburb", "Kotara", "Kotara South"],
        # ["Bar Beach", "Hamilton", "Hamilton South", "Merewether", "Merewether Heights", "The Junction"],
        # ["Cooks Hill", "Newcastle", "Newcastle East", "Newcastle West", "The Hill"],
        # ["Stockton", "Fern Bay"],
        # ["Boolaroo", "Cardiff", "Hillsborough", "Lakelands", "Macquarie Hills", "Speers Point"],
        # ["Charlestown", "Dudley", "Kahibah", "Highlands", "Whitebridge"]
    ]
    gpx_folder = "GPX_Files/Empty"
    output_html = "Maps/Letterbox/letterbox_test_21.html"
    
    app = UpdateLetterboxMap(base_places, gpx_folder, output_html)
    app.run()
