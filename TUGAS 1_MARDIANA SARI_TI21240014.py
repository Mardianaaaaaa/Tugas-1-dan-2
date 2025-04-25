kamus = {
        "tas"   : "yaitu terbuat dari kanvas berkualitas,memberikan kesan kasual dan stylish",
        "sepatu": "yaitu terbuat dari karet yang fleksibel dan tahan lama ",
        "bangku": "adalah kayu jati,dengan menggunakan kayu jati yang berkualitas,bangku tidak hanya estetis tetapi juga sanggat awet dan tahan lama",
        "meja"  : "yaitu terbuat dari kayu gaharu yang elegan dan klasik",
        "kemeja": "yaitu terbuat dari kain katun yang halus dan lembut"
    }

    
kata = input("Masukkan benda yang ingin di cari bahan pembuatannya: ").lower()

    
if kata in kamus:
        print(f"Bahan dari {kata} {kamus[kata]}")
else:
        print(f"Maaf, bahan dari {kata} tidak ditemukan dalam kamus.")

