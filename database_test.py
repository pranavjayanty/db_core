from database import Database

db = Database()

user_info = db.get_user(discord_id="241085495398891521")
print(user_info)

user_facts = db.get_user_fact(discord_id="241085495398891521", days_back=7)
print(user_facts)

db.set_user_fact(discord_id="241085495398891521", fact_text="Likes the colour White.")

# user_facts = db.get_user_fact(discord_id="241085495398891521", days_back=7)
# print(user_facts)
