def main():
    grocery = {}
    while True:
        try:
            item = input("").strip().lower()
            if item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1  
        except item == "done":
            break
    sorted_grocery = sorted(grocery.items())
    for key,value in sorted_grocery.items():
        print(sorted(f"{value}{key}")).upper()
    

main()