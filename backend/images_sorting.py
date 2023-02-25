import polars as pl
from pathlib import Path
from PIL import Image
from collections import Counter, defaultdict
from typing import Sequence
import re
from hierarchical import parent_index, path_to_root

path = Path(r"/mnt/z/DATASETS/ukraine/russia/russia/")

def sort_tank_images(path_list:Sequence[Path]):
    tank_img_index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_") if r]
        model = split[0]
        if model=="Unknown":
            model = "Unknown tank"
        tank_img_index[model].append(p)
    return tank_img_index

def test_sort_tank_images(path: Path):
    index = sort_tank_images(path.rglob("*.*"))
    for model in index.keys():
        assert "Tanks" in path_to_root(model)
    assert sum(len(v) for v in index.values()) == sum(1 for _ in path.rglob("*.*"))
    return True



def sort_afv_images(path_list: Sequence[Path]):
    afv_index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
                break
            model += " " + part
        if model == "GAZ-3344-20 Aleut articulated tracked carrier":
            model = "GAZ-3344-20 'Aleut' articulated tracked carrier"
        if model == "Unknown BTR-D BMD-2":
            model = "Unknown BTR-D/BMD-2"
        afv_index[model].append(p)
    return afv_index

def test_sort_afv_images(path: Path):
    index = sort_afv_images(path.rglob("*.*"))
    for model in index.keys():
        assert "AFV" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True



def sort_ifv_images(path_list: Sequence[Path]):
    ifv_index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
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
        ifv_index[model].append(p)
    return ifv_index

def test_sort_ifv_images(path: Path):
    index = sort_ifv_images(path.rglob("*.*"))
    for model in index.keys():
        assert "IFV" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True



def sort_apc_images(path_list: Sequence[Path]):
    apc_index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
                break
            model += " " + part
        if model == "Unknown BTR-80 BTR-82A":
            model = "Unknown BTR-80/BTR-82A"
        if model == "BTR-MDM Rakushka":
            model = "BTR-MDM 'Rakushka'"
        apc_index[model].append(p)
    return apc_index

def test_sort_apc_images(path: Path):
    index = sort_apc_images(path.rglob("*.*"))
    for model in index.keys():
        assert "APC" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True


def sort_mrap_images(path_list: Sequence[Path]):
    mrap_index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
                break
            model += " " + part
        mrap_index[model].append(p)
    return mrap_index

def test_sort_mrap_images(path: Path):
    index = sort_mrap_images(path.rglob("*.*"))
    for model in index.keys():
        assert "MRAP" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True



def sort_c2_images(path_list: Sequence[Path]):
    c2_index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
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
        c2_index[model].append(p)
    return c2_index

def test_sort_c2_images(path: Path):
    index = sort_c2_images(path.rglob("*.*"))
    for model in index.keys():
        assert "C2" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True


def sort_engineer_images(path_list: Sequence[Path]):
    engineer_index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index and model != "Ural-4320":
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
        engineer_index[model].append(p)
    return engineer_index

def test_sort_engineer_images(path: Path):
    index = sort_engineer_images(path.rglob("*.*"))
    for model in index.keys():
        assert "Engineering" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True


def sort_spat_images(path_list: Sequence[Path]):
    spat_index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
                break
            model += " " + part
        spat_index[model].append(p)
    return spat_index

def test_sort_spat_images(path: Path):
    index = sort_spat_images(path.rglob("*.*"))
    for model in index.keys():
        assert "SPATMS" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True




