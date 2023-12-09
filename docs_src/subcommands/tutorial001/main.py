import clix

import items
import users

app = clix.Clix()
app.add_clix(users.app, name="users")
app.add_clix(items.app, name="items")

if __name__ == "__main__":
    app()
