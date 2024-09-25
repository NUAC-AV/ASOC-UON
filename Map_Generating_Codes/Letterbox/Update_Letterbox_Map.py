from typing import List, Optional
from create_map import CreateMap

class UpdateLetterboxMap:
    def __init__(self, base_places: List[List[str]], gpx_folder: str, output_html: str):
        self.base_places: List[List[str]] = base_places
        self.gpx_folder: str = gpx_folder
        self.output_html: str = output_html
        self.map_creator: Optional[CreateMap] = None

    def create_map(self) -> None:
        """Initialize CreateMap which handles the complete setup of the map."""
        self.map_creator = CreateMap(self.base_places, self.gpx_folder)
        self.map_creator.setup_map()

    def save_map(self) -> None:
        """Save the map to the specified HTML file."""
        if self.map_creator:
            self.map_creator.save_map(self.output_html)
        else:
            raise RuntimeError("Map creator is not initialized. Call create_map() first.")

    def run(self) -> None:
        """Run the map creation and saving process."""
        self.create_map()
        self.save_map()

if __name__ == "__main__":
    base_places = [
        ["Birmingham Gardens", "Shortland", "Jesmond", "North Lambton", "Waratah West", "Waratah", "Georgetown", "Hamilton North"],
        ["Carrington", "Islington", "Maryville", "Mayfield", "Mayfield East", "Mayfield West", "Tighes Hill", "Warabrook", "Wickham"],
        ["Broadmeadow", "Lambton", "New Lambton"],
        ["Elermore Vale", "Wallsend", "Maryland", "Fletcher", "Minmi"],
        ["Barnsley", "Cameron Park", "Edgeworth", "Killingworth", "West Wallsend", "Holmesville"],
        ["Argenton",  "Cardiff Heights", "Glendale", "New Lambton Heights", "Rankin Park"],
        ["Adamstown", "Adamstown Heights", "Garden Suburb", "Kotara", "Kotara South"],
        ["Bar Beach", "Hamilton", "Hamilton South", "Merewether", "Merewether Heights", "The Junction"],
        # ["Cooks Hill", "Newcastle", "Newcastle East", "Newcastle West", "The Hill"],
        # ["Stockton", "Fern Bay"],
        # ["Boolaroo", "Cardiff", "Hillsborough", "Lakelands", "Macquarie Hills", "Speers Point"],
        # ["Charlestown", "Dudley", "Kahibah", "Highlands", "Whitebridge"]
    ]
    gpx_folder = "GPX_Files/Letterbox_Routes/Sep15-21"
    output_html = "Maps/Letterbox/main.html"
    
    app = UpdateLetterboxMap(base_places, gpx_folder, output_html)
    app.run()
