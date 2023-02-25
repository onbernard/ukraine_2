const crayola_colors = [
    "#F35623",
    "#EF2732",
    "#8A161F",
    "#B13396",
    "#EA579E",
    "#F693BF",
    "#653414",
    "#CBAB84",
    "#007FB2",
    "#025C65",
    "#009247",
    "#81A028",
    "#F5F243",
    "#FEF200",
    "#F67321",
    "#F25920",
    "#FFFFFF",
    "#737278",
    "#231F20",
    "#2C1543",
    "#6E3B98",
    "#59469F",
    "#122C67",
    "#185B90"
]

export const crayola_scheme = (idx) => {
    return crayola_colors(idx%24);
}