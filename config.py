# =====================================================================
# Define the application directory
# =====================================================================
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
campaign_name = ''

# =====================================================================
# Enter database URI and credentials
# =====================================================================
db_user = ""
db_pass =""
db_uri = ""

# =====================================================================
# Build the DB URI here for SQLAlchemy & other options
# =====================================================================
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://" + db_user + ":" + db_pass + \
                            "@" + db_uri + "/" + "?charset=utf8mb4"

DATABASE_CONNECT_OPTIONS = {}

# =====================================================================
# Twitter API Kajigger 🐦
# =====================================================================
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
URL = ""

# =====================================================================
# Twitter Status Kajigger 🐦
# =====================================================================
HASHTAG = "NHL3on3"

# =====================================================================
# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other
# =====================================================================
THREADS_PER_PAGE = 2
