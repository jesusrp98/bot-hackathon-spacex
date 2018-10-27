import rocket

class Launch:
    def __init__(self, json)
        self.number = json['flight_number']
        self.name = json['mission_number']
        self.launchpadId = json['launch_site']['site_id']
        self.launchpadName = json['launch_site']['site_name']
        self.imageUrl = json['links']['mission_patch_small']
        self.details = json['details']
        self.tentativePrecision = json['tentative_max_precision']
        self.video = json['links']['video_link']
        self.launchDate = json['launch_date_local']
        self.staticFireDate = json['static_fire_date_utc']
        self.launchSuccess = json['launch_success']
        self.rocket = Rocket(json['rocket'])