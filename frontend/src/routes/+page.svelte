<script>
    import { onMount } from "svelte";
    import * as d3 from "d3";
    import TreeMap from "$lib/TreeMap.svelte";
    import { fade } from 'svelte/transition';

    let innerWidth;
    let innerHeight;
    let data;
    onMount(async () => {
        await d3.json("/losses_russia.json").then((dt) => {
            data = dt
        })
    });
    let sources;
    let treemapWidth, treemapHeight;
    const onLeaf = (dt) => {
        sources = [];
        sources = dt?.images;
    }
</script>

<svelte:window bind:innerHeight bind:innerWidth/>

<div class="tree-grid-ctnr">
    {#if data}
    <div class="left treemap-ctnr" transition:fade bind:clientWidth={treemapWidth} bind:clientHeight={treemapHeight}>
        <TreeMap
            on:leaf={e=>onLeaf(e.detail)}
            width={treemapWidth}
            height={treemapHeight}
            {data}
            childrenAcc={(d)=>d.children}
            sumAcc={(d)=>d.losses_total}/>
    </div>
    {:else}
        <div class="left treemap-placeholder">
            Loading...
        </div>
    {/if}
    {#if sources}
        <div class="right img-grid-ctnr">
            {#each sources as src}
                <img {src} alt={src}>
            {/each}
        </div>
    {:else}
        <div class="right img-grid-placeholder">
            Click on a leaf...
        </div>
    {/if}
</div>

<style lang="postcss">
    .tree-grid-ctnr {
        @apply flex flex-row items-center justify-around;
        @apply rounded-md;
        @apply m-2 p-2;
        height: 60rem;
        border: 3px solid var(--ctp-latte-overlay0);
    }
    .left {
        flex: 1 1 500px;
    }
    .treemap-ctnr {
    }
    .treemap-placeholder {
        @apply flex flex-row justify-center items-center;
    }
    .right {
        flex: 1 1 500px;
        min-height: 100%;
    }
    .img-grid-ctnr {
        @apply flex flex-col items-center overflow-y-scroll snap-y snap-mandatory;
        max-height: 500px;
    }
    .img-grid-ctnr > img {
        @apply p-2;
    }
    .img-grid-placeholder {
        @apply flex flex-row justify-center items-center;
        @apply font-sans font-semibold;
        color: var(--ctp-latte-text);
    }
</style>