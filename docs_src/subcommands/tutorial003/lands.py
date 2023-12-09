import clix

import reigns
import towns

app = clix.Clix()
app.add_clix(reigns.app, name="reigns")
app.add_clix(towns.app, name="towns")

if __name__ == "__main__":
    app()
