<script>
    import { onMount } from "svelte";
    import * as d3 from "d3";
    import TreeMap from "$lib/TreeMap.svelte";
    import Icon from "$lib/Icon.svelte";
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
    let model;
    let losses;
    let treemapWidth, treemapHeight;
    const onLeaf = (dt) => {
        sources = [];
        losses = dt?.losses_total;
        model = dt?.name;
        sources = dt?.images;
        console.log(dt)
    }
</script>

<svelte:window bind:innerHeight bind:innerWidth/>

<div class="ctnr m-4">
    <span class="m-auto pt-2">
        Click on a square to zoom in, click on top to zoom out
    </span>
    <div class="tree-grid-ctnr">
        {#if data}
        <div class="left treemap-ctnr" transition:fade bind:clientWidth={treemapWidth} bind:clientHeight={treemapHeight}>
            {#key treemapHeight, treemapWidth}
            <TreeMap
                on:leaf={e=>onLeaf(e.detail)}
                width={treemapWidth-50}
                height={treemapHeight-50}
                {data}
                childrenAcc={(d)=>d.children}
                sumAcc={(d)=>d.losses_total}/>
            {/key}
        </div>
        {:else}
            <div class="left treemap-placeholder">
                Loading...
            </div>
        {/if}
        {#if sources}
            <div class="right img-grid-ctnr">
                {model} : {losses}
                {#each sources as src}
                    <img {src} alt={src}>
                {:else}
                    <span class="row-span-full col-span-full">It seems there are not images there</span>
                {/each}
            </div>
        {:else}
            <div class="right img-grid-placeholder">
                Click on a leaf...
            </div>
        {/if}
    </div>
    <span class="m-auto flex flex-row">
        Sources: 
        <a
            class="mx-10 flex flex-row"
            href="https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html"
            target="_blank"
            rel="noreferrer noopener">
            <img src="/oryx.png" alt="oryx-logo" width="20px">
                Oryx blog
        </a>
        via
        <a
            class="ml-10 mr-4 flex flex-row"
            href="https://www.kaggle.com/datasets/piterfm/2022-ukraine-russia-war-equipment-losses-oryx"
            target="_blank"
            rel="noreferrer noopener">
                <Icon src="/kaggle.svg" color="#434555"/>dataset
        </a>
        (last pulled on the 5th of february 2023)
    </span>
</div>

<style lang="postcss">
    .ctnr {
        @apply flex flex-col;
        @apply rounded-md;
        @apply font-sans font-semibold;
        height: 60rem;
        border: 3px solid var(--ctp-latte-overlay0);
        color: var(--ctp-latte-text);
    }
    .tree-grid-ctnr {
        @apply grid grid-cols-2 gap-2;
        @apply m-2 p-2;
        flex-basis: 100%
    }
    .left {
        @apply flex flex-row justify-center items-center;
    }
    .treemap-ctnr {
    }
    .treemap-placeholder {
        @apply flex flex-row justify-center items-center;
    }
    .right {
        min-height: 100%;
    }
    .img-grid-ctnr {
        @apply flex flex-col items-center overflow-y-scroll snap-y snap-mandatory;
        @apply font-sans font-semibold;
        color: var(--ctp-latte-text);
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