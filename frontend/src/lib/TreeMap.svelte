<script>
    import * as d3 from "d3";
    export let height = 800;
    export let width = 800;
    export let colors = d3.scaleOrdinal().range(d3.schemeDark2);
    export let data;
    export let childrenAcc
    export let sumAcc;
    export let border = 2;
    export let zoomOutHeight = 50;

    const treemap = d3.treemap()
        .tile(d3.treemapBinary);
    let current = d3.hierarchy(data, childrenAcc);
    $: root = treemap(current.copy().sum(sumAcc));
    const zoomIn = (child, idx) => {
        if (child.children) current = current.children[idx];
    }
    const zoomOut = () => {
        if (current.parent) current = current.parent;
    }
    let hovered="";
</script>

<svg {height} {width} >
    <rect on:click={zoomOut}
        x=0
        y=0
        width={width}
        height={zoomOutHeight}
        fill={current.parent?"grey":"lightgrey"}
        stroke-width={border}
        stroke="lightgrey"/>
    <text x=5 y={zoomOutHeight/2+10}>Zoom out</text>
    {#each root.children as child, idx}
    <g id={idx} on:click={()=>zoomIn(child, idx)} on:mouseover={()=>{hovered=idx}}>
        <rect class="model-rect" class:clickable={child.children}
        x={child.x0*width}
        y={child.y0*height + zoomOutHeight}
        width={Math.max(1,(child.x1-child.x0)*width)}
        height={Math.max(1,(child.y1-child.y0)*height)}
        fill={colors(child.data.name)}
        stroke-width={border}
        stroke="black"/>
        <text
            x={5 + child.x0*width}
            y={child.y0*height + zoomOutHeight + 20}
        >{child.data.name}</text>
    </g>
    {/each}
</svg>

<style lang="postcss">
    svg {
    @apply bg-black;
    }
    text {
        font-size: large;
        font-weight: 600;
        fill: white;
    }
    .model-rect {
        stroke: lightgrey;
    }
    .model-rect.clickable {
        stroke: white;
    }
    #hovered > .model-rect {
        fill: black;
    }
</style>