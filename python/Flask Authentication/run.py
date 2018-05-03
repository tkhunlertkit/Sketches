import uuid
from app import app

app.secret_key = str(uuid.uuid4())
app.debug = False
app.run()
