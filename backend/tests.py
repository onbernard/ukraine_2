from pathlib import Path

import polars as pl

from images_sorting import *
from hierarchical import path_to_root

path = Path(r"/mnt/z/DATASETS/ukraine/russia/russia/")
df = pl.read_csv(r"/mnt/z/DATASETS/ukraine/losses_russia.csv")
tank_models = df.filter(df["equipment"]=="Tanks")["model"].unique().to_list()
afv_models = df.filter(df["equipment"]=="Armoured Fighting Vehicles")["model"].unique().to_list()
ifv_models = df.filter(df["equipment"]=="Infantry Fighting Vehicles")["model"].unique().to_list()
apc_models = df.filter(df["equipment"]=="Armoured Personnel Carriers")["model"].unique().to_list()
mrap_models = df.filter(df["equipment"]=="Mine-Resistant Ambush Protected")["model"].unique().to_list()
imv_models = df.filter(df["equipment"]=="Infantry Mobility Vehicles")["model"].unique().to_list()
c2_models = df.filter(df["equipment"]=="Command Posts And Communications Stations")["model"].unique().to_list()
engineer_models = df.filter(df["equipment"]=="Engineering Vehicles And Equipment")["model"].unique().to_list()
spat_models = df.filter(df["equipment"]=="Self-Propelled Anti-Tank Missile Systems")["model"].unique().to_list()
arty_supp_models = df.filter(df["equipment"]=="Artillery Support Vehicles And Equipment")["model"].unique().to_list()
towed_models = df.filter(df["equipment"]=="Towed Artillery")["model"].unique().to_list()
spa_models = df.filter(df["equipment"]=="Self-Propelled Artillery")["model"].unique().to_list()
mrl_models = df.filter(df["equipment"]=="Multiple Rocket Launchers")["model"].unique().to_list()
aa_models = df.filter(df["equipment"]=="Anti-Aircraft Guns")["model"].unique().to_list()
spaag_models = df.filter(df["equipment"]=="Self-Propelled Anti-Aircraft Guns")["model"].unique().to_list()
sam_models = df.filter(df["equipment"]=="Surface-To-Air Missile Systems")["model"].unique().to_list()
radar_models = df.filter(df["equipment"]=="Radars")["model"].unique().to_list()
ew_models = df.filter(df["equipment"]=="Jammers And Deception Systems")["model"].unique().to_list()
fixed_wing_models = df.filter(df["equipment"]=="Aircraft")["model"].unique().to_list()
rotary_wing_models = df.filter(df["equipment"]=="Helicopters")["model"].unique().to_list()
ucav_models = df.filter(df["equipment"]=="Unmanned Combat Aerial Vehicles")["model"].unique().to_list()
ruav_models = df.filter(df["equipment"]=="Reconnaissance Unmanned Aerial Vehicles")["model"].unique().to_list()
ship_models = df.filter(df["equipment"]=="Naval Ships")["model"].unique().to_list()
truck_models = df.filter(df["equipment"]=="Trucks, Vehicles and Jeeps")["model"].unique().to_list()

# 0. Tanks
def test_sort_tank_images(path: Path):
    index = sort_tank_images(path.rglob("*.*"), tank_models)
    for model in index.keys():
        assert "Tanks" in path_to_root(model), (model, path_to_root(model))
        assert model in tank_models, model
    assert sum(len(v) for v in index.values()) == sum(1 for _ in path.rglob("*.*"))
    return index

# 1. AFV
def test_sort_afv_images(path: Path):
    index = sort_afv_images(path.rglob("*.*"), afv_models)
    for model in index.keys():
        assert "AFV" in path_to_root(model)
        assert model in afv_models, model
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 2. IFV
def test_sort_ifv_images(path: Path):
    index = sort_ifv_images(path.rglob("*.*"), ifv_models)
    for model in index.keys():
        assert "IFV" in path_to_root(model)
        assert model in ifv_models
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True

