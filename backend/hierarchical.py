import polars as pl
from pydantic import BaseModel
from typing import List, Optional, Union, Dict
from collections import defaultdict
from pathlib import Path


class Record(BaseModel):
    name: str
    images: List[Path] = []
    losses_total: Optional[int] = None
    children: List["Record"] = []

parent_index = {
    "Armor": "All",
    "Mobility": "All",
    "Support": "All",
    "Artillery": "All",
    "AA": "All",
    "Aircraft": "All"
    ,

    # TANKS
    "T-62 Obr. 1967": "T-62",
    "T-62M": "T-62",
    "T-62MV": "T-62",
    "T-64A": "T-64",
    "T-64BV": "T-64",
    "T-72A": "T-72",
    "T-72AV": "T-72",
    "T-72B": "T-72",
    "T-72B Obr. 1989": "T-72",
    "T-72BA": "T-72",
    "T-72B3": "T-72",
    "T-72B3 Obr. 2014": "T-72",
    "T-72B3 Obr. 2016": "T-72",
    "Unknown T-72": "T-72",
    "T-80BV": "T-80",
    "T-80BVK": "T-80",
    "T-80U": "T-80",
    "T-80UK": "T-80",
    "T-80UE-1": "T-80",
    "T-80UM2": "T-80",
    "T-80BVM": "T-80",
    "T-80BVM Obr. 2022": "T-80",
    "Unknown T-80": "T-80",
    "T-90A": "T-90",
    "T-90S": "T-90",
    "T-90M": "T-90",
    "Unknown tank": "Tanks",

    "T-62": "Tanks",
    "T-64": "Tanks",
    "T-72": "Tanks",
    "T-80": "Tanks",
    "T-90": "Tanks",

    "Tanks": "Armor",

    # AFVs
    "BRM-1 and BRM-1K reconnaissance vehicle": "BRM",
    "BRM-1K Obr. 2021": "BRM",
    "BRDM-2": "BRDM",
    "BRDM-2RKhb chemical reconnaissance vehicle": "BRDM",
    "BRDM-2-based ZS-82 PsyOps vehicle": "BRDM",
    "MT-LB": "MT-LB",
    "MT-LBVM and MT-LBVMK": "Other MT-LB",
    "MT-LB with ZU-23 AA gun": "Other MT-LB",
    "MT-LBu": "Other MT-LB",
    "Vityaz DT-10PM articulated tracked carrier": "ATC",
    "Vityaz DT-30 articulated tracked carrier": "ATC",
    "GAZ-3344-20 'Aleut' articulated tracked carrier": "ATC",
    "2S1 with ZU-23 AA gun": "Other AFV",
    "Unknown BTR-D/BMD-2": "Other AFV",
    "BTR-80-based ZS-88 PsyOps vehicle": "Other AFV",
    "BMM-80 ambulance": "Other AFV",
    "Unknown AFV": "Other AFV",

    "BRM": "AFV",
    "BRDM": "AFV",
    "MT-LB": "AFV",
    "Other MT-LB": "AFV",
    "ATC": "AFV",
    "Other AFV": "AFV",

    "AFV": "Armor",

    # IFVs
    "BMD-2": "BMD",
    "BMD-4M": "BMD",
    "BTR-82A(M)": "Other IFV",
    "BMO-T": "Other IFV",
    "MT-LBM 6MB": "Other IFV",
    "BMP-2 675-sb3KDZ": "BMP",
    "BMP-1AM": "BMP",
    "BMP-1(P)": "BMP",
    "BMP-3": "BMP",
    "BMP-2(K)": "BMP",
    "Unknown BMP-1/2": "BMP",
    "BMP-2M": "BMP",

    "BMD": "IFV",
    "Other IFV": "IFV",
    "BMP": "IFV",

    "IFV": "Armor",

    # APCs
    'BTR-70M': "BTR",
    'Unknown BTR-80/BTR-82A': "BTR",
    'BTR-D': "BTR",
    'BTR-80': "BTR",
    'BTR-60PB': "BTR",
    "BTR-MDM 'Rakushka'": "BTR",
    'BTR-70': "BTR",
    'Ural-4320VV': "Other APC",
    'Remdiesel Z-STS Akhmat': "Other APC",

    "BTR": "APC",
    "Other APC": "APC",

    "APC": "Armor",

    # MRAPs
    'KamAZ-435029 Patrol-A' : "MRAP",
    'KamAZ-63968 Typhoon' : "MRAP",
    'K-53949 Linza' : "MRAP",
    'K-53949 Typhoon-K' : "MRAP",

    "MRAP": "Mobility",

    # IMVs
    "AMN-590951": "IMV",
    "Iveco LMV Rys": "IMV",
    "GAZ Tigr-M": "IMV",
    "BPM-97 Vystrel": "IMV",
    "GAZ Tigr": "IMV",

    "IMV": "Mobility",

    # Command Posts And Communications Stations
    "R-142NSA command and signals vehicle": "C2",
    "R-419L1 communications station": "C2",
    "Unknown communications station based on the KamAZ 6x6": "C2",
    "R-145BM command vehicle": "C2",
    "P-240 digital communications vehicle": "C2",
    "APE-5 command post": "C2",
    "Auriga-1.2V portable satellite communications station": "C2",
    "MP-2IM signals vehicle": "C2",
    "Orlan-10 UAV control station": "C2",
    "BMP-1KSh command and staff vehicle": "C2",
    "MPUS-K mobile command post": "C2",
    "9S470M1 (or variant thereof) command post (for Buk-M1/2)": "C2",
    "Command vehicle for Podlet-K1 low-altitude S-band surveillance radar": "C2",
    "R-149MA3 command and staff vehicle": "C2",
    "R-145BM1 command vehicle": "C2",
    "R-149AKSh-1 command and signals vehicle": "C2",
    "MSh-5350.1 command vehicle": "C2",
    "MP-1IM signals vehicle": "C2",
    "Unknown communications station": "C2",
    "9S932-2 intelligence, control and command vehicle (for Barnaul-T)": "C2",
    "R-431AM antenna module for the Redut-2US communications system": "C2",
    "P-260-U signals vehicle (for Redut-2US signal and communications system)": "C2",
    "R-439-MD2 SatCom Station": "C2",
    "BMD-1KSh-A command vehicle": "C2",
    "BTR-60PU-12command vehicle": "C2",
    "R-145BMA command vehicle": "C2",
    "R-149MA1 command and staff vehicle": "C2",
    "Barnaul-T 9С932-1 automated system for air defence units": "C2",
    "R-166-0.5 signals vehicle": "C2",
    "P-260 Redut-2US communication system": "C2",
    "R-381T2M 1.5-3000 MHz radio monitoring station from a modernised R-381TM Taran-M automatic signals intelligence complex": "C2",
    "R-441 SatCom station": "C2",
    "P-230T command vehicle": "C2",

    "C2": "Support",

    # Engineering Vehicles And Equipment
    "UR-77 'Meteorit'  mine clearing vehicle" : "(De-)Mining",
    "UR-67 mine clearing charge on BTR-D APC" : "(De-)Mining",
    "Uran-6 mine-clearing robotic system" : "(De-)Mining",
    "GMZ-3 minelayer" : "(De-)Mining",
    "BREM-Ch ''BREM-4'' armoured recovery vehicle" : "Recovery",
    "BREM-D armoured recovery vehicle" : "Recovery",
    "BREM-K armoured recovery vehicle" : "Recovery",
    "BTS-4A armoured recovery vehicle" : "Recovery",
    "BREM-1 armoured recovery vehicle" : "Recovery",
    "Ural-4320 KET-L recovery vehicle" : "Recovery",
    "BREM-2 armoured recovery vehicle" : "Recovery",
    "Ural-4320 KT-L recovery vehicle" : "Recovery",
    "MTP-A2.1 recovery vehicle" : "Recovery",
    "REM-KL recovery vehicle" : "Recovery",
    "MTP-A2 recovery vehicle" : "Recovery",
    "Mobile generator for Podlet-K1 low-altitude S-band surveillance radar" : "Engineering",
    "ARS-14 decontamination and degassing vehicle" : "Other Engineering",
    "Ural-4320 with KS-3574M3 or KS-3574M crane" : "Other Engineering",
    "KamAZ-63501 with KS-55729-7M 32-ton crane" : "Other Engineering",
    "IMR-2(M) combat engineering vehicle" : "Other Engineering",
    "KamAZ-5350 with EOV-3523 excavator" : "Other Engineering",
    "RKhM-6 CBRN reconnaissance vehicle" : "Other Engineering",
    "IMR-3M combat engineering vehicle" : "Other Engineering",
    "KamAZ-5350 with KS-45719-7M crane" : "Other Engineering",
    "ED2x30-T400-3RA mobile generator" : "Other Engineering",
    "BAT-2 heavy engineering vehicle" : "Other Engineering",
    "KamAZ KMV-10V boom crane truck" : "Other Engineering",
    "APA-80 engine starting vehicle" : "Other Engineering",
    "MDK-3 trench-digging vehicle" : "Other Engineering",
    "PZM-2 trench-digging vehicle" : "Other Engineering",
    "MTO-UB1 maintenance vehicle" : "Other Engineering",
    "Ural-4320 with excavator" : "Other Engineering",
    "KrAZ-255B with excavator" : "Other Engineering",
    "MTO-AT mobile workshop" : "Other Engineering",
    "RKhM-6 Povozka" : "Other Engineering",
    "MTO-AG-3M" : "Other Engineering",
    "BMK-130M/BMK-150 towing and motor boat" : "Water Crossing",
    "PTS-2  tracked amphibious transport" : "Water Crossing",
    "BMK-460 towing and motor boat" : "Water Crossing",
    "BMK-MT towing and motor boat" : "Water Crossing",
    "BMK-MO towing and motor boat" : "Water Crossing",
    "PP-2005 floating bridge" : "Water Crossing",
    "MTU-72 bridge layer" : "Water Crossing",
    "PMP floating bridge" : "Water Crossing",
    "TMM-3 bridge layer" : "Water Crossing",
    "Pontoon bridge" : "Water Crossing",

    "(De-)Mining": "Engineering",
    "Recovery": "Engineering",
    "Other Engineering": "Engineering",
    "Water Crossing": "Engineering",

    "Engineering": "Support",

    # Self-Propelled Anti-Tank Missile Systems
    "9P163M-1 Kornet-T" : "SPATMS",
    "9P149 Shturm-S" : "SPATMS",
    "9P148 Konkurs" : "SPATMS",

    "SPATMS": "Artillery",

    # Artillery Support Vehicles And Equipment
    "1V13(M) battery fire control center" : "Artillery Support",
    "1V14 battery command and forward observer vehicle" : "Artillery Support",
    "1V16 battalion fire direction vehicle" : "Artillery Support",
    "9T452 transporter-loader (for BM-27 'Uragan' MRL)" : "Artillery Support",
    "TZM-T reloader vehicle (for TOS-1A)" : "Artillery Support",
    "1V18 'Klyon-1' artillery command and forward observer vehicle" : "Artillery Support",
    "2F77M transloading vehicle for 2K22M Tunguska-M" : "Artillery Support",
    "1V110 BM-21 Grad battery command vehicle" : "Artillery Support",
    "1V1003 command and observation vehicle (for 1V198 artillery fire control system)" : "Artillery Support",
    "PRP-4A Argus artillery reconnaissance vehicle" : "Artillery Support",
    "1V119 artillery fire direction vehicle" : "Artillery Support",
    "1V15M fire control and observation vehicle" : "Artillery Support",

    "Artillery Support": "Artillery",

    # Towed Artillery
    "120mm 2B16 Nona-K howitzer": "Towed Artillery",
    "152mm 2A36 Giatsint-B": "Towed Artillery",
    "2B9 Vasilek 82mm automatic gun mortar": "Towed Artillery",
    "152mm D-20 gun-howitzer": "Towed Artillery",
    "152mm 2A65 Msta-B howitzer": "Towed Artillery",
    "100mm MT-12 anti-tank gun": "Towed Artillery",
    "122mm D-30 howitzer": "Towed Artillery",
    "Unknown towed artillery": "Towed Artillery",

    "Towed Artillery": "Artillery",

    # Self-Propelled Artillery
    "240mm 2S4 Tyulpan": "SPA",
    "152mm 2S5 Giatsint-S": "SPA",
    "Unknown SPG": "SPA",
    "120mm 2S9 Nona": "SPA",
    "122mm 2S1 Gvozdika": "SPA",
    "152mm 2S19 Msta-S": "SPA",
    "152mm 2S3(M) Akatsiya": "SPA",
    "203mm 2S7M Malka": "SPA",
    "120mm 2S34 Khosta": "SPA",
    "120mm 2S23 Nona-SVK": "SPA",
    "152mm 2S33 Msta-SM2": "SPA",

    "SPA": "Artillery",

    # Multiple Rocket Launchers
    "220mm BM-27 Uragan": "MRL",
    "300mm BM-30 Smerch": "MRL",
    "122mm 2B17 Tornado-G": "MRL",
    "122mm 9P138 Grad-1": "MRL",
    "122mm BM-21 Grad": "MRL",
    "220mm TOS-1A": "MRL",
    "Unknown MRL": "MRL",

    "MRL": "Artillery",

    # Anti-Aircraft Guns
    "23mm ZU-23-2": "AA",

    # Self-Propelled Anti-Aircraft Guns
    "BTR-ZD Skrezhet": "SPAAG",
    "ZSU-23-4 Shilka": "SPAAG",
    "2K22M1 Tunguska": "SPAAG",

    "SPAAG": "AA",

    # Surface-To-Air Missile Systems
    "9K35 Strela-10": "SAM",
    "9A310M1-2 TELAR (for Buk-M1-2)": "SAM",
    "9K33 Osa": "SAM",
    "9A331M TLAR (for 9K332 Tor-M2)": "SAM",
    "9A316 TEL (for Buk-M2)": "SAM",
    "9A317 TELAR (for Buk-M2)": "SAM",
    "9K331MDT Tor-M2DT": "SAM",
    "Unknown Buk SAM system": "SAM",
    "9A39M1-2 TEL (for Buk-M1-2)": "SAM",
    "9A331 TLAR (for 9K331 Tor-M1)": "SAM",
    "5P85SM2-01 (launcher for S-400)": "SAM",
    "Pantsir-S1": "SAM",
    "9A330 Tor TLAR (for 9K330 Tor)": "SAM",
    "5P85SD/SM (launcher for S-300 PMU(-1))": "SAM",

    "SAM": "AA",

    # Radars
    "Fara ground surveillance radar": "Radar",
    "9S36 (for Buk-M2)": "Radar",
    "SNAR-10M1 battlefield surveillance radar": "Radar",
    "9S18 Kupol TUBE ARM Search and Acquisition Radar for Buk-M2": "Radar",
    "1L271 portable mortar locating reconnaissance radar": "Radar",
    "Unknown radar": "Radar",
    "9S18М1(-3) (for Buk-M3)": "Radar",
    "48Ya6-K1 Podlet-K1 low-altitude S-band surveillance radar": "Radar",
    "PPRU-1(M) '9S80(-1)' 'Sborka' (for 9K35 Strela-10)": "Radar",
    "P-18T": "Radar",
    "9S18М1(-2) (for Buk-M2)": "Radar",
    "1L261 (for 1L260 Zoopark-1M counter-battery radar complex)": "Radar",
    "P-18-2 2D VHF surveillance radar": "Radar",

    "Radar": "AA",

    # Jammers And Deception Systems
    "RLK-MC-A (ROSC-1) counter-UAV system": "EW",
    "Leer-2 electronic warfare system": "EW",
    "RB-636AM2 Svet-KU EW system": "EW",
    "Torn(-MDM)": "EW",
    "1L262E Rtut-BM": "EW",
    "R-330ZH Zhitel": "EW",
    "R-330BMV Borisoglebsk-2B": "EW",
    "Unknown EW system": "EW",
    "Silok-01 counter-UAV system": "EW",
    "1RL257 Krasukha-4 (command post)": "EW",

    "EW": "All",

    # Aircraft
    "Su-35S multirole aircraft": "Fixed Wing",
    "Su-30SM multirole aircraft": "Fixed Wing",
    "Tu-22M3 strategic bomber": "Fixed Wing",
    "Su-34M strike aircraft": "Fixed Wing",
    "Su-24M/MR strike/tactical reconnaissance aircraft": "Fixed Wing",
    "Su-24MR tactical reconnaissance aircraft": "Fixed Wing",
    "MiG-31BM fighter aircraft": "Fixed Wing",
    "Su-34 strike aircraft": "Fixed Wing",
    "Unknown Su-30/Su-34/Su-35": "Fixed Wing",
    "Su-25 close air support aircraft": "Fixed Wing",
    "Tu-95MS strategic bomber": "Fixed Wing",
    "An-26 transport aircraft": "Fixed Wing",

    "Fixed Wing": "Aircraft",

    # Helicopters
    "Mi-28 attack helicopter": "Rotary Wing",
    "Mi-35M attack helicopter": "Rotary Wing",
    "Mi-24V/P attack helicopter": "Rotary Wing",
    "Mi-8 transport helicopter": "Rotary Wing",
    "Mi-24P/35M attack helicopter": "Rotary Wing",
    "Ka-52 'Alligator' attack helicopter": "Rotary Wing",
    "Mi-24P attack helicopter": "Rotary Wing",
    "Unknown helicopter": "Rotary Wing",

    "Rotary Wing": "Aircraft",

    # Unmanned Combat Aerial Vehicles
    "Forpost-RU": "UCAV",
    "Orion": "UCAV",
    "Korsar": "UCAV",
    "Mohajer-6": "UCAV",
    "Orlan-10 UCAV": "UCAV",

    "UCAV": "Aircraft",

    # Reconnaissance Unmanned Aerial Vehicles
    "Lastochka-M": "RUAV",
    "Grifon-12": "RUAV",
    "ZALA 421-16Е2": "RUAV",
    "Orlan-10": "RUAV",
    "Orlan-30": "RUAV",
    "Takhion": "RUAV",
    "Merlin-VR": "RUAV",
    "Granat-4": "RUAV",
    "Eleron-3": "RUAV",
    "Eleron T28ME": "RUAV",
    "Unknown reconnaissance UAV": "RUAV",
    "ZALA 421-16ЕM": "RUAV",
    "Orlan-10 'Moskit' jamming UAV": "RUAV",
    "Supercam S350": "RUAV",
    "Orlan-10 jamming UAV": "RUAV",
    "Forpost": "RUAV",
    "Supercam S150": "RUAV",
    "'Orlan-20' ''Kartograf''": "RUAV",

    "RUAV": "Aircraft",

    # Naval Ships
    "Project 1171 Tapir-class landing ship 'Saratov (BDK-65)'": "Ship",
    "Project 02510 BK-16E high-speed assault boat": "Ship",
    "Project 1164 Slava-class guided missile cruiser 'Moskva'": "Ship",
    "Project 03160 Raptor-class patrol boat": "Ship",
    "Project 775 Ropucha-class landing ship": "Ship",
    "Project 11770 Serna-class landing craft": "Ship",
    "Project 22870 SB-739 Vasily Bekh rescue tug": "Ship",
    "Project 266M Natya-class minesweeper": "Ship",

    "Ship": "All",

    # Trucks, Vehicles and Jeeps
    "Ural-63704-0010 Tornado-U": "Trucks&co",
    "Ural-542301 tank transporter": "Trucks&co",
    "KamAZ-6350 8x8 artillery tractor": "Trucks&co",
    "Civilian KamAZ 6x6 converted for military use": "Trucks&co",
    "UAZ-452 van": "Trucks&co",
    "UAZ-394511 ‘Esaul’": "Trucks&co",
    "Unknown fuel tanker": "Trucks&co",
    "(Unknown) vehicle": "Trucks&co",
    "Ural-375D": "Trucks&co",
    "UAZ-23632-148-64 armed pickup truck": "Trucks&co",
    "KamAZ 4x4": "Trucks&co",
    "LuAZ-969": "Trucks&co",
    "ZiL-131 tanker": "Trucks&co",
    "KamAZ-5350 with armoured cabin": "Trucks&co",
    "Ural Federal": "Trucks&co",
    "KamAZ 6x6": "Trucks&co",
    "UAZ-23632 pickup truck": "Trucks&co",
    "KrAZ-260 tanker": "Trucks&co",
    "GAZ-51": "Trucks&co",
    "Ural-4320": "Trucks&co",
    "(Unknown) truck": "Trucks&co",
    "KrAZ-255B": "Trucks&co",
    "Ural-4320 tanker": "Trucks&co",
    "UAZ-469 jeep": "Trucks&co",
    "GAZ Sobol": "Trucks&co",
    "MAZ TZ-500 tanker": "Trucks&co",
    "KamAZ 6x6 tanker": "Trucks&co",
    "GAZ-3308": "Trucks&co",
    "Ural-5323": "Trucks&co",
    "KamAZ 8x8": "Trucks&co",
    "KamAZ with MM-501 armoured cabin": "Trucks&co",
    "KrAZ-255B tanker": "Trucks&co",
    "KamAZ-395800 'Gorets'": "Trucks&co",
    "Ural-43206": "Trucks&co",
    "9T244 transloader (for 9A330/1 Tor)": "Trucks&co",
    "UAZ-31514": "Trucks&co",
    "UAZ-515195 'Esaul'": "Trucks&co",
    "KamAZ Avtozaks": "Trucks&co",
    "ZiL-131": "Trucks&co",
    "Ural-375D tanker": "Trucks&co",
    "UAZ Patriot jeep": "Trucks&co",
    "9T217 transloader (for 9K33 Osa)": "Trucks&co",
    "GAZ-66": "Trucks&co",
    "Ural Avtozaks": "Trucks&co",

    "Trucks&co": "Mobility",
}


