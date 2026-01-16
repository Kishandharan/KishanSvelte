<script lang="ts">
  let items : string[] = ["apple", "banana", "strawberry", "pineapple", "watermelon"];
  let searchInput : string = "";
</script>

<input bind:value={searchInput}>
{#each items as item}
  {#if item.includes(searchInput.toLowerCase())}
    <p>{item}</p>
  {/if}
{/each}


<style>
  /* your styles go here */
</style>
