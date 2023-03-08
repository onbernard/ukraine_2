<script>
    export let sources;
</script>

<div class="ctnr">
    {#each sources as src}
    <img {src} alt="fkptn">
    {/each}
</div>

<style lang="postcss">
    .ctnr {
        @apply flex flex-row flex-wrap;
    }
    img {
    }
</style>