def path_to_root(category: str) -> List[str]:
    path = []
    current_cat = category
    while (parent:=parent_index.get(current_cat)):
        path.append(parent)
        current_cat = parent
    return path

def walk_records(r: Record):
    for child in r.children:
        yield from walk_records(child)
    yield r

def test_index_validity(df: pl.DataFrame):
    models = df["model"].to_list()
    # Every model in the dataset must have an entry
    for model in models:
        assert model in parent_index
    # Every parent of an entry must have en entry or be the root
    for v in parent_index.values():
        assert v in parent_index or v=="All"
    # Every entry must connect back to root
    for k in parent_index.keys():
        assert path_to_root(k)[-1]=="All"
    # Models cannot be an inner node
    for model in models:
        assert model not in parent_index.values()
    # Nodes of the output structure must be a leaf with a losses value or an inner node with children
    root = df_to_records(df)
    for r in walk_records(root):
        assert bool(r.children) != bool(r.losses_total)
    return True

def dict_to_records(key: str, val: Union[int, defaultdict], img_index: Dict[str, List[Path]]) -> Record:
    if isinstance(val, int):
        return Record(name=key, losses_total=val, images=img_index[key])
    return Record(
        name=key,
        children=[dict_to_records(k,v, img_index) for k,v in val.items()],
        images=img_index[key])

