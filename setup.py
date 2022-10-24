import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="The Adventures of Bilbo Swaggins",
    options={"build_exe": {"packages":["pygame", "sys","random"],
                           "include_files":["playerinfo.py","houseinfo.py","gameinfo.py","fireballinfo.py","enemyinfo.py","StartScreen.png","HouseAsset.png", "Fireball.png", "FireWizard.png","Broman.png", "Background.png"]}},
    executables = executables

    )
