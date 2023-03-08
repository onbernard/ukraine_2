<script>
    export let src;
    export let size="20px";
    export let color="black";
</script>

<span id="ctnr" style="--size:{size}; --src: url({src}); --color: {color};"></span>

<style lang="postcss">
    #ctnr {
        display: block;
        width: var(--size);
        height: var(--size);
        mask: var(--src) center no-repeat;
        background-color: var(--color);
    }
</style>