def df_to_records(df: pl.DataFrame, img_index: Dict[str, List[Path]]) -> Record:
    tree = lambda: defaultdict(tree)
    root = tree()
    for row in df.rows():
        walker = root
        for asc in path_to_root(row[0])[::-1]:
            walker = walker[asc]
        walker[row[0]] = row[1]
    return dict_to_records("All", root["All"], img_index)

def losses_csv_to_hierarchical_jsonv2(input_csv_path: str, output_json_path: str):
    df = pl.read_csv(input_csv_path)
    root = df_to_records(df)
    with open(output_json_path, "w") as fp:
        fp.write(root.json())

def losses_csv_to_hierarchical_json(input_csv_path: str, output_json_path: str):
    df = pl.read_csv(input_csv_path)
    by_equipment = df.partition_by("equipment")
    equipment_records = []
    for idx, equipment_df in enumerate(by_equipment):
        by_model = equipment_df.partition_by("model")
        model_records = []
        for model_df in by_model:
            model_records.append(Record(name=model_df["model"][0], losses_total=model_df["losses_total"][0]))
        equipment_records.append(Record(name=equipment_df["equipment"][0], children=model_records))
    output = Record(name="total", children=equipment_records)
    with open(output_json_path, "w") as fp:
        fp.write(output.json())
