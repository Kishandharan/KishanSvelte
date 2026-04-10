<script>
  let list1 = $state([]);
  let inputElm;

  function handleClick(){
    list1.push(inputElm.value);
  }
</script>

<input bind:this={inputElm}>
<button onclick={handleClick}>Add item</button>
{#each list1 as item}
  <p>{item}</p>
{/each}
