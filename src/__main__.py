import menu_management 

if __name__ == "__main__": # Eğer ana dosya ise çalışıyor, modül ise çalışmıyor.
    menu_management.main_menu()
else:
    print("This Application Doesn't Use As Module!")