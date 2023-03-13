<script>
    import "../app.css";
    import Icon from "$lib/Icon.svelte";
</script>

<header>
    <span class="flex flex-row" title="Слава Україні">🇺🇦 <img width="30px" src="/fella.webp"> 🇺🇦</span>
</header>
<main>
    <slot />
</main>
<footer>
    <a 
        target="_blank"
        rel="noreferrer noopener"
        href="https://github.com/onbernard/ukraine_2">
        <Icon src="/icons/github.svg" color="#dc8a78"/>
    </a>
</footer>

<style lang="postcss">
    @import "@catppuccin/palette/style";
    :global(body) {
        display: flex;
        flex-direction: column;
        min-height: 100dvh;
        margin: 0;
        padding: 0;
    }
    header {
        @apply fixed top-0 left-0 w-full h-8 flex flex-row justify-center items-center;
        @apply font-sans font-semibold;
        background-color: #dce0e8;
        color: var(--ctp-latte-text);
    }
    main {
        @apply mt-8;
        background-color: #eff1f5;
        flex: 1;
    }
    footer {
        @apply flex flex-row justify-center items-center h-8;
        background-color: #dce0e8;
    }
</style>