import polars as pl
from pathlib import Path
from collections import defaultdict
from typing import Sequence, Dict, List

def sort_tank_images(path_list:Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        if model == "T-62 Obr 1967":
            model = "T-62 Obr. 1967"
        assert model in ref_models, model
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_afv_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        if model == "GAZ-3344-20 Aleut articulated tracked carrier":
            model = "GAZ-3344-20 'Aleut' articulated tracked carrier"
        if model == "Unknown BTR-D BMD-2":
            model = "Unknown BTR-D/BMD-2"
        assert model in ref_models, model
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_ifv_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        if model == "BMP-1 P":
            model = "BMP-1(P)"
        if model == "BMP-2 K":
            model = "BMP-2(K)"
        if model == "BTR-82A M":
            model = "BTR-82A(M)"
        if model == "Unknown BMP-1 2":
            model = "Unknown BMP-1/2"
        assert model in ref_models, model
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_apc_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        if model == "Unknown BTR-80 BTR-82A":
            model = "Unknown BTR-80/BTR-82A"
        if model == "BTR-MDM Rakushka":
            model = "BTR-MDM 'Rakushka'"
        assert model in ref_models, model
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_mrap_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_imv_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_c2_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        if model == "9S470M1 or variant thereof command post for Buk-M1 2":
            model = "9S470M1 (or variant thereof) command post (for Buk-M1/2)"
        if model == "9S932-2 intelligence control and command vehicle for Barnaul-T":
            model = "9S932-2 intelligence, control and command vehicle (for Barnaul-T)"
        if model == "Auriga-1 2V portable satellite communications station":
            model = "Auriga-1.2V portable satellite communications station"
        if model == "Barnaul-T 9 932-1 automated system for air defence units":
            model = "Barnaul-T 9С932-1 automated system for air defence units"
        if model == "MSh-5350 1 command vehicle":
            model = "MSh-5350.1 command vehicle"
        if model == "P-260-U signals vehicle for Redut-2US signal and communications system":
            model = "P-260-U signals vehicle (for Redut-2US signal and communications system)"
        if model == "R-166-0 5 signals vehicle":
            model = "R-166-0.5 signals vehicle"
        if model == "R-381T2M 1 5-3000 MHz radio monitoring station from a modernised R-381TM Taran-M automatic signals intelligence complex":
            model = "R-381T2M 1.5-3000 MHz radio monitoring station from a modernised R-381TM Taran-M automatic signals intelligence complex"
        if model == "Orlan-10":
            model = "Orlan-10 UAV control station"
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_engineer_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        if model == "BREM-Ch BREM-4 armoured recovery vehicle":
            model = "BREM-Ch ''BREM-4'' armoured recovery vehicle"
        if model == "IMR-2 M combat engineering vehicle":
            model = "IMR-2(M) combat engineering vehicle"
        if model == "MTP-A2 1 recovery vehicle":
            model = "MTP-A2.1 recovery vehicle"
        if model == "PTS-2 tracked amphibious transport":
            model = "PTS-2  tracked amphibious transport"
        if model == "UR-77 Meteorit mine clearing vehicle":
            model = "UR-77 'Meteorit'  mine clearing vehicle"
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_spat_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_arty_support_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        if model == "1V13 M battery fire control center":
            model = "1V13(M) battery fire control center"
        if model == "1V18 Klyon-1 artillery command and forward observer vehicle":
            model = "1V18 'Klyon-1' artillery command and forward observer vehicle"
        if model == "9T452 transporter-loader for BM-27 Uragan MRL":
            model = "9T452 transporter-loader (for BM-27 'Uragan' MRL)"
        if model == "TZM-T reloader vehicle for TOS-1A":
            model = "TZM-T reloader vehicle (for TOS-1A)"
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_towed_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_spa_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        if model == "152mm 2S3 M Akatsiya":
            model = "152mm 2S3(M) Akatsiya"
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_mrl_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_aa_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_spaag_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_sam_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        if model == "9A310M1-2 TELAR for Buk-M1-2":
            model = "9A310M1-2 TELAR (for Buk-M1-2)"
        if model == "9A316 TEL for Buk-M2":
            model = "9A316 TEL (for Buk-M2)"
        if model == "9A317 TELAR for Buk-M2":
            model = "9A317 TELAR (for Buk-M2)"
        if model == "9A330 Tor TLAR for 9K330 Tor":
            model = "9A330 Tor TLAR (for 9K330 Tor)"
        if model == "9A331M TLAR for 9K332 Tor-M2":
            model = "9A331M TLAR (for 9K332 Tor-M2)"
        if model == "9A331 TLAR for 9K331 Tor-M1":
            model = "9A331 TLAR (for 9K331 Tor-M1)"
        if model == "9A39M1-2 TEL for Buk-M1-2":
            model = "9A39M1-2 TEL (for Buk-M1-2)"
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_radars_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        if model == "1L261 for 1L260 Zoopark-1M counter-battery radar complex":
            model = "1L261 (for 1L260 Zoopark-1M counter-battery radar complex)"
        if model == "9S18 1 -2 for Buk-M2":
            model = "9S18М1(-2) (for Buk-M2)"
        if model == "9S18 1 -3 for Buk-M3":
            model = "9S18М1(-3) (for Buk-M3)"
        if model == "9S36 for Buk-M2":
            model = "9S36 (for Buk-M2)"
        if model == "PPRU-1 M 9S80 -1 Sborka for 9K35 Strela-10":
            model = "PPRU-1(M) '9S80(-1)' 'Sborka' (for 9K35 Strela-10)"
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_ew_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        if model == "1RL257 Krasukha-4 command post":
            model = "1RL257 Krasukha-4 (command post)"
        if model == "Torn -MDM":
            model = "Torn(-MDM)"
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_fixed_wing_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        if model == "Su-24M MR strike tactical reconnaissance aircraft":
            model = "Su-24M/MR strike/tactical reconnaissance aircraft"
        if model == "Unknown Su-30 Su-34 Su-35":
            model = "Unknown Su-30/Su-34/Su-35"
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_rotary_wing_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        if model == "Ka-52 Alligator attack helicopter":
            model = "Ka-52 'Alligator' attack helicopter"
        if model == "Mi-24P 35M attack helicopter":
            model = "Mi-24P attack helicopter"
        if model == "Mi-24V P attack helicopter":
            model = "Mi-24V/P attack helicopter"
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_ucav_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models and model != "Orlan-10":
                break
            model += " " + part
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_ruav_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models and model != "Orlan-10":
                break
            model += " " + part
        if model == "ZALA 421-16 2":
            model = "ZALA 421-16Е2"
        if model == "Orlan-20 Kartograf":
            model = "'Orlan-20' ''Kartograf''"
        if model == "Orlan-10 Moskit jamming UAV":
            model = "Orlan-10 'Moskit' jamming UAV"
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_ship_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        if model == "Project 1164 Slava-class guided missile cruiser Moskva": # RUSSIAN WARSHIP GO FUCK YOURSELF
            model = "Project 1164 Slava-class guided missile cruiser 'Moskva'"
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_trucks_images(path_list: Sequence[Path], ref_models: List[str]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        for part in split[1:-1]:
            if model in ref_models:
                break
            model += " " + part
        if model == "9T217 transloader for 9K33 Osa":
            model = "9T217 transloader (for 9K33 Osa)"
        if model == "9T244 transloader for 9A330 1 Tor":
            model = "9T244 transloader (for 9A330/1 Tor)"
        if model == "KamAZ-395800 Gorets":
            model = "KamAZ-395800 'Gorets'"
        if model == "UAZ-394511 Esaul":
            model = "UAZ-394511 ‘Esaul’"
        if model == "UAZ-515195 Esaul":
            model = "UAZ-515195 'Esaul'"
        if model == "Unknown truck":
            model = "(Unknown) truck"
        if model == "Unknown vehicle":
            model = "(Unknown) vehicle"
        index[model].append(Path('/',*p.parts[-3:]))
    return index

def sort_images(df, path: Path) -> Dict[str, Dict[str, List[Path]]]:
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
    img_index = {}
    img_index["Tank"] = sort_tank_images((path/"Tanks").rglob("*.*"), tank_models)
    img_index["IMV"] = sort_imv_images((path/"Infantry_Mobility_Vehicles").rglob("*.*"), imv_models)
    img_index["AFV"] = sort_afv_images((path/"Armoured_Fighting_Vehicles").rglob("*.*"), afv_models)
    img_index["IFV"] = sort_ifv_images((path/"Infantry_Fighting_Vehicles").rglob("*.*"), ifv_models)
    img_index["APC"] = sort_apc_images((path/"Armoured_Personnel_Carriers").rglob("*.*"), apc_models)
    img_index["MRAP"] = sort_mrap_images((path/"Mine-Resistant_Ambush_Protected").rglob("*.*"), mrap_models)
    img_index["C2"] = sort_c2_images((path/"Command_Posts_And_Communications_Stations").rglob("*.*"), c2_models)
    img_index["Engineering"] = sort_engineer_images((path/"Engineering_Vehicles_And_Equipment").rglob("*.*"), engineer_models)
    img_index["SPATMS"] = sort_spat_images((path/"Self-Propelled_Anti-Tank_Missile_Systems").rglob("*.*"), spat_models)
    img_index["Artillery Support"] = sort_arty_support_images((path/"Artillery_Support_Vehicles_And_Equipment").rglob("*.*"), arty_supp_models)
    img_index["Towed Artillery"] = sort_towed_images((path/"Towed_Artillery").rglob("*.*"), towed_models)
    img_index["SPA"] = sort_spa_images((path/"Self-Propelled_Artillery").rglob("*.*"), spa_models)
    img_index["MRL"] = sort_mrl_images((path/"Multiple_Rocket_Launchers").rglob("*.*"), mrl_models)
    img_index["AA"] = sort_aa_images((path/"Anti-Aircraft_Guns").rglob("*.*"), aa_models)
    img_index["SPAAG"] = sort_spaag_images((path/"Self-Propelled_Anti-Aircraft_Guns").rglob("*.*"), spaag_models)
    img_index["SAM"] = sort_sam_images((path/"Surface-To-Air_Missile_Systems").rglob("*.*"), sam_models)
    img_index["Radar"] = sort_radars_images((path/"Radars").rglob("*.*"), radar_models)
    img_index["EW"] = sort_ew_images((path/"Jammers_And_Deception_Systems").rglob("*.*"), ew_models)
    img_index["Fixed Wing"] = sort_fixed_wing_images((path/"Aircraft").rglob("*.*"), fixed_wing_models)
    img_index["Rotary Wing"] = sort_rotary_wing_images((path/"Helicopters").rglob("*.*"), rotary_wing_models)
    img_index["UCAV"] = sort_ucav_images((path/"Unmanned_Combat_Aerial_Vehicles").rglob("*.*"), ucav_models)
    img_index["RUAV"] = sort_ruav_images((path/"Reconnaissance_Unmanned_Aerial_Vehicles").rglob("*.*"), ruav_models)
    img_index["Ship"] = sort_ship_images((path/"Naval_Ships").rglob("*.*"), ship_models)
    img_index["Trucks&co"] = sort_trucks_images((path/"Trucks,_Vehicles_and_Jeeps").rglob("*.*"), truck_models)
    return img_index
