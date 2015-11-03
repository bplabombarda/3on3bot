# =====================================================================
# This is the name of the campaign's specific database.
# =====================================================================
campaign_name = 'pledge-tool'

# =====================================================================
# Enter database URI and credentials.
# =====================================================================
db_user = 'emmisdigital'
db_pass ='Digital1313'
db_uri = 'emmisservices.cwh5q682finc.us-east-1.rds.amazonaws.com'

# =====================================================================
# Build the DB URI here for SQLAlchemy.
# =====================================================================
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + db_user + ':' + db_pass + '@' + \
                            db_uri + '/' + campaign_name + '?charset=utf8mb4'

# =====================================================================
# Twitter API Kajigger
# =====================================================================
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
