def mengubah_ekstensi_file():
    filenames = ["satu_program.c", "dua_program.cpp", "tiga_program.hpp", 
                "empat_program.cpp", "matematika.c", "bahasa_indonesia.h",
                "fisika.hpp", "ppkn.c"]

    #isilah bagian yang di garis bawahi tersebut untuk membenarkan program sesuai yang diperintah
    newfilenames=[]
    for i in filenames:
        if i.endswith(".c"):
            i = i.replace(".c",".py")
        elif i.endswith(".cpp"):
            i = i.replace(".cpp","py")
        newfilenames.append(i)
            

    #hint 
    # gunakan perulangan untuk mengambil datanya
    # gunakan pengkodisian untuk mencari data yang diinginkan

    print(filenames)
    print(newfilenames)
    
    
mengubah_ekstensi_file()
"""
Output Nya seharusnya seperti ini 
["satu_program.py", "dua_program.py", "tiga_program.hpp", "empat_program.py", 
"matematika.py", "bahasa_indonesia.h","fisika.hpp", "ppkn.py"]
"""

