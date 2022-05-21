name=input("İsminizi Giriniz.")
print("Merhaba"+" "+name+" "+"Adam Asmaca oyununa hoşgeldin")
secretWord="Python"
guess_string=""
lives=10

while lives>0:

    chracter_left=0

    for character in secretWord:

        if character in guess_string:
             print(character)
        else:
            print("-")
            chracter_left+=1

    if chracter_left==0:
        print("Kazandınız")
        break
       
    guess=input("Tahmit et:")
    guess_string+=guess

    if guess not in secretWord:
        lives-=1
        print(f"Yanlış tahmin {lives} canın kaldı")

  
        if lives==0:
            print("Oyun bitti")




