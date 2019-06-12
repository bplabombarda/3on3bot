HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) \
                            AppleWebKit/537.36 (KHTML, like Gecko) \
                            Chrome/47.0.2526.106 Safari/537.36"
}
STATUSES = {
    "default": "{} at {} tied at {} going into #3on3OT",
    "P": "{} @ {} tied at {} going into #PlayoffOvertime",
    "PR": "{} @ {} tied at {} going into preseason #3on3OT",
    "R": "{} @ {} tied at {} going into #3on3OT",
}
OVERTIME_STATUSES = ['END 3rd', 'OT']
PATTERN = r"\{(?:{[^{}]*}|[^{}])*}"
SOURCE_URL = "http://live.nhle.com/GameData/RegularSeasonScoreboardv3.jsonp"
