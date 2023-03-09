<script>
    import { onMount } from "svelte";
    import * as d3 from "d3";
    import TreeMap from "$lib/TreeMap.svelte";
    import ImageGrid from "$lib/ImageGrid.svelte";

    let innerWidth;
    let data;
    onMount(async () => {
        await d3.json("/losses_russia.json").then((dt) => {
            data = dt
        })
    });
    let current;
    let sources = [];
</script>

<svelte:window bind:innerWidth/>

<div class="flex flex-col items-center">
    {#if data}
    <TreeMap
        on:leaf={(e)=>{current=e.detail}}
        width={innerWidth-50}
        height={innerWidth-50}
        {data}
        childrenAcc={(d)=>d.children}
        sumAcc={(d)=>d.losses_total}/>
    {:else}
        loading...
    {/if}
    {#if current}
    <ImageGrid sources={current.images}/>
    {/if}
</div>

