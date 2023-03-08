<script>
    import { createEventDispatcher } from 'svelte';
    import * as d3 from "d3";
    export let height = 800;
    export let width = 800;
    export let data;
    export let childrenAcc
    export let sumAcc;
    export let zoomOutHeight = 50;
    export let padding = 1;
    const dispatch = createEventDispatcher();
    
    $: textElems = [];
    const x = d3.scaleLinear()
        .domain([0,1])
        .range([0,width]);
    const y = d3.scaleLinear()
        .domain([0,1])
        .range([0,height]);
    const treemap = d3.treemap()
        .size([width,height])
        .padding([padding])
        .tile(d3.treemapSquarify);
    let current = d3.hierarchy(data, childrenAcc);
    $: root = treemap(current.copy().sum(sumAcc));
    $: {console.log(root)}
    const zoomIn = (child, idx) => {
        if (child.children) current = current.children[idx];
        else {
            dispatch("leaf", child.data);
        }
    }
    const zoomOut = () => {
        if (current.parent) current = current.parent;
    }
    const childWidth = (child) => (child.x1-child.x0);
    const childHeight = (child) => (child.y1-child.y0);
    let hoveredId;
    let hoveredChild;
    let hovered=false;
    const hoverEnterRect = (idx) => {
        if (textElems[idx].getBBox().width > childWidth(root.children[idx])){
            hoveredId = idx;
            hoveredChild = root.children[idx];
            hovered = true;
        }
    }
    const hoverLeaveRect = (idx) => {
        hoveredId = null;
        hoveredChild = null;
        hovered = false;
    }
</script>

<svg height={+height+zoomOutHeight} {width}>
    <rect class="go-back" on:click={zoomOut}
        width={width-2*padding}
        height={zoomOutHeight-2*padding}
        x={padding}
        y={padding}
        fill={current.parent?"#acb0be":"#ccd0da"}
    />
    <text x=5 y={zoomOutHeight/2+7}>Click to zoom out</text>
    <text x={width/2} y={zoomOutHeight/2+7}>{current.data.name}:{root.value}</text>

    <g transform="translate(0,{zoomOutHeight})">
        {#each root.children as child, idx}
            <g
                id={idx}
                on:click={()=>zoomIn(child, idx)} on:mouseenter={()=>hoverEnterRect(idx)} on:mouseleave={()=>hoverLeaveRect(idx)}
                transform="translate({child.x0},{child.y0})"
            >
                <clipPath id="clip{idx}">
                    <rect
                    width={childWidth(child)}
                    height={childHeight(child)}
                />
                </clipPath>
                <rect
                    style="--border:{padding}"
                    class="model-rect"
                    class:clickable={child.children}
                    width={childWidth(child)}
                    height={childHeight(child)}
                    stroke="black"
                />
                {#if textElems[idx]}
                <rect
                    class="text-box"
                    x={textElems[idx].getBBox().x}
                    y={textElems[idx].getBBox().y}
                    width={textElems[idx].getBBox().width}
                    height={textElems[idx].getBBox().height}
                />
                {/if}
                <text bind:this={textElems[idx]} id="text{idx}"
                    clip-path="url(#clip{idx})"
                    x={childWidth(child)/2.}
                    y={childHeight(child)/2.}
                    dominant-baseline="middle"
                    text-anchor="middle">
                    {child.data.name}
                </text>
            </g>
            {/each}
            {#if hovered}
                <text
                    x={root.children[hoveredId].x0+childWidth(root.children[hoveredId])/2.}
                    y={root.children[hoveredId].y0+childHeight(root.children[hoveredId])/2.}
                    dominant-baseline="middle"
                    text-anchor="middle"
                >{root.children[hoveredId].data.name}</text>
            {/if}
        </g>
</svg>

<style lang="postcss">
    svg {
        @apply bg-white;
    }
    text {
        font-size: small;
        font-weight: 600;
        fill: #263238;
        pointer-events: none;
        background-color: red;
    }
    .text-box {
        fill: white;
    }
    .model-rect {
        fill: #ccd0da;
        stroke: none;
    }
    .model-rect.clickable {
        fill: #acb0be;
    }
    .model-rect.clickable:hover {
        stroke-width: var(--border);
        stroke: #7c7f93;
    }
</style>