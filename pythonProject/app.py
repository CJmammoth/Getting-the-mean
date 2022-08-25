from flask import Flask, render_template
app = Flask(__name__)

characters = [{"Name":"Arthurius","Power":"Telepathy","Weapon":"Sword","Description":"Really smart but grades are pretty low, which is surprising because he should be able to read his professor's minds during a test. Maybe he chooses not to. He's also super friendly and kind."},
             {"Name":"Fanstasia","Power":"Telekenesis","Weapon":"Crossbow","Description":"Shy and likes to play with talking raccoons."},
             {"Name":"Obsidian","Power":"Invisibility","Weapon":"Spear","Description":"No one knows for sure who Obsidian really is. This boy just poppped out of nowhere one day. Many people suspect that he's always been around, silently staring at everyone."}]
@app.route('/')
@app.route('/character')
def character():
    return render_template("character.html", characters=characters)

if __name__=="__main__":
    app.run()
