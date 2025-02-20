import requests

while True:
    user_input = input("Enter problem or type 'exit ' to quit: ").strip()
    if user_input.lower() == "exit":
        print("Byeee")
        break

    response = requests.post("http://127.0.0.1:5000/suggest", json={"problem":user_input})

    if response.status_code == 200:
        data = response.json()
        print(f" Suggested Spell: {data["spell"]}\n Description: {data['description']}")
    else:
        print(f"Error: {response.status_code}")