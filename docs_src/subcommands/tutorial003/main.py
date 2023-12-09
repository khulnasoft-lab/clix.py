import clix

import items
import lands
import users

app = clix.Clix()
app.add_clix(users.app, name="users")
app.add_clix(items.app, name="items")
app.add_clix(lands.app, name="lands")

if __name__ == "__main__":
    app()
