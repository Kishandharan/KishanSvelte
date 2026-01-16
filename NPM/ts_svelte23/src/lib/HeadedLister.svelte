<script lang="ts">
  interface propsType1{
    heading:string;
    listItems:string[];
    listType:"ordered" | "unordered";
  }
  let {heading, listItems, listType}:propsType1 = $props();
</script>

<h1>{heading}</h1>
{#if listType=="ordered"}
  <ol>
    {#each listItems as item}
      <li>{item}</li>
    {/each}
  </ol>
{:else if listType=="unordered"}
  <ul>
    {#each listItems as item}
      <li>{item}</li>
    {/each}
  </ul>
{/if}
