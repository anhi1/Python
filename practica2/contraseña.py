# hay otras formas de hacerlo mas corto, segun el stackoverflow
# https://stackoverflow.com/questions/45179130/password-testing-in-python

# esta es mi base de datos ficticia

personas = {
    "persona_1":{
        "email":"annie@gmail.com",
        "password": "abcdefghEEwq@"
    },
    "persona_2":{
        "email":"patty@gmail.com",
        "password":"ijklmnopq"
    },
    "persona_3":{
        "email":"betty@gmail.com",
        "password":"rstuvwxy"
    }
}

def comprobar_password(base_de_datos: dict, persona_id: str) -> bool:
    SpecialSym = "!@#$%^&*()"
    password = personas[persona_id]["password"]
    if len(password) > 10 and any(char in SpecialSym for char in password):
        return True
    return False

print(comprobar_password(personas, "persona_1"))



