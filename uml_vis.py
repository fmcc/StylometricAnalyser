import sadisplay
from database import models

desc = sadisplay.describe([getattr(models, attr) for attr in dir(models)])
open('schema.dot', 'w').write(sadisplay.dot(desc))
