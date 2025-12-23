<script lang="ts">
    let visibility:boolean = false;
    function handle1(){
        visibility = !(visibility);
    }
</script>

<button on:click={handle1}>Toggle Visibility</button>
{#if visibility}
    <p>Click the button, and I will be visible.</p>
{/if}
