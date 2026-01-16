<script>
  let count = 0;
</script>

<button on:click={count++}>Increase Count</button>

{#if count>=1}
  <p>The count is greater than or equal to 1✅</p>
{/if}
{#if count>=2}
  <p>The count is greater than or equal 2✅</p>
{/if}
{#if count>=3}
  <p>The count is greater than or equal 3✅</p>
{/if}
{#if count>=4}
  <p>The count is greater than or equal 4✅</p>
{/if}

<style>
</style>