# 3. APC
def test_sort_apc_images(path: Path):
    index = sort_apc_images(path.rglob("*.*"), apc_models)
    for model in index.keys():
        assert "APC" in path_to_root(model), (model, path_to_root(model))
        assert model in apc_models
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 4. MRAP
def test_sort_mrap_images(path: Path):
    index = sort_mrap_images(path.rglob("*.*"), mrap_models)
    for model in index.keys():
        assert "MRAP" in path_to_root(model)
        assert model in mrap_models
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 5. IMV
def test_sort_imv_images(path: Path):
    index = sort_imv_images(path.rglob("*.*"), imv_models)
    for model in index.keys():
        assert "IMV" in path_to_root(model)
        assert model in imv_models
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 6. C2
def test_sort_c2_images(path: Path):
    index = sort_c2_images(path.rglob("*.*"), c2_models)
    for model in index.keys():
        assert "C2" in path_to_root(model)
        assert model in c2_models
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 7. Engineering
def test_sort_engineer_images(path: Path):
    index = sort_engineer_images(path.rglob("*.*"), engineer_models)
    for model in index.keys():
        assert "Engineering" in path_to_root(model)
        assert model in engineer_models, model
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 8. SPAT
def test_sort_spat_images(path: Path):
    index = sort_spat_images(path.rglob("*.*"), spat_models)
    for model in index.keys():
        assert "SPATMS" in path_to_root(model), (model, path_to_root(model))
        assert model in spat_models
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 9. Artillery Support
def test_sort_arty_support_images(path: Path):
    index = sort_arty_support_images(path.rglob("*.*"), arty_supp_models)
    for model in index.keys():
        assert "Artillery Support" in path_to_root(model)
        assert model in arty_supp_models
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 10. Towed Artillery
def test_sort_towed_images(path: Path):
    index = sort_towed_images(path.rglob("*.*"), towed_models)
    for model in index.keys():
        assert "Towed Artillery" in path_to_root(model)
        assert model in towed_models, model
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 11. SPA
def test_sort_spa_images(path: Path):
    index = sort_spa_images(path.rglob("*.*"), spa_models)
    for model in index.keys():
        assert "SPA" in path_to_root(model)
        assert model in spa_models, model
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 12. MRL
def test_sort_mrl_images(path: Path):
    index = sort_mrl_images(path.rglob("*.*"), mrl_models)
    for model in index.keys():
        assert "MRL" in path_to_root(model)
        assert model in mrl_models, model
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 13. AA 
def test_sort_aa_images(path: Path):
    index = sort_aa_images(path.rglob("*.*"), aa_models)
    for model in index.keys():
        assert "AA" in path_to_root(model)
        assert model in aa_models, model
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 14. SPAAG
def test_sort_spaag_images(path: Path):
    index = sort_spaag_images(path.rglob("*.*"), spaag_models)
    for model in index.keys():
        assert "SPAAG" in path_to_root(model)
        assert model in spaag_models, model
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 15. SAM
def test_sort_sam_images(path: Path):
    index = sort_sam_images(path.rglob("*.*"), sam_models)
    for model in index.keys():
        assert "SAM" in path_to_root(model)
        assert model in sam_models, model
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 16. Radars
def test_sort_radars_images(path: Path):
    index = sort_radars_images(path.rglob("*.*"), radar_models)
    for model in index.keys():
        assert "Radar" in path_to_root(model)
        assert model in radar_models, model
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 17. EW
def test_sort_ew_images(path: Path):
    index = sort_ew_images(path.rglob("*.*"), ew_models)
    for model in index.keys():
        assert "EW" in path_to_root(model)
        assert model in ew_models, model
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 18. Fixed Wing
def test_sort_fixed_wing_images(path: Path):
    index = sort_fixed_wing_images(path.rglob("*.*"), fixed_wing_models)
    for model in index.keys():
        assert "Fixed Wing" in path_to_root(model)
        assert model in fixed_wing_models, model
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 19. Rotary Wing
def test_sort_rotary_images(path: Path):
    index = sort_rotary_wing_images(path.rglob("*.*"), rotary_wing_models)
    for model in index.keys():
        assert "Rotary Wing" in path_to_root(model)
        assert model in rotary_wing_models, model
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 20. UCAV
def test_sort_ucav_images(path: Path):
    index = sort_ucav_images(path.rglob("*.*"), ucav_models)
    for model in index.keys():
        assert "UCAV" in path_to_root(model)
        assert model in ucav_models, model
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 21. RUAV
def test_sort_ruav_images(path: Path):
    index = sort_ruav_images(path.rglob("*.*"), ruav_models)
    for model in index.keys():
        assert "RUAV" in path_to_root(model), (model, path_to_root(model))
        assert model in ruav_models
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 22. Ships
def test_sort_ship_images(path: Path):
    index = sort_ship_images(path.rglob("*.*"), ship_models)
    for model in index.keys():
        assert "Ship" in path_to_root(model)
        assert model in ship_models, model
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index

# 23. Trucks
def test_sort_trucks_images(path: Path):
    index = sort_trucks_images(path.rglob("*.*"), truck_models)
    for model in index.keys():
        assert "Trucks&co" in path_to_root(model)
        assert model in truck_models
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return index


def test_sort_images(df, path):
    test_sort_ruav_images(path/"Reconnaissance_Unmanned_Aerial_Vehicles")
    test_sort_ship_images(path/"Naval_Ships")
    test_sort_trucks_images(path/"Trucks,_Vehicles_and_Jeeps")
    test_sort_imv_images(path/"Infantry_Mobility_Vehicles")
    test_sort_ucav_images(path/"UCAV")
    test_sort_rotary_images(path/"Helicopters")
    test_sort_fixed_wing_images(path/"Aircraft")
    test_sort_ew_images(path/"Jammers_And_Deception_Systems")
    test_sort_radars_images(path/"Radars")
    test_sort_sam_images(path/"Surface-To-Air_Missile_Systems")
    test_sort_spaag_images(path/"Self-Propelled_Anti-Aircraft_Guns")
    test_sort_apc_images(path/"Armoured_Personnel_Carriers")
    test_sort_spat_images(path/"Self-Propelled_Anti-Tank_Missile_Systems")
    test_sort_engineer_images(path/"Engineering_Vehicles_And_Equipment")
    test_sort_c2_images(path/"Command_Posts_And_Communications_Stations")
    test_sort_mrap_images(path/"Mine-Resistant_Ambush_Protected")
    test_sort_ifv_images(path/"Infantry_Fighting_Vehicles")
    test_sort_afv_images(path/"Armoured_Fighting_Vehicles")
    test_sort_mrl_images(path/"Multiple_Rocket_Launchers")
    test_sort_towed_images(path/"Towed_Artillery")
    test_sort_arty_support_images(path/"Artillery_Support_Vehicles_And_Equipment")
    test_sort_tank_images(path/"Tanks")
    test_sort_spa_images(path/"Self-Propelled_Artillery")
    test_sort_aa_images(path/"Anti-Aircraft_Guns")
    index = sort_images(df, path)
    sub_indexes = list(index.values())
    for i in range(len(sub_indexes)):
        for j in range(i+1, len(sub_indexes)):
            inter = set(sub_indexes[i].keys()).intersection(set(sub_indexes[j].keys()))
            assert not inter
    return True