def sort_arty_support_images(path_list: Sequence[Path]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
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
        index[model].append(p)
    return index

def test_sort_arty_support_images(path: Path):
    index = sort_arty_support_images(path.rglob("*.*"))
    for model in index.keys():
        assert "Artillery Support" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True



def sort_towed_images(path_list: Sequence[Path]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
                break
            model += " " + part
        index[model].append(p)
    return index

def test_sort_towed_images(path: Path):
    index = sort_towed_images(path.rglob("*.*"))
    for model in index.keys():
        assert "Towed Artillery" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True


def sort_spa_images(path_list: Sequence[Path]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
                break
            model += " " + part
        if model == "152mm 2S3 M Akatsiya":
            model = "152mm 2S3(M) Akatsiya"
        index[model].append(p)
    return index

def test_sort_spa_images(path: Path):
    index = sort_spa_images(path.rglob("*.*"))
    for model in index.keys():
        assert "SPA" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True


def sort_mrl_images(path_list: Sequence[Path]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
                break
            model += " " + part
        index[model].append(p)
    return index

def test_sort_mrl_images(path: Path):
    index = sort_mrl_images(path.rglob("*.*"))
    for model in index.keys():
        assert "MRL" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True



def sort_aa_images(path_list: Sequence[Path]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
                break
            model += " " + part
        index[model].append(p)
    return index

def test_sort_aa_images(path: Path):
    index = sort_aa_images(path.rglob("*.*"))
    for model in index.keys():
        assert "AA" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True


def sort_spaag_images(path_list: Sequence[Path]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
                break
            model += " " + part
        index[model].append(p)
    return index

def test_sort_spaag_images(path: Path):
    index = sort_spaag_images(path.rglob("*.*"))
    for model in index.keys():
        assert "SPAAG" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True


def sort_sam_images(path_list: Sequence[Path]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
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
        index[model].append(p)
    return index

def test_sort_sam_images(path: Path):
    index = sort_sam_images(path.rglob("*.*"))
    for model in index.keys():
        assert "SAM" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True



def sort_radars_images(path_list: Sequence[Path]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
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
        index[model].append(p)
    return index

def test_sort_radars_images(path: Path):
    index = sort_radars_images(path.rglob("*.*"))
    for model in index.keys():
        assert "Radar" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True



def sort_ew_images(path_list: Sequence[Path]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
                break
            model += " " + part
        if model == "1RL257 Krasukha-4 command post":
            model = "1RL257 Krasukha-4 (command post)"
        if model == "Torn -MDM":
            model = "Torn(-MDM)"
        index[model].append(p)
    return index

def test_sort_ew_images(path: Path):
    index = sort_ew_images(path.rglob("*.*"))
    for model in index.keys():
        assert "EW" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True


def sort_fixed_images(path_list: Sequence[Path]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
                break
            model += " " + part
        if model == "Su-24M MR strike tactical reconnaissance aircraft":
            model = "Su-24M/MR strike/tactical reconnaissance aircraft"
        if model == "Unknown Su-30 Su-34 Su-35":
            model = "Unknown Su-30/Su-34/Su-35"
        index[model].append(p)
    return index

def test_sort_fixed_images(path: Path):
    index = sort_fixed_images(path.rglob("*.*"))
    for model in index.keys():
        assert "Fixed Wing" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True



def sort_rotary_images(path_list: Sequence[Path]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
                break
            model += " " + part
        if model == "Ka-52 Alligator attack helicopter":
            model = "Ka-52 'Alligator' attack helicopter"
        if model == "Mi-24P 35M attack helicopter":
            model = "Mi-24P attack helicopter"
        if model == "Mi-24V P attack helicopter":
            model = "Mi-24V/P attack helicopter"
        index[model].append(p)
    return index

def test_sort_rotary_images(path: Path):
    index = sort_rotary_images(path.rglob("*.*"))
    for model in index.keys():
        assert "Rotary Wing" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True


def sort_ucav_images(path_list: Sequence[Path]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
                break
            model += " " + part
        index[model].append(p)
    return index

def test_sort_ucav_images(path: Path):
    index = sort_ucav_images(path.rglob("*.*"))
    for model in index.keys():
        assert "UCAV" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True


def sort_ruav_images(path_list: Sequence[Path]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
                break
            model += " " + part
        if model == "ZALA 421-16 2":
            model = "ZALA 421-16Е2"
        if model == "Orlan-20 Kartograf":
            model = "'Orlan-20' ''Kartograf''"
        index[model].append(p)
    return index

def test_sort_ruav_images(path: Path):
    index = sort_ruav_images(path.rglob("*.*"))
    for model in index.keys():
        assert "RUAV" in path_to_root(model), (model, path_to_root(model))
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True


def sort_ship_images(path_list: Sequence[Path]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
                break
            model += " " + part
        if model == "Project 1164 Slava-class guided missile cruiser Moskva": # RUSSIAN WARSHIP GO FUCK YOURSELF
            model = "Project 1164 Slava-class guided missile cruiser 'Moskva'"
        index[model].append(p)
    return index

def test_sort_ship_images(path: Path):
    index = sort_ship_images(path.rglob("*.*"))
    for model in index.keys():
        assert "Ship" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True


def sort_trucks_images(path_list: Sequence[Path]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
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
        index[model].append(p)
    return index

def test_sort_trucks_images(path: Path):
    index = sort_trucks_images(path.rglob("*.*"))
    for model in index.keys():
        assert "Trucks&co" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True


def sort_imv_images(path_list: Sequence[Path]):
    index = defaultdict(list)
    for p in path_list:
        split = [r for r in p.stem.split("_")[:-1] if r]
        model = split[0]
        for part in split[1:]:
            if model in parent_index:
                break
            model += " " + part
        index[model].append(p)
    return index

def test_sort_imv_images(path: Path):
    index = sort_imv_images(path.rglob("*.*"))
    for model in index.keys():
        assert "IMV" in path_to_root(model)
    n_index = sum(len(v) for v in index.values())
    n_imgs = sum(1 for _ in path.rglob("*.*"))
    assert n_index == n_imgs, (n_index, n_imgs)
    return True

test_sort_ruav_images(path/"Reconnaissance_Unmanned_Aerial_Vehicles")
test_sort_ship_images(path/"Naval_Ships")
test_sort_trucks_images(path/"Trucks,_Vehicles_and_Jeeps")
test_sort_imv_images(path/"Infantry_Mobility_Vehicles")
test_sort_ucav_images(path/"UCAV")
test_sort_rotary_images(path/"Helicopters")
test_sort_fixed_images(path/"Aircraft")
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
