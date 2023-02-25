<script>
    import { onMount } from "svelte";
    import * as d3 from "d3";
    import TreeMap from "$lib/TreeMap.svelte";

    let data;
    onMount(async () => {
        await d3.json("/lossesv3.json").then((dt) => {
            data = dt
        })
    });
</script>

<div class="bg-stone-200 flex flex-row justify-center items-center min-h-screen">
    {#if data}
    <TreeMap
        width=800
        height=800
        {data}
        childrenAcc={(d)=>d.children}
        sumAcc={(d)=>d.losses_total}/>
    {/if}
</div>