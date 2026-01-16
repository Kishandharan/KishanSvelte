<script>
    import { page } from "$app/stores";
    $: name = $page.params.name;
</script>

<h1>Hello, {name}</h1>
