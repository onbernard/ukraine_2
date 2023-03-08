<script>
    import "../app.css";
    import Icon from "$lib/Icon.svelte";
</script>

<header>
    🇺🇦
</header>
<main>
    <slot />
</main>
<footer>
    <a href="https://github.com/onbernard/ukraine_2">
        <Icon src="/icons/github.svg" color="#dc8a78"/>
    </a>
</footer>

<style lang="postcss">
    :global(body) {
        display: flex;
        flex-direction: column;
        min-height: 100dvh;
        margin: 0;
        padding: 0;
    }
    header {
        @apply fixed top-0 left-0 w-full h-8 flex flex-row justify-center items-center;
        background-color: #dce0e8
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