<script>
    import { createEventDispatcher, beforeUpdate, afterUpdate, tick } from 'svelte';
    import * as d3 from "d3";
    export let height = 800;
    export let width = 800;
    export let data;
    export let childrenAcc
    export let sumAcc;
    export let zoomOutHeight = 50;
    export let padding = 1;
    const dispatch = createEventDispatcher();
    
    let textElems = [];
    const treemap = d3.treemap()
        .size([width,height])
        .padding([padding])
        .tile(d3.treemapSquarify);
    let current = d3.hierarchy(data, childrenAcc);
    $: root = treemap(current.copy().sum(sumAcc));
    const zoomIn = (child, idx) => {
        if (child.children) {
            current = current.children[idx];
        }
        else {
            dispatch("leaf", child.data);
        }
    }
    const zoomOut = () => {
        if (current.parent) {
            current = current.parent;
        }
    }
    const childWidth = (child) => (child.x1-child.x0);
    const childHeight = (child) => (child.y1-child.y0);
    let hoveredId;
    let hoveredChild;
    let hovered=false;
    const hoverEnterRect = (idx) => {
        if (isOverflowing(idx)){
            hoveredId = idx;
            hoveredChild = root.children[idx];
            hovered = true;
        }
    }
    const hoverLeaveRect = () => {
        hoveredId = null;
        hoveredChild = null;
        hovered = false;
    }
    const isOverflowingRight = (idx) => {
        return root.children[idx].x0+textElems[idx].getBBox().x + textElems[idx].getBBox().width > width;
    }
    const isOverflowingLeft = (idx) => {
        return root.children[idx].x0+textElems[idx].getBBox().x < 0;
    }
    const isOverflowingBottom = (idx) => {
        return root.children[idx].y0+textElems[idx].getBBox().y + textElems[idx].getBBox().height > height;
    }
    const isOverflowingTop = (idx) => {
        return root.children[idx].y0+textElems[idx].getBBox().y < 0;
    }
    const isOverflowing = (idx) => (
        textElems[idx].getBBox().width > childWidth(root.children[idx]) ||
        isOverflowingRight(idx) ||
        isOverflowingLeft(idx) ||
        isOverflowingBottom(idx) ||
        isOverflowingTop(idx)
    )
    const overflowOffsetX = (idx) => {
        if (isOverflowingRight(idx)) {
            return root.children[idx].x0+textElems[idx].getBBox().x + textElems[idx].getBBox().width - width;
        }
        else if (isOverflowingLeft(idx)) {
            return root.children[idx].x0+textElems[idx].getBBox().x;
        }
        return 0;
    }
    const overflowOffsetY = (idx) => {
        if (isOverflowingBottom(idx)) {
            return root.children[idx].y0+textElems[idx].getBBox().y + textElems[idx].getBBox().height - height;
        }
        else if (isOverflowingTop(idx)) {
            return root.children[idx].y0+textElems[idx].getBBox().y;
        }
        return 0;
    }
    const overflow = (idx) => {
        let outp= `translate(${root.children[idx].x0-overflowOffsetX(idx)},${root.children[idx].y0-overflowOffsetY(idx)})`
        console.log(outp)
        return outp
    }
    afterUpdate(()=>{
        textElems = textElems;
    })
</script>

<svg height={+height+zoomOutHeight} {width}>
    <rect class="go-back" on:click={zoomOut} on:keyup
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
                on:click={()=>zoomIn(child, idx)} on:mouseenter={()=>hoverEnterRect(idx)} on:mouseleave={hoverLeaveRect} on:keyup
                transform="translate({child.x0},{child.y0})"
            >
                
                <rect
                    style="--border:{padding}"
                    class="model-rect"
                    class:clickable={child.children}
                    width={childWidth(child)}
                    height={childHeight(child)}
                    stroke="black"
                />
                
            </g>
        {/each}
        {#each root.children as child, idx}
            <g
                id={idx}
                on:click={()=>zoomIn(child, idx)} on:mouseenter={()=>hoverEnterRect(idx)} on:mouseleave={hoverLeaveRect} on:keyup
                transform="translate({child.x0},{child.y0})"
            >
                <clipPath id="clip{idx}">
                    <rect
                    width={childWidth(child)}
                    height={childHeight(child)}
                />
                </clipPath>
                {#if textElems[idx]}
                    <rect
                        class="text-box"
                        clip-path="url(#clip{idx})"
                        x={textElems[idx].getBBox().x}
                        y={textElems[idx].getBBox().y}
                        width={textElems[idx].getBBox().width}
                        height={textElems[idx].getBBox().height}/>                    
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
            <g transform={overflow(hoveredId)} class="hovered-ctnr">
                <rect
                    class="text-box"
                    x={textElems[hoveredId].getBBox().x}
                    y={textElems[hoveredId].getBBox().y}
                    width={textElems[hoveredId].getBBox().width}
                    height={textElems[hoveredId].getBBox().height}
                />
                <text
                    x={+childWidth(hoveredChild)/2.}
                    y={+childHeight(hoveredChild)/2.}
                    dominant-baseline="middle"
                    text-anchor="middle"
                >{root.children[hoveredId].data.name}</text>
            </g>
            {/if}
        </g>
</svg>

<style lang="postcss">
    svg {
        @apply bg-white;
    }
    text {
        font-size: small;
        font-weight: 700;
        fill: #263238;
        pointer-events: none;
        background-color: red;
    }
    .text-box {
        fill: #eff1f5;
        stroke-width: 1px;
        stroke: #7c7f93;
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
    .hovered-ctnr {
        pointer-events: none;
    }
</